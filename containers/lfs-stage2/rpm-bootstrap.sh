#!/bin/bash 

set -e -x

lua_version=5.4.6
cmake_version=3.27.7 
rpm_version=4.19.0
bzip2_version=1.0.8 
pkgconfig_version=0.29.2
zlib_version=1.2.13

srcdir=/root/rpmbuild/SOURCES
export MAKEFLAGS=-j$(nproc)

mkdir /root/rpm-bootstrap
cd /root/rpm-bootstrap
rm -rf lua-${lua_version}
tar xf "$srcdir/lua-${lua_version}.tar.gz"
cd lua-${lua_version}
make "INSTALL_TOP=/usr" "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -fPIC" 
make install 

cd /root/rpm-bootstrap
tar xf "$srcdir/cmake-${cmake_version}.tar.gz"
cd cmake-${cmake_version}
./bootstrap -- -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_USE_OPENSSL=OFF
make 
make install 

cd /root/rpm-bootstrap
tar xf "$srcdir/bzip2-${bzip2_version}.tar.gz"
cd bzip2-${bzip2_version}
make -f Makefile-libbz2_so
make clean
make 
make PREFIX=/usr install
cp -av libbz2.so.* /usr/lib
ln -sv libbz2.so.1.0.8 /usr/lib/libbz2.so
cp -v bzip2-shared /usr/bin/bzip2
for i in /usr/bin/{bzcat,bunzip2}; do
  ln -sfv bzip2 $i
done

cd /root/rpm-bootstrap 
tar xf "$srcdir/pkg-config-${pkgconfig_version}.tar.gz"
cd pkg-config-${pkgconfig_version}
./configure --prefix=/usr --with-internal-glib
make 
make install 

cd /root/rpm-bootstrap 
tar xf "$srcdir/zlib-${zlib_version}.tar.xz"
cd zlib-${zlib_version}
./configure --prefix=/usr
make 
make install

cd /root/rpm-bootstrap 
tar xf "$srcdir/popt-1.19.tar.gz"
cd popt-1.19 
./configure --prefix=/usr
make 
make install 

cd /root/rpm-bootstrap 
tar xf "$srcdir/libgpg-error-1.47.tar.bz2"
cd libgpg-error-1.47
./configure --prefix=/usr
make 
make install 

cd /root/rpm-bootstrap 
tar xf "$srcdir/libgcrypt-1.10.2.tar.bz2"
cd libgcrypt-1.10.2 
./configure --prefix=/usr
make 
make install 

cd /root/rpm-bootstrap 
tar xf "$srcdir/gettext-0.22.3.tar.gz"
cd gettext-0.22.3 
./configure --prefix=/usr
make 
make install 

cd /root/rpm-bootstrap 
tar xf "$srcdir/elfutils-latest.tar.bz2"
cd elfutils-0.189
./configure --prefix=/usr \
            --disable-libdebuginfod \
            --disable-debuginfod
make
make install 

cd /root/rpm-bootstrap 
rm -rf rpm-${rpm_version}
tar xf "$srcdir/rpm-${rpm_version}.tar.bz2"
cd rpm-${rpm_version}
mkdir -p _build 
cd _build 
cmake -DCMAKE_INSTALL_PREFIX=/usr \
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
