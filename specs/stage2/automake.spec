%global version         1.16.5
%global version2        1.16
%global _build_id_links none

Name:           automake
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU tool for automatically creating Makefiles
License:        GPLv2+ and GFDL and Public Domain and MIT

Source0:        https://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz

%description
Automake is a tool for automatically generating `Makefile.in' files compliant
with the GNU Coding Standards.

You should install Automake if you are developing software and would like to
use its ability to automatically generate GNU standard Makefiles.


%prep
%setup -q


%build
./configure --prefix=/usr --docdir=/usr/share/doc/automake-%{version}
make


%check
make check


%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info/dir
mv %{buildroot}/usr/share/aclocal/README %{buildroot}/usr/share/doc/automake-%{version}


%files
/usr/bin/aclocal
/usr/bin/aclocal-%{version2}
/usr/bin/automake
/usr/bin/automake-%{version2}
/usr/share/aclocal-%{version2}
/usr/share/automake-%{version2}
/usr/share/doc/automake-%{version}
/usr/share/info/*
/usr/share/man/man1/*

