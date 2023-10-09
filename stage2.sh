#!/bin/bash

set -e

. ./env

cmake_version=3.27.7
rpm_version=4.19.0
rpmdevtools_version=9_6

case $1 in
    init)
        podman stop -t 0 lfs-stage2
        podman rm -f lfs-stage2
        podman build -t lfs-stage2 containers/lfs-stage2
        podman create \
            --name lfs-stage2 \
            --hostname lfs-stage2 \
            --userns keep-id \
            --volume "$builddir:/home/lfs/rpmbuild:z" \
            --volume .:/home/lfs/lfs-rpm:z \
            lfs-stage2
        podman start lfs-stage2
        ;;
    start)
        podman start lfs-stage2
        ;;
    stop)
        podman stop lfs-stage2
        ;;
    shell)
        exec podman exec -it lfs-stage2 /usr/bin/bash
        ;;
    root-shell)
        exec podman exec --user root -it lfs-stage2 /usr/bin/bash
        ;;
    download)
        ( cd $builddir/SOURCES &&
            wget -nc https://github.com/Kitware/CMake/releases/download/v${cmake_version}/cmake-${cmake_version}.tar.gz &&
            wget -nc https://ftp.osuosl.org/pub/rpm/releases/rpm-4.19.x/rpm-${rpm_version}.tar.bz2
        )
        packages=$(cat containers/lfs-stage2/stage2.txt)
        for package in $packages; do
            spectool -g -C $HOME/.local/cache/lfs/rpmbuild/SOURCES specs/stage2/${package}.spec
        done
        ;;
    bootstrap)
        exec podman exec --user root -it lfs-stage2 /home/lfs/lfs-rpm/containers/lfs-stage2/rpm-bootstrap.sh
        ;;
    build)
        packages=$(cat containers/lfs-stage2/stage2.txt)
        for package in $packages; do
            podman exec -it lfs-stage2 rpmbuild -ba lfs-rpm/specs/stage2/${package}.spec
            podman exec --user root -it lfs-stage2 rpm -i --replacefiles rpmbuild/RPMS/${package}-*.rpm
        done
        ;;
    *)
        echo "invalid command"
        exit 1
esac
