# dnf

%global name            sqlite
%global version         3.50.4
%global file_version    3500400
%global year            2025
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A small, fast, self-contained, high-reliability, full-featured, SQL database engine
License:        Public Domain

Source0:        https://www.sqlite.org/%{year}/%{name}-autoconf-%{file_version}.tar.gz
Source1:        %{name}.sha256

Provides:       libsqlite3.so()(64bit)

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
SQLite is a C-language library that implements a small, fast, self-contained,
high-reliability, full-featured, SQL database engine. SQLite is the most used
database engine in the world. SQLite is built into all mobile phones and most
computers and comes bundled inside countless other applications that people
use every day.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n sqlite-autoconf-%{file_version}

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

%if %{with lfs}
rm %{buildroot}/usr/lib/libsqlite3.a

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/bin/sqlite3
/usr/lib/libsqlite3.so.*
/usr/lib/libsqlite3.so

%files devel
/usr/include/sqlite3*
/usr/lib/pkgconfig/sqlite3.pc

%files man
/usr/share/man/man*/*

%files static
/usr/lib/libsqlite3.a

%endif
