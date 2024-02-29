Name:           kbd
Version:        2.6.4
Release:        1%{?dist}
Summary:        Tools for configuring the console (keyboard, virtual terminals, etc.)
License:        GPLv2+

Source0:        https://www.kernel.org/pub/linux/utils/kbd/kbd-%{version}.tar.xz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/kbd-%{version}-backspace-1.patch

%description
The kbd package contains tools for managing a Linux system's console's
behavior, including the keyboard, the screen fonts, the virtual terminals and
font files.

#---------------------------------------------------------------------------
%prep
%setup -q
%patch 0 -p 1

#---------------------------------------------------------------------------
%build
%lfs_build_begin

sed -i '/RESIZECONS_PROGS=/s/yes/no/' configure
sed -i 's/resizecons.8 //' docs/man/man8/Makefile.in
./configure --prefix=/usr --disable-vlock
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%files
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
/usr/share/locale/*/LC_MESSAGES/kbd.mo
/usr/share/man/man{1,5,8}/*
/usr/share/unimaps