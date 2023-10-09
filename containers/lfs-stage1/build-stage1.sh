#!/bin/bash

set -e

thisdir="$(dirname $0)"
specdir="$HOME/lfs-rpm/specs/stage1"
rpmdir="$HOME/rpmbuild/RPMS/$(uname -m)"

packages="
    lfs-tools-binutils
    lfs-tools-gcc
    lfs-linux-headers
    lfs-glibc
    lfs-libstdc++
    lfs-m4
    lfs-ncurses
    lfs-bash
    lfs-coreutils
    lfs-diffutils
    lfs-file
    lfs-findutils
    lfs-gawk
    lfs-grep
    lfs-gzip
    lfs-make
    lfs-patch
    lfs-sed
    lfs-tar
    lfs-xz
    lfs-binutils
    lfs-gcc
    lfs-root-fs
    lfs-lua 
    lfs-pkg-config
    lfs-popt
    lfs-libgpg-error
    lfs-libgcrypt
    lfs-gettext
    lfs-zlib
    lfs-bzip2
    lfs-elfutils
"

cd $specdir
for package in $packages; do
    if ! rpm -q ${package}; then
        spectool -g -R ${package}.spec
        rpmbuild -bb ${package}.spec
        sudo rpm -i --replacefiles "$rpmdir/${package}*.rpm"
    fi
done
