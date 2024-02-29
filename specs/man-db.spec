Name:           man-db
Version:        2.12.0
Release:        1%{?dist}
Summary:        Tools for searching and reading man pages
License:        GPLv2+ and GPLv3+

Source0:        https://download.savannah.gnu.org/releases/man-db/man-db-%{version}.tar.xz

%description
The man-db package includes five tools for browsing man-pages: man, whatis,
apropos, manpath and lexgrog. man formats and displays manual pages. whatis
searches the manual page names. apropos searches the manual page names and
descriptions. manpath determines search path for manual pages. lexgrog directly
reads header information in manual pages.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr                         \
            --docdir=/usr/share/doc/man-db-%{version} \
            --sysconfdir=/etc                     \
            --disable-setuid                      \
            --enable-cache-owner=bin              \
            --with-browser=/usr/bin/lynx          \
            --with-vgrind=/usr/bin/vgrind         \
            --with-grap=/usr/bin/grap
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

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
/usr/lib/man-db/libmandb.so
/usr/lib/systemd/system/man-db.service
/usr/lib/systemd/system/man-db.timer
/usr/lib/tmpfiles.d/man-db.conf
/usr/libexec/man-db/globbing
/usr/libexec/man-db/manconv
/usr/libexec/man-db/zsoelim
/usr/sbin/accessdb
/usr/share/doc/man-db-%{version}
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/it/man{1,5,8}/*
/usr/share/man/man{1,5,8}/*

%defattr(755,root,root,755)
/usr/lib/man-db/libman-2.*.so
/usr/lib/man-db/libmandb-2.*.so
