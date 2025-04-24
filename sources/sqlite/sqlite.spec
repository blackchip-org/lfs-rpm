# dnf
# Python test fails with 3.49

%global name            sqlite
%global version         3.48.0
%global file_version    3480000
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

Suggests:       %{name}-doc = %{version}

%description
SQLite is a C-language library that implements a small, fast, self-contained,
high-reliability, full-featured, SQL database engine. SQLite is the most used
database engine in the world. SQLite is built into all mobile phones and most
computers and comes bundled inside countless other applications that people
use every day.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

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

# Remove static libraries
rm %{buildroot}/usr/lib/libsqlite3.a

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/bin/sqlite3
/usr/include/sqlite3*
/usr/lib/libsqlite3.so
/usr/lib/libsqlite3.so.0
%shlib /usr/lib/libsqlite3.so.0.8.6
/usr/lib/pkgconfig/sqlite3.pc

%files doc
/usr/share/man/man*/*

%endif
