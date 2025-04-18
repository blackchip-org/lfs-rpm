Name:           kmod
Version:        34
Release:        1%{?dist}
Summary:        Linux kernel module management utilities
License:        GPLv2+

Source:         https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkg-config
Suggests:       %{name}-doc = %{version}

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
mkdir -p build
cd build

# man pages requires scdoc

meson setup --prefix=/usr           \
            --sbindir=/usr/sbin     \
            --buildtype=release     \
            -D manpages=false
ninja

#---------------------------------------------------------------------------
%install
cd build
DESTDIR=%{buildroot} ninja install

#---------------------------------------------------------------------------
%files
/usr/bin/kmod
/usr/include/*.h
/usr/lib/libkmod.so
/usr/lib/libkmod.so.2
%shlib /usr/lib/libkmod.so.2.5.1
/usr/lib/pkgconfig/libkmod.pc
/usr/sbin/depmod
/usr/sbin/insmod
/usr/sbin/lsmod
/usr/sbin/modinfo
/usr/sbin/modprobe
/usr/sbin/rmmod
/usr/share/bash-completion/completions/{insmod,kmod,lsmod,rmmod}
/usr/share/fish/vendor_functions.d/{insmod,lsmod,rmmod}.fish
/usr/share/pkgconfig/kmod.pc
/usr/share/zsh/site-functions/_{insmod,lsmod,rmmod}

