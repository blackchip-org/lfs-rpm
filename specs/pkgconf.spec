Name:           pkgconf
Version:        2.3.0
Release:        1%{?dist}
Summary:        Package compiler and linker metadata toolkit
License:        ISC

Source0:        https://distfiles.ariadne.space/pkgconf/pkgconf-%{version}.tar.xz

%description
pkgconf is a program which helps to configure compiler and linker flags for
development frameworks. It is similar to pkg-config from freedesktop.org and
handles .pc files in a similar manner as pkg-config.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}
%make

mkdir -p         %{buildroot}/usr/bin
mkdir -p         %{buildroot}/usr/share/man/man1
ln -sv pkgconf   %{buildroot}/usr/bin/pkg-config
ln -sv pkgconf.1 %{buildroot}/usr/share/man/man1/pkg-config.1
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/bomtool
/usr/bin/pkgconf
/usr/include/pkgconf/libpkgconf
/usr/lib/libpkgconf.so
/usr/lib/libpkgconf.so.5
/usr/lib/pkgconfig/libpkgconf.pc
/usr/share/aclocal/*
/usr/share/doc/%{name}-%{version}
/usr/share/man/man{1,5,7}/*

%defattr(755,root,root,755)
/usr/lib/libpkgconf.so.5.0.0