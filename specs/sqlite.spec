Name:           sqlite
Version:        3.47.2
%global         file_version 3470200
Release:        1%{?dist}
Summary:        A small, fast, self-contained, high-reliability, full-featured, SQL database engine
License:        Public Domain

Source:         https://www.sqlite.org/2024/sqlite-autoconf-%{file_version}.tar.gz

Suggests:       %{name}-man = %{version}

%package man
Summary:        Manual pages for %{name}

%description
SQLite is a C-language library that implements a small, fast, self-contained,
high-reliability, full-featured, SQL database engine. SQLite is the most used
database engine in the world. SQLite is built into all mobile phones and most
computers and comes bundled inside countless other applications that people
use every day.

%description man
Manual pages for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n sqlite-autoconf-%{file_version}

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

# Remove static libraries
rm %{buildroot}/usr/lib/libsqlite3.a

#---------------------------------------------------------------------------
%files
/usr/bin/sqlite3
/usr/include/sqlite3*
/usr/lib/libsqlite3.so
/usr/lib/libsqlite3.so.0
/usr/lib/pkgconfig/sqlite3.pc

%defattr(755,root,root,755)
/usr/lib/libsqlite3.so.0.8.6

%files man
/usr/share/man/man1/*.gz