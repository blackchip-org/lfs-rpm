# lfs

%global name        libtool
%global version     2.5.4
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU Portable Library Tool
License:        GPLv2+ and LGPLv2+ and GFDL

Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf and
GNU Automake).

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
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
rm -fv %{buildroot}/usr/lib/libltdl.a

#---------------------------------------------------------------------------
%check
make -k check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/share/{aclocal,libtool}

%else
/usr/bin/libtool
/usr/bin/libtoolize
/usr/include/libltdl
/usr/include/*.h
/usr/lib/libltdl.so
/usr/lib/libltdl.so.7
%shlib /usr/lib/libltdl.so.7.3.3
/usr/share/aclocal/*
/usr/share/libtool

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
