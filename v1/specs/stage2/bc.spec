%global version     6.6.0

Name:           bc
Version:        %{version}
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


%global _build_id_links none


%prep
%setup -q


%build
CC=gcc ./configure --prefix=/usr -G -O3 -r
make 


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/bc 
/usr/bin/dc 
/usr/share/locale/*/bc 
/usr/share/man/man1/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
