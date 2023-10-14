#!/bin/bash

set -e

[ -z "$builddir" ] && builddir=$HOME/.local/cache/lfs/rpmbuild
[ -z "$nproc" ]    && nproc=$(nproc)

if [ "$with_check" != "1" ] ; then
    rpm_nocheck="--nocheck"
fi

arch=$(arch)

cmake_version=3.27.7
rpm_version=4.19.0

prog="$(basename $0)"

usage() {
    cat 2>&1 <<EOF

Usage: $prog <stage> <command>
       $prog <stage> rpm <package>
       $prog info
EOF
exit 2
}

msg() {
    echo -e "\n----- $@"
}

case $1 in
    1)
        stage=stage1
        rpmbuild_flags="-bb $rpm_nocheck"
        ;;
    1a)
        stage=stage1a
        rpmbuild_flags="-bb $rpm_nocheck"
        rpm_flags="--nodeps"
        ;;
    2)
        stage=stage2
        rpmbuild_flags="-ba $rpm_nocheck"
        rpm_flags="--nodeps"
        ;;
    3)
        stage=stage3 
        ;;
    info)
        echo "builddir: $builddir"
        echo "arch:     $arch"
        echo "nproc:    $nproc"
        exit 0
        ;;
    *)
        echo "$prog: error: invalid stage" 2>&1
        usage
esac


lfs-init() {
    mkdir -p "$builddir"

    podman stop -t 0    lfs-$stage || true
    podman rm -f        lfs-$stage || true

    podman build \
        --build-arg nproc=$nproc \
        --tag       lfs-$stage \
        containers/lfs-$stage
    podman create \
        --name      lfs-$stage \
        --hostname  lfs-$stage \
        --userns    keep-id \
        --volume    "$builddir:/home/lfs/rpmbuild:z" \
        --volume    .:/home/lfs/lfs-rpm:z \
        lfs-$stage
    podman start    lfs-$stage

    if [ "$stage" == "stage3" ] ; then 
        podman exec --user root lfs-$stage bash -c 'cd /home/lfs/rpmbuild/RPMS/* ; rpm --reinstall --justdb --nodeps $(ls | grep -v "^lfs-")'
    fi 
}

lfs-download() {
    packages="$(cat containers/lfs-$stage/$stage.pkg.txt)"
    for package in $packages; do
        spectool -g -C "$builddir/SOURCES" specs/$stage/${package}.spec
    done

    if [ "$stage" == "stage1a" ] ; then
        ( cd $builddir/SOURCES &&
            wget -nc https://github.com/Kitware/CMake/releases/download/v${cmake_version}/cmake-${cmake_version}.tar.gz &&
            wget -nc https://ftp.osuosl.org/pub/rpm/releases/rpm-4.19.x/rpm-${rpm_version}.tar.bz2
        )
    fi
}
nproc=$(nproc)

lfs-build() {
    packages="$(cat containers/lfs-$stage/$stage.pkg.txt)"
    for package in $packages; do
        if ! podman exec lfs-$stage rpm -q $package ; then
            msg "building $stage:$package"
            podman exec lfs-$stage rpmbuild $rpmbuild_flags lfs-rpm/specs/$stage/${package}.spec
            podman exec --user root lfs-$stage rpm -i --replacefiles $rpm_flags rpmbuild/RPMS/$arch/${package}-*.rpm
        fi
    done
}

lfs-rpm() {
    package=$1
    if [ -z "$package" ] ; then
        echo "$prog: no package specified: $package" 2>&1
        usage
    fi
    podman exec lfs-$stage rpmbuild $rpmbuild_flags lfs-rpm/specs/$stage/${package}.spec
    podman exec --user root lfs-$stage rpm --reinstall --replacefiles $rpm_flags rpmbuild/RPMS/$arch/${package}-*.rpm
}

lfs-export() {
    if [ "$stage" == "stage1" ] ; then
        rm -f containers/lfs-stage1a/lfs-stage1.tar.gz
        podman exec --user root -t lfs-stage1 tar -C /lfs -c -z -f /tmp/lfs-stage1.tar.gz --exclude=./tools .
        podman cp lfs-stage1:/tmp/lfs-stage1.tar.gz containers/lfs-stage1a
    elif [ "$stage" == "stage1a" ] || [ "$stage" == "stage2" ] ; then
        [ "$stage" == "stage1a" ] && next_stage="stage2" || next_stage="stage3"
        rm -f containers/lfs-$next_stage/lfs-stage1a.tar.gz
        podman exec --user root -t lfs-$stage \
            tar -C / -c -z -f /tmp/lfs-$stage.tar.gz \
            --exclude='./tmp/*' \
            --exclude './home/lfs/*' \
            --exclude './root/*' \
            --exclude './dev/*' \
            --exclude './proc/*' \
            --exclude './sys/*' \
            --exclude './var/lib/rpm/*' \
            .
        podman cp lfs-$stage:/tmp/lfs-$stage.tar.gz containers/lfs-$next_stage
    fi
}

lfs-bootstrap() {
    if [ "$stage" == "stage1a" ] ; then
        podman exec --user root -t lfs-stage1a lfs-rpm/containers/lfs-stage1a/rpm-bootstrap.sh
    fi
}

case $2 in
    init)       lfs-init ;;
    start)      podman start lfs-$stage ;;
    stop)       podman stop  lfs-$stage ;;
    shell)      exec podman exec -it lfs-$stage /bin/bash ;;
    root-shell) exec podman exec --user root -it lfs-$stage /bin/bash ;;
    download)   lfs-download ;;
    build)      lfs-build ;;
    rpm)        lfs-rpm $3 ;;
    export)     lfs-export ;;
    bootstrap)  lfs-bootstrap ;;
    *)
        echo "$prog: error: invalid command" 2>&1
        usage
esac
