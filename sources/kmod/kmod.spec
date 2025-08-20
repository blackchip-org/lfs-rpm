# lfs

%global name            kmod
%global version         34.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Linux kernel module management utilities
License:        GPLv2+

Source0:        https://www.kernel.org/pub/linux/utils/kernel/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconf

%if !%{with lfs}
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%endif

%description
The kmod package provides various programs needed for automatic loading and
unloading of modules under 2.6, 3.x, and later kernels, as well as other module
management programs. Device drivers and filesystems are two examples of loaded
and unloaded modules.

%if !%{with lfs}
%description devel
Development files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
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
%if %{with lfs}
/usr/bin/*
/usr/include/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*
/usr/sbin/*
/usr/share/bash-completion/completions/*
/usr/share/fish/vendor_functions.d/*
/usr/share/pkgconfig/*
/usr/share/zsh/site-functions/*

%else
/usr/bin/kmod
/usr/lib/libkmod.so*
/usr/lib/pkgconfig/libkmod.pc
/usr/sbin/depmod
/usr/sbin/insmod
/usr/sbin/lsmod
/usr/sbin/modinfo
/usr/sbin/modprobe
/usr/sbin/rmmod
/usr/share/bash-completion/completions/{insmod,kmod,lsmod,rmmod}
/usr/share/fish/vendor_functions.d/{insmod,lsmod,rmmod}.fish
/usr/share/zsh/site-functions/_{insmod,lsmod,rmmod}

%files devel
/usr/include/*.h
/usr/share/pkgconfig/%{name}.pc

%endif

