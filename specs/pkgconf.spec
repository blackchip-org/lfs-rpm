Name:           pkgconf
Version:        2.3.0
Release:        1%{?dist}
Summary:        Package compiler and linker metadata toolkit
License:        ISC

Source:         https://distfiles.ariadne.space/pkgconf/pkgconf-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

%description
pkgconf is a program which helps to configure compiler and linker flags for
development frameworks. It is similar to pkg-config from freedesktop.org and
handles .pc files in a similar manner as pkg-config.

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}
%make

mkdir -p         %{buildroot}/usr/bin
mkdir -p         %{buildroot}/usr/share/man/man1
ln -sv pkgconf   %{buildroot}/usr/bin/pkg-config
ln -sv pkgconf.1 %{buildroot}/usr/share/man/man1/pkg-config.1

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/bin/bomtool
/usr/bin/pkgconf
/usr/include/pkgconf/libpkgconf
/usr/lib/libpkgconf.so
/usr/lib/libpkgconf.so.5
%shlib /usr/lib/libpkgconf.so.5.0.0
/usr/lib/pkgconfig/libpkgconf.pc
/usr/share/aclocal/*

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*
