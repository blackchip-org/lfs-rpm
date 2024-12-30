Name:           libvterm
Version:        0.3.3
Release:        1%{?dist}
Summary:        An abstract library implementation of a VT220/xterm/ECMA-48 terminal emulator.
License:        MIT

Source:         https://www.leonerd.org.uk/code/libvterm/libvterm-%{version}.tar.gz

BuildRequires:  libtool

%description
An abstract C99 library which implements a VT220 or xterm-like terminal
emulator. It doesn't use any particular graphics toolkit or output system,
instead it invokes callback function pointers that its embedding program
should provide it to draw on its behalf. It avoids calling malloc() during
normal running state, allowing it to be used in embedded kernel situations.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
sed -i 's|/usr/local|/usr|g' Makefile
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/lib/*.a

#---------------------------------------------------------------------------
%files
/usr/bin/unterm
/usr/bin/vterm-ctrl
/usr/bin/vterm-dump
/usr/include/vterm.h
/usr/include/vterm_keycodes.h
/usr/lib/libvterm.so
/usr/lib/libvterm.so.0
%shlib /usr/lib/libvterm.so.0.0.0
/usr/lib/pkgconfig/vterm.pc
