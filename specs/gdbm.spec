Name:           gdbm
Version:        1.24
Release:        1%{?dist}
Summary:        A GNU set of database routines which use extensible hashing
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

%description
Gdbm is a GNU database indexing library, including routines which
use extensible hashing. Gdbm works in a similar way to standard UNIX dbm
routines. Gdbm is useful for developers who write C applications and need
access to a simple and efficient database or who are building C applications
which will use such a database.

If you're a C developer and your programs need access to simple database
routines, you should install gdbm. You'll also need to install gdbm-devel.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr    \
            --disable-static \
            --enable-libgdbm-compat
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
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/include/*.h
/usr/lib/libgdbm.so
/usr/lib/libgdbm.so.6
/usr/lib/libgdbm_compat.so
/usr/lib/libgdbm_compat.so.4
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man{1,3}/*

%defattr(755,root,root,755)
/usr/lib/libgdbm.so.6.0.0
/usr/lib/libgdbm_compat.so.4.0.0
