#!/bin/bash

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
            --volume "$builddir:/root/rpmbuild:z" \
            --volume .:/root/lfs-rpm:z \
            lfs-stage2
        podman start lfs-stage2 
        ;;
    download)
        ( cd $builddir/SOURCES && 
            wget -nc https://github.com/Kitware/CMake/releases/download/v${cmake_version}/cmake-${cmake_version}.tar.gz && 
            wget -nc https://ftp.osuosl.org/pub/rpm/releases/rpm-4.19.x/rpm-${rpm_version}.tar.bz2  
        )
        ;;
    start)
        podman start lfs-stage2 
        ;;
    shell)
        exec podman exec -it lfs-stage2 /usr/bin/bash 
        ;;
    bootstrap)
        exec podman exec -it lfs-stage2 /root/lfs-rpm/containers/lfs-stage2/rpm-bootstrap.sh
        ;;
    *)
        echo "invalid command"
        exit 1
esac
