#!/bin/bash

. ./env 

lua_version=5.4.6 
cmake_version=3.27.7
rpm_version=4.19.0
bzip2_version=1.0.8 
pkgconfig_version=0.29.2
zlib_version=1.2.13

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
            wget -nc http://www.lua.org/ftp/lua-${lua_version}.tar.gz && 
            wget -nc https://github.com/Kitware/CMake/releases/download/v${cmake_version}/cmake-${cmake_version}.tar.gz && 
            wget -nc https://www.sourceware.org/pub/bzip2/bzip2-${bzip2_version}.tar.gz && \
            wget -nc https://pkgconfig.freedesktop.org/releases/pkg-config-${pkgconfig_version}.tar.gz && \
            wget -nc https://anduin.linuxfromscratch.org/LFS/zlib-1.2.13.tar.xz && \
            wget -nc http://ftp.rpm.org/popt/releases/popt-1.x/popt-1.19.tar.gz && \
            wget -nc https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-1.10.2.tar.bz2 && \
            wget -nc https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-1.47.tar.bz2 && \
            wget -nc https://ftp.gnu.org/pub/gnu/gettext/gettext-0.22.3.tar.gz && \
            wget -nc https://sourceware.org/elfutils/ftp/elfutils-latest.tar.bz2 && \
            wget -nc https://ftp.osuosl.org/pub/rpm/releases/rpm-4.19.x/rpm-${rpm_version}.tar.bz2 )
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
