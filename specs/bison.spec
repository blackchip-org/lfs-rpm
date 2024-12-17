Name:           bison
Version:        3.8.2
Release:        1%{?dist}
Summary:        A GNU general-purpose parser generator
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz


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

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr \
            --docdir=/usr/share/doc/bison-3.8.2
%make

%else
./configure --prefix=/usr \
            --docdir=/usr/share/doc/bison-3.8.2
%make

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install

%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
/usr/bin/bison
/usr/bin/yacc
/usr/lib/liby.a
/usr/share/aclocal/*
/usr/share/%{name}
/usr/share/locale/*/LC_MESSAGES/*.mo

%if %{without lfs_stage1}
/usr/share/doc/%{name}-%{version}
/usr/share/info/*
/usr/share/man/man1/*
%endif



