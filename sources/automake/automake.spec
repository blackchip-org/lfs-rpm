# lfs

%global name        automake
%global version_2   1.16
%global version     %{version_2}.5
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU tool for automatically creating Makefiles
License:        GPLv2+ and GFDL and Public Domain and MIT

Source0:        https://ftp.gnu.org/gnu/automake/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  autoconf >= 2.65
Suggests:       %{name}-doc = %{version}

%description
Automake is a tool for automatically generating `Makefile.in' files compliant
with the GNU Coding Standards.

You should install Automake if you are developing software and would like to
use its ability to automatically generate GNU standard Makefiles.

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr --docdir=/usr/share/doc/automake-%{version}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
mv %{buildroot}/usr/share/aclocal/README %{buildroot}/usr/share/doc/automake-%{version}

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/share/aclocal-%{version_2}
/usr/share/automake-%{version_2}

%else
/usr/bin/aclocal
/usr/bin/aclocal-%{version2}
/usr/bin/automake
/usr/bin/automake-%{version2}
/usr/share/aclocal-%{version2}
/usr/share/automake-%{version2}

%files doc
/usr/share/doc/automake-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
