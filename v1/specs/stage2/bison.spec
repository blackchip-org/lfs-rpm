%define version   3.8.2

Name:           bison
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU general-purpose parser generator
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz

%global _build_id_links none

%description
Bison is a general purpose parser generator that converts a grammar
description for an LALR(1) context-free grammar into a C program to
parse that grammar. Bison can be used to develop a wide range of
language parsers, from ones used in simple desk calculators to complex
programming languages. Bison is upwardly compatible with Yacc, so any
correctly written Yacc grammar should work with Bison without any
changes. If you know Yacc, you shouldn't have any trouble using
Bison. You do need to be very proficient in C programming to be able
to use Bison. Bison is only needed on systems that are used for
development.

If your system will be used for C development, you should install
Bison.


%prep
%setup -q


%build
./configure --prefix=/usr    \
            --docdir=/usr/share/doc/%{name}-%{version}
make


%check
make check


%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info/dir


%files
/usr/bin/bison
/usr/bin/yacc
/usr/lib/liby.a
/usr/share/aclocal/*
/usr/share/%{name}
/usr/share/doc/%{name}-%{version}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man1/*
   

%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4-1
- Initial package


