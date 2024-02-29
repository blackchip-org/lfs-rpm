Name:           kmod
Version:        31
Release:        1%{?dist}
Summary:        Linux kernel module management utilities
License:        GPLv2+

Source0:        https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%{version}.tar.xz

%description
The kmod package provides various programs needed for automatic loading and
unloading of modules under 2.6, 3.x, and later kernels, as well as other module
management programs. Device drivers and filesystems are two examples of loaded
and unloaded modules.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr          \
            --sysconfdir=/etc      \
            --with-openssl         \
            --with-xz              \
            --with-zstd            \
            --with-zlib
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/{,s}bin
for target in depmod insmod modinfo modprobe rmmod; do
  ln -sfv ../bin/kmod %{buildroot}/usr/sbin/$target
done

ln -sfv kmod %{buildroot}/usr/bin/lsmod
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/kmod
/usr/bin/lsmod
/usr/include/*.h
/usr/lib/libkmod.so
/usr/lib/libkmod.so.2
/usr/lib/pkgconfig/libkmod.pc
/usr/sbin/depmod
/usr/sbin/insmod
/usr/sbin/modinfo
/usr/sbin/modprobe
/usr/sbin/rmmod
/usr/share/bash-completion/completions/kmod
/usr/share/man/man{5,8}/*

%defattr(755,root,root,755)
/usr/lib/libkmod.so.2.*
