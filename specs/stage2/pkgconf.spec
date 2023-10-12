%global version     2.0.1

Name:           pkgconf
Version:        %{version}
Release:        1%{?dist}
Summary:        Package compiler and linker metadata toolkit
License:        ISC

Source0:        https://distfiles.ariadne.space/pkgconf/pkgconf-%{version}.tar.xz

%global _build_id_links none

%description
pkgconf is a program which helps to configure compiler and linker flags for
development frameworks. It is similar to pkg-config from freedesktop.org and
handles .pc files in a similar manner as pkg-config.


%prep
%setup -q


%build
./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}
make

mkdir -p         %{buildroot}/usr/bin
mkdir -p         %{buildroot}/usr/share/man/man1
ln -sv pkgconf   %{buildroot}/usr/bin/pkg-config
ln -sv pkgconf.1 %{buildroot}/usr/share/man/man1/pkg-config.1


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/bomtool
/usr/bin/pkgconf
/usr/include/pkgconf/libpkgconf
/usr/lib/libpkgconf.so
/usr/lib/libpkgconf.so.4
/usr/lib/pkgconfig/libpkgconf.pc
/usr/share/aclocal/*
/usr/share/doc/%{name}-%{version}
/usr/share/man/man{1,5,7}/*


%defattr(755,root,root,755)
/usr/lib/libpkgconf.so.4.0.0


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
