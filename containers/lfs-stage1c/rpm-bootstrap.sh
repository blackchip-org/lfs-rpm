#!/bin/bash

set -e -x

srcdir=/home/lfs/rpmbuild/SOURCES
export MAKEFLAGS=-j${lfs_nproc}

mkdir -p /home/lfs/rpm-bootstrap

cd /home/lfs/rpm-bootstrap
tar xf $srcdir/cmake-*.tar.gz
cd cmake-*
./bootstrap -- -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_USE_OPENSSL=OFF
make
make install

cd /home/lfs/rpm-bootstrap
rm -rf rpm-*
tar xf $srcdir/rpm-*.tar.bz2
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
      ..
make
make install
