# lfs

%global name        tcl
%global version_2   8.6
%global version     %{version_2}.16
%global release     1

%global tdbc_version    1.1.10
%global itcl_version    4.3.2
%global sqlite_version  3.47.2
%global thread_version  2.8.11

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tool Command Language, pronounced tickle
License:        TCL

Source0:        https://downloads.sourceforge.net/%{name}/%{name}%{version}-src.tar.gz
Source1:        %{name}.sha256

BuildRequires:  pkg-config
Suggests:       %{name}-doc = %{version}

%description
The Tcl (Tool Command Language) provides a powerful platform for creating
integration applications that tie together diverse applications, protocols,
devices, and frameworks. When paired with the Tk toolkit, Tcl provides a
fastest and powerful way to create cross-platform GUI applications. Tcl can
also be used for a variety of web-related tasks and for creating powerful
command languages for applications.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{name}%{version}

#---------------------------------------------------------------------------
%build
SRCDIR=$(pwd)
cd unix
./configure --prefix=/usr           \
            --mandir=/usr/share/man \
            --disable-rpath
%make

sed -e "s|$SRCDIR/unix|/usr/lib|" \
    -e "s|$SRCDIR|/usr/include|"  \
    -i tclConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/tdbc%{tdbc_version}|/usr/lib/tdbc%{tdbc_version}|" \
    -e "s|$SRCDIR/pkgs/tdbc%{tdbc_version}/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/tdbc%{tdbc_version}/library|/usr/lib/tcl8.6|" \
    -e "s|$SRCDIR/pkgs/tdbc%{tdbc_version}|/usr/include|"            \
    -i pkgs/tdbc%{tdbc_version}/tdbcConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/itcl%{itcl_version}|/usr/lib/itcl%{itcl_version}|" \
    -e "s|$SRCDIR/pkgs/itcl%{itcl_version}/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/itcl%{itcl_version}|/usr/include|"            \
    -i pkgs/itcl%{itcl_version}/itclConfig.sh

unset SRCDIR

#---------------------------------------------------------------------------
%install
cd unix
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-private-headers
ln -sfv tclsh%{version2} %{buildroot}/usr/bin/tclsh
mv %{buildroot}/usr/share/man/man3/{Thread,Tcl_Thread}.3

find %{buildroot}/usr/lib -type f -name "*.so" -exec chmod 755 {} \;

%if %{with lfs}
%discard_docs
%discard_locales
%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/lib/{itcl,sqlite,tcl,tdbc,thread}*
/usr/lib/lib*.{a,so*}
/usr/lib/pkgconfig/*

%else
/usr/bin/sqlite3_analyzer
/usr/bin/tclsh
/usr/bin/tclsh%{version2}
/usr/include/*
/usr/lib/itcl%{itcl_version}/itcl.tcl
/usr/lib/itcl%{itcl_version}/itclConfig.sh
/usr/lib/itcl%{itcl_version}/itclHullCmds.tcl
/usr/lib/itcl%{itcl_version}/itclWidget.tcl
/usr/lib/itcl%{itcl_version}/libitclstub%{itcl_version}.a
/usr/lib/itcl%{itcl_version}/pkgIndex.tcl
%shlib /usr/lib/itcl%{itcl_version}/libitcl%{itcl_version}.so
%shlib /usr/lib/libtcl%{version2}.so
%shlib /usr/lib/tdbc%{tdbc_version}/libtdbc%{tdbc_version}.so
%shlib /usr/lib/tdbcmysql%{tdbc_version}/libtdbcmysql%{tdbc_version}.so
%shlib /usr/lib/tdbcodbc%{tdbc_version}/libtdbcodbc%{tdbc_version}.so
%shlib /usr/lib/tdbcpostgres%{tdbc_version}/libtdbcpostgres%{tdbc_version}.so
%shlib /usr/lib/thread%{thread_version}/libthread%{thread_version}.so
/usr/lib/libtclstub%{version2}.a
/usr/lib/pkgconfig/tcl.pc
/usr/lib/sqlite%{sqlite_version}/libsqlite%{sqlite_version}.so
/usr/lib/sqlite%{sqlite_version}/pkgIndex.tcl
/usr/lib/tcl%{version2}
/usr/lib/tcl8
/usr/lib/tclConfig.sh
/usr/lib/tclooConfig.sh
/usr/lib/tdbc%{tdbc_version}/libtdbcstub%{tdbc_version}.a
/usr/lib/tdbc%{tdbc_version}/pkgIndex.tcl
/usr/lib/tdbc%{tdbc_version}/tdbc.tcl
/usr/lib/tdbc%{tdbc_version}/tdbcConfig.sh
/usr/lib/tdbcmysql%{tdbc_version}/pkgIndex.tcl
/usr/lib/tdbcmysql%{tdbc_version}/tdbcmysql.tcl
/usr/lib/tdbcodbc%{tdbc_version}/pkgIndex.tcl
/usr/lib/tdbcodbc%{tdbc_version}/tdbcodbc.tcl
/usr/lib/tdbcpostgres%{tdbc_version}/pkgIndex.tcl
/usr/lib/tdbcpostgres%{tdbc_version}/tdbcpostgres.tcl
/usr/lib/thread%{thread_version}/pkgIndex.tcl
/usr/lib/thread%{thread_version}/ttrace.tcl

%files doc
/usr/share/man/man*/*

%endif
