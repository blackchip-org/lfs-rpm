# lfs

%global name        kbd
%global version     2.7.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tools for configuring the console (keyboard, virtual terminals, etc.)
License:        GPLv2+

Source0:        https://www.kernel.org/pub/linux/utils/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/kbd-%{version}-backspace-1.patch

BuildRequires:  autoconf
BuildRequires:  pkg-config
Suggests:       %{name}-doc = %{version}

%description
The kbd package contains tools for managing a Linux system's console's
behavior, including the keyboard, the screen fonts, the virtual terminals and
font files.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q
%patch 0 -p 1

#---------------------------------------------------------------------------
%build
sed -i '/RESIZECONS_PROGS=/s/yes/no/' configure
sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in
./configure --prefix=/usr --disable-vlock
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/share/console{fonts,trans}
/usr/share/{keymaps,unimaps}

%else
/usr/bin/chvt
/usr/bin/deallocvt
/usr/bin/dumpkeys
/usr/bin/fgconsole
/usr/bin/getkeycodes
/usr/bin/kbd_mode
/usr/bin/kbdinfo
/usr/bin/kbdrate
/usr/bin/loadkeys
/usr/bin/loadunimap
/usr/bin/mapscrn
/usr/bin/openvt
/usr/bin/psfaddtable
/usr/bin/psfgettable
/usr/bin/psfstriptable
/usr/bin/psfxtable
/usr/bin/setfont
/usr/bin/setkeycodes
/usr/bin/setleds
/usr/bin/setmetamode
/usr/bin/setvtrgb
/usr/bin/showconsolefont
/usr/bin/showkey
/usr/bin/unicode_start
/usr/bin/unicode_stop
/usr/share/console{fonts,trans}
/usr/share/keymaps
/usr/share/unimaps

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/man/man*/*

%endif
