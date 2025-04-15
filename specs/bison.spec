# lfs

%global name        bison
%global version     3.8.2
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU general-purpose parser generator
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

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

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr \
            --docdir=/usr/share/doc/bison-3.8.2
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

%if %{with lfs}
%discard_docs
%discard_locales
rm -rf %{buildroot}/usr/share/aclocal
%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir


#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/lib/*
/usr/share/%{name}

%else
/usr/bin/bison
/usr/bin/yacc
/usr/lib/liby.a
/usr/share/aclocal/*
/usr/share/%{name}

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif


