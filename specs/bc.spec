Name:           bc
Version:        7.0.3
Release:        1%{?dist}
Summary:        GNU's bc (a numeric processing language) and dc (a calculator)
License:        GPLv2+

Source:         https://github.com/gavinhoward/bc/releases/download/%{version}/bc-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

%description
The bc package includes bc and dc. Bc is an arbitrary precision numeric
processing arithmetic language. Dc is an interactive arbitrary precision stack
based calculator, which can be used as a text mode calculator.

Install the bc package if you need its number handling capabilities or if you
would like to use its text mode calculator.

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
%setup -q

#---------------------------------------------------------------------------
%build
CC=gcc ./configure --prefix=/usr -G -O3 -r
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/bin/bc
/usr/bin/dc

%files lang
/usr/share/locale/*/bc

%files doc
/usr/share/man/man*/*
