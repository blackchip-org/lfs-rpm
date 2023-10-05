#!/bin/bash -e

thisdir="$(dirname $0)"
specdir="$HOME/lfs-rpm/specs/stage1"
rpmdir="$HOME/rpmbuild/RPMS/$(uname -m)"

packages="
    binutils-lfs-tools
    gcc-lfs-tools
    linux-headers-lfs
    glibc-lfs
    gcc-libstdc++-lfs
    m4-lfs
    ncurses-lfs
    bash-lfs
    coreutils-lfs
    diffutils-lfs
    file-lfs
    findutils-lfs
    gawk-lfs
    grep-lfs
    gzip-lfs
    make-lfs
    patch-lfs
    sed-lfs
    tar-lfs
    xz-lfs
    binutils-lfs
    gcc-lfs
"

cd $specdir
for package in $packages; do
    rpmbuild -bb ${package}.spec
    if [ "$package" == "gcc-lfs" ] ; then
        sudo rpm -e gcc-libstdc++-lfs
    fi
    sudo rpm -i "$rpmdir/${package}*.rpm"
done