#!/bin/bash

set -e -x

elfutils_source=elfutils-0.190.tar.bz2
cmake_source=cmake-3.28.3.tar.gz
rpm_source=rpm-4.19.1.1.tar.bz2

srcdir=/build/rpmbuild/SOURCES
export MAKEFLAGS=-j${lfs_nproc}

mkdir -p /build/rpm-bootstrap

cd /build/rpm-bootstrap
rm -rf elfutils-*
tar xf $srcdir/$elfutils_source
cd elfutils-*
./configure --prefix=/usr                         \
            --disable-demangler                   \
            --disable-debuginfod                  \
            --enable-libdebuginfod=dummy
make
make install

cd /build/rpm-bootstrap
tar xf $srcdir/$cmake_source
cd cmake-*
./bootstrap -- -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_USE_OPENSSL=OFF
make
make install

cd /build/rpm-bootstrap
rm -rf rpm-*
tar xf $srcdir/$rpm_source
cd rpm-*
mkdir -p _build
cd _build
cmake \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_INSTALL_LIBDIR=/lib \
      -DENABLE_NLS=OFF \
      -DENABLE_OPENMP=OFF \
      -DENABLE_PYTHON=OFF \
      -DENABLE_SQLITE=OFF \
      -DENABLE_TESTSUITE=OFF \
      -DRPM_CONFIGDIR=/usr/lib/rpm \
      -DRPM_VENDOR=lfs \
      -DWITH_ACL=OFF \
      -DWITH_ARCHIVE=OFF \
      -DWITH_AUDIT=OFF \
      -DWITH_CAP=OFF \
      -DWITH_DBUS=OFF \
      -DWITH_FAPOLICYD=OFF \
      -DWITH_INTERNAL_OPENPGP=ON \
      -DWITH_SELINUX=OFF \
      -DWITH_READLINE=OFF \
      ..
make
make install
