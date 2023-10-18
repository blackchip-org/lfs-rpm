#!/bin/bash

set -e

[ -z "$lfsdir" ]    && lfsdir=$HOME/.local/cache/lfs
[ -z "$nproc" ]    && nproc=$(nproc)

if [ "$with_check" != "1" ] ; then
    rpm_nocheck="--nocheck"
fi

builddir="$lfsdir/rpmbuild"
arch=$(arch)

lfs_version=12.0
cmake_version=3.27.7
rpm_version=4.19.0
kernel_version=6.4.12

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

lfs-kernel() {
    ( cd $builddir/SOURCES &&
        wget -nc https://www.kernel.org/pub/linux/kernel/v6.x/linux-${kernel_version}.tar.xz )
    podman exec -t lfs-stage3 lfs-rpm/containers/lfs-stage3/build-kernel.sh
    podman cp lfs-stage3:/home/lfs/dist/boot-lfs-${lfs_version}.tar.gz "$lfsdir"
    podman cp lfs-stage3:/home/lfs/dist/modules-lfs-${lfs_version}.tar.gz "$lfsdir"
}

lfs-qcow2() {
    set -x
    qcow2file="$lfsdir/lfs-${lfs_version}.qcow2"
    rawfile="$lfsdir/lfs-${lfs_version}.raw"
    rm -f "$qcow2file" "$rawfile"
    qemu-img create -f qcow2 "$qcow2file" 10G
    #dd if=/dev/zero of="$rawfile" count=1 bs=1 seek=10737418239
    sudo modprobe nbd
    sudo qemu-nbd --connect=/dev/nbd0 "$qcow2file"
    cat conf/qcow2/fdisk.txt | sudo fdisk /dev/nbd0
    sudo mkfs -t ext4 /dev/nbd0p1
    sudo mkdir -p /run/lfs
    sudo mount /dev/nbd0p1 /run/lfs
    sudo tar xf containers/lfs-stage3/lfs-stage2.tar.gz -C /run/lfs
    sudo tar xf "$lfsdir/boot-lfs-${lfs_version}.tar.gz" -C /run/lfs
    sudo tar xf "$lfsdir/modules-lfs-${lfs_version}.tar.gz" -C /run/lfs
    sudo cp -r conf/qcow2/fs/* /run/lfs
    #sudo chmod 755 /run/lfs/usr/lib/*.so*
    #sudo mkdir -p /run/lfs/boot/extlinux
    #sudo cp conf/qcow2/extlinux.conf /run/lfs/boot/extlinux/extlinux.conf
    #sudo extlinux --install /run/lfs/boot/extlinux
    #sudo bash -c 'cat /usr/share/syslinux/mbr.bin > /dev/nbd0'
    sudo umount /run/lfs
    sudo qemu-nbd --disconnect /dev/nbd0
    #sudo qemu-img convert -f raw -O qcow2 "$rawfile" "$qcow2file"
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
    kernel) lfs-kernel  && exit 0 ;;
    qcow2)  lfs-qcow2   && exit 0 ;;
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
        podman exec --user root lfs-$stage bash -c 'cd /home/lfs/rpmbuild/RPMS/* ; rpm --reinstall --justdb --nodeps $(ls *.rpm | grep -v "^lfs-")'
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
