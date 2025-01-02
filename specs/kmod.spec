Name:           kmod
Version:        31
Release:        1%{?dist}
Summary:        Linux kernel module management utilities
License:        GPLv2+

Source:         https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%{version}.tar.xz

BuildRequires:  pkg-config
Suggests:       %{name}-doc = %{version}

%description
The kmod package provides various programs needed for automatic loading and
unloading of modules under 2.6, 3.x, and later kernels, as well as other module
management programs. Device drivers and filesystems are two examples of loaded
and unloaded modules.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr          \
            --sysconfdir=/etc      \
            --with-openssl         \
            --with-xz              \
            --with-zstd            \
            --with-zlib
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/{,s}bin
for target in depmod insmod modinfo modprobe rmmod; do
  ln -sfv ../bin/kmod %{buildroot}/usr/sbin/$target
done

ln -sfv kmod %{buildroot}/usr/bin/lsmod

#---------------------------------------------------------------------------
%files
/usr/bin/kmod
/usr/bin/lsmod
/usr/include/*.h
/usr/lib/libkmod.so
/usr/lib/libkmod.so.2
%shlib /usr/lib/libkmod.so.2.4.1
/usr/lib/pkgconfig/libkmod.pc
/usr/sbin/depmod
/usr/sbin/insmod
/usr/sbin/modinfo
/usr/sbin/modprobe
/usr/sbin/rmmod
/usr/share/bash-completion/completions/kmod

%files doc
/usr/share/man/man*/*
