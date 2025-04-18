Name:           gdbm
Version:        1.24
Release:        1%{?dist}
Summary:        A GNU set of database routines which use extensible hashing
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
Gdbm is a GNU database indexing library, including routines which
use extensible hashing. Gdbm works in a similar way to standard UNIX dbm
routines. Gdbm is useful for developers who write C applications and need
access to a simple and efficient database or who are building C applications
which will use such a database.

If you're a C developer and your programs need access to simple database
routines, you should install gdbm. You'll also need to install gdbm-devel.

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
./configure --prefix=/usr    \
            --disable-static \
            --enable-libgdbm-compat
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/include/*.h
/usr/lib/libgdbm.so
/usr/lib/libgdbm.so.6
%shlib /usr/lib/libgdbm.so.6.0.0
/usr/lib/libgdbm_compat.so
/usr/lib/libgdbm_compat.so.4
%shlib /usr/lib/libgdbm_compat.so.4.0.0

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*
