Name:           man-db
Version:        2.12.0
Release:        1%{?dist}
Summary:        Tools for searching and reading man pages
License:        GPLv2+ and GPLv3+

Source:         https://download.savannah.gnu.org/releases/man-db/man-db-%{version}.tar.xz

BuildRequires:  gdbm
BuildRequires:  groff
BuildRequires:  libpipeline
BuildRequires:  pkg-config
BuildRequires:  systemd
Suggests:       %{name}-doc = %{version}

%description
The man-db package includes five tools for browsing man-pages: man, whatis,
apropos, manpath and lexgrog. man formats and displays manual pages. whatis
searches the manual page names. apropos searches the manual page names and
descriptions. manpath determines search path for manual pages. lexgrog directly
reads header information in manual pages.

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
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr                         \
            --docdir=/usr/share/doc/man-db-%{version} \
            --sysconfdir=/etc                     \
            --disable-setuid                      \
            --enable-cache-owner=bin              \
            --with-browser=/usr/bin/lynx          \
            --with-vgrind=/usr/bin/vgrind         \
            --with-grap=/usr/bin/grap
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%config(noreplace) /etc/man_db.conf
/usr/bin/apropos
/usr/bin/catman
/usr/bin/lexgrog
/usr/bin/man
/usr/bin/man-recode
/usr/bin/mandb
/usr/bin/manpath
/usr/bin/whatis
/usr/lib/man-db/libman.so
%shlib /usr/lib/man-db/libman-2.12.0.so
/usr/lib/man-db/libmandb.so
%shlib /usr/lib/man-db/libmandb-2.12.0.so
/usr/lib/systemd/system/man-db.service
/usr/lib/systemd/system/man-db.timer
/usr/lib/tmpfiles.d/man-db.conf
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim
/usr/sbin/accessdb

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/man-db-%{version}

%files man
/usr/share/man/it/man{1,5,8}/*
/usr/share/man/man{1,5,8}/*