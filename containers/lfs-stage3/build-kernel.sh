#!/bin/bash

set -e -x

lfs_version="12.0"
lfs_release="lfs12"
kernel_version="6.4.12"

distdir=/home/lfs/dist
basedir=/home/lfs/kernel

srcdir="$basedir/linux"
bootdir="$basedir/boot"
rootdir="$basedir/root"



if [ ! -d "$srcdir" ] ; then
    mkdir -p "$srcdir"
    tar xf rpmbuild/SOURCES/linux-*.tar.xz -C "$srcdir" --strip-components=1
fi

cd "$srcdir"
if [ ! -e .config ] ; then
    make mrproper
    make defconfig
fi

make

rm -rf "$rootdir"
mkdir -p "$rootdir"
make INSTALL_MOD_PATH=${rootdir}/usr modules_install

rm -rf "$bootdir"
mkdir -p "$bootdir"
cp -v arch/x86/boot/bzImage "$bootdir/vmlinuz-${kernel_version}.${lfs_release}.x86_64"
cp -v System.map "$bootdir/System.map-$kernel_version"
cp -v .config "$bootdir/config-6.4.12"

install -v -m755 -d "${rootdir}/etc/modprobe.d"
cat > "$rootdir/etc/modprobe.d/usb.conf" <<EOF
install ohci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i ohci_hcd ; true
install uhci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i uhci_hcd ; true
EOF

mkdir -p "$distdir"

cd "$bootdir/.."
tar zcf "$distdir/boot-lfs-${lfs_version}.tar.gz" "$(basename $bootdir)"

cd "$rootdir"
tar zcf "$distdir/modules-lfs-${lfs_version}.tar.gz" *

