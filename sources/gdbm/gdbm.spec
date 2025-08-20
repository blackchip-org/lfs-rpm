# lfs

%global name            gdbm
%global version         1.26
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU set of database routines which use extensible hashing
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
Gdbm is a GNU database indexing library, including routines which
use extensible hashing. Gdbm works in a similar way to standard UNIX dbm
routines. Gdbm is useful for developers who write C applications and need
access to a simple and efficient database or who are building C applications
which will use such a database.

If you're a C developer and your programs need access to simple database
routines, you should install gdbm. You'll also need to install gdbm-devel.

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs}
./configure --prefix=/usr    \
            --disable-static \
            --enable-libgdbm-compat

%else
./configure --prefix=/usr    \
            --enable-libgdbm-compat

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/lib/lib*.so*

%else
/usr/bin/gdbm_dump
/usr/bin/gdbm_load
/usr/bin/gdbmtool
/usr/lib/libgdbm.so.*
/usr/lib/libgdbm_compat.so.*

%files devel
/usr/include/*.h
/usr/lib/libgdbm.so
/usr/lib/libgdbm_compat.so

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libgdbm.a
/usr/lib/libgdbm_compat.a

%endif
