# lfs

%global name            man-db
%global version         2.13.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tools for searching and reading man pages
License:        GPLv2+ and GPLv3+

Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  gdbm-devel
BuildRequires:  groff
BuildRequires:  libpipeline
BuildRequires:  pkgconf
BuildRequires:  systemd

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The man-db package includes five tools for browsing man-pages: man, whatis,
apropos, manpath and lexgrog. man formats and displays manual pages. whatis
searches the manual page names. apropos searches the manual page names and
descriptions. manpath determines search path for manual pages. lexgrog directly
reads header information in manual pages.

%if !%{with lfs}
%description doc
Documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr                         \
            --docdir=/usr/share/doc/%{name}-%{version} \
            --sysconfdir=/etc                     \
            --disable-setuid                      \
            --enable-cache-owner=bin              \
            --with-browser=/usr/bin/lynx          \
            --with-vgrind=/usr/bin/vgrind         \
            --with-grap=/usr/bin/grap
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
install -Dt %{buildroot}/usr/share/doc/%{name}-%{version} ABOUT-NLS COPYING ChangeLog* FAQ NEWS.md README.md

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/etc/*
/usr/bin/*
/usr/lib/%{name}/*.so*
/usr/lib/systemd/system/*
/usr/lib/tmpfiles.d/*
/usr/libexec/%{name}
/usr/sbin/*

%else
%config(noreplace) /etc/man_db.conf
/usr/bin/apropos
/usr/bin/catman
/usr/bin/lexgrog
/usr/bin/man
/usr/bin/man-recode
/usr/bin/mandb
/usr/bin/manpath
/usr/bin/whatis
/usr/lib/%{name}/libman.so*
/usr/lib/%{name}/libman-%{version}.so*
/usr/lib/%{name}/libmandb.so*
/usr/lib/%{name}/libmandb-%{version}.so*
/usr/lib/systemd/system/man-db.service
/usr/lib/systemd/system/man-db.timer
/usr/lib/tmpfiles.d/man-db.conf
/usr/libexec/%{name}/globbing
/usr/libexec/%{name}/manconv
/usr/libexec/%{name}/zsoelim
/usr/sbin/accessdb

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/it/man{1,5,8}/*.gz
/usr/share/man/man{1,5,8}/*.gz

%endif
