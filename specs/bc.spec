Name:           bc
Version:        6.7.5
Release:        1%{?dist}
Summary:        GNU's bc (a numeric processing language) and dc (a calculator)
License:        GPLv2+

Source0:        https://github.com/gavinhoward/bc/releases/download/%{version}/bc-%{version}.tar.xz

%description
The bc package includes bc and dc. Bc is an arbitrary precision numeric
processing arithmetic language. Dc is an interactive arbitrary precision stack
based calculator, which can be used as a text mode calculator.

Install the bc package if you need its number handling capabilities or if you
would like to use its text mode calculator.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

CC=gcc ./configure --prefix=/usr -G -O3 -r
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_build_begin

%make DESTDIR=%{buildroot} install
%lfs_build_end

#---------------------------------------------------------------------------
%files
/usr/bin/bc
/usr/bin/dc
/usr/share/locale/*/bc
/usr/share/man/man1/*
