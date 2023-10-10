#!/bin/bash

set -e

builddir=$HOME/.local/cache/lfs/rpmbuild
arch=$(arch)
nproc=$(nproc) 

prog="$(basename $0)"

usage() {
    cat 2>&1 <<EOF

Usage: $prog <stage> <command>

EOF
exit 2
}

case $1 in
    1)
        stage=stage1
        rpmbuild_flags=-bb
        ;;
    1a)
        stage=stage1a
        rpmbuild_flags=-bb
        ;;
    *)
        echo "$prog: error: invalid stage" 2>&1
        usage
esac


lfs-init() {
    mkdir -p "$builddir"

    set +e
    podman stop -t 0    lfs-$stage
    podman rm -f        lfs-$stage
    set -e

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
}

lfs-download() {
    packages="$(cat containers/lfs-$stage/$stage.pkg.txt)"
    for package in $packages; do
        spectool -g -C "$builddir/SOURCES" specs/$stage/${package}.spec
    done
}

lfs-build() {
    packages="$(cat containers/lfs-$stage/$stage.pkg.txt)"
    for package in $packages; do
        if ! podman exec lfs-$stage rpm -q $package ; then
            podman exec lfs-$stage rpmbuild $rpmbuild_flags lfs-rpm/specs/$stage/${package}.spec
            podman exec --user root lfs-$stage rpm -i --replacefiles rpmbuild/RPMS/$arch/${package}-*.rpm
        fi
    done
}

lfs-export() {
    if [ "$stage" == "stage1" ] ; then
        rm -f containers/lfs-stage1a/lfs-stage1.tar.gz
        podman exec --user root -t lfs-stage1 tar -C /lfs -c -z -f /tmp/lfs-stage1.tar.gz --exclude=./tools .
        podman cp lfs-stage1:/tmp/lfs-stage1.tar.gz containers/lfs-stage1a
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
    export)     lfs-export ;;
    bootstrap)  lfs-bootstrap ;;
    *)
        echo "$prog: error: invalid command" 2>&1
        usage
esac
