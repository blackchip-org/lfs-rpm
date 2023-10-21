Name:           tcl
Version:        8.6.13
%global         version2 8.6
Release:        1%{?dist}
Summary:        Tool Command Language, pronounced tickle
License:        TCL

Source0:        https://downloads.sourceforge.net/tcl/tcl%{version}-src.tar.gz

%description
The Tcl (Tool Command Language) provides a powerful platform for creating
integration applications that tie together diverse applications, protocols,
devices, and frameworks. When paired with the Tk toolkit, Tcl provides a
fastest and powerful way to create cross-platform GUI applications. Tcl can
also be used for a variety of web-related tasks and for creating powerful
command languages for applications.

#---------------------------------------------------------------------------
%prep
%setup -q -n %{name}%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

SRCDIR=$(pwd)
cd unix
./configure --prefix=/usr           \
            --mandir=/usr/share/man
%make 

sed -e "s|$SRCDIR/unix|/usr/lib|" \
    -e "s|$SRCDIR|/usr/include|"  \
    -i tclConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/tdbc1.1.5|/usr/lib/tdbc1.1.5|" \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5/library|/usr/lib/tcl8.6|" \
    -e "s|$SRCDIR/pkgs/tdbc1.1.5|/usr/include|"            \
    -i pkgs/tdbc1.1.5/tdbcConfig.sh

sed -e "s|$SRCDIR/unix/pkgs/itcl4.2.3|/usr/lib/itcl4.2.3|" \
    -e "s|$SRCDIR/pkgs/itcl4.2.3/generic|/usr/include|"    \
    -e "s|$SRCDIR/pkgs/itcl4.2.3|/usr/include|"            \
    -i pkgs/itcl4.2.3/itclConfig.sh

unset SRCDIR
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd unix 
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install-private-headers
ln -sfv tclsh%{version2} %{buildroot}/usr/bin/tclsh
mv %{buildroot}/usr/share/man/man3/{Thread,Tcl_Thread}.3
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/sqlite3_analyzer
/usr/bin/tclsh
/usr/bin/tclsh%{version2}
/usr/include/*
/usr/lib/itcl4.2.3/itcl.tcl
/usr/lib/itcl4.2.3/itclConfig.sh
/usr/lib/itcl4.2.3/itclHullCmds.tcl
/usr/lib/itcl4.2.3/itclWidget.tcl
/usr/lib/itcl4.2.3/libitclstub4.2.3.a
/usr/lib/itcl4.2.3/pkgIndex.tcl
/usr/lib/libtclstub%{version2}.a
/usr/lib/pkgconfig/tcl.pc
/usr/lib/sqlite3.40.0/libsqlite3.40.0.so
/usr/lib/sqlite3.40.0/pkgIndex.tcl
/usr/lib/tcl%{version2}
/usr/lib/tcl8 
/usr/lib/tclConfig.sh
/usr/lib/tclooConfig.sh
/usr/lib/tdbc1.1.5/libtdbcstub1.1.5.a
/usr/lib/tdbc1.1.5/pkgIndex.tcl
/usr/lib/tdbc1.1.5/tdbc.tcl
/usr/lib/tdbc1.1.5/tdbcConfig.sh
/usr/lib/tdbcmysql1.1.5/pkgIndex.tcl
/usr/lib/tdbcmysql1.1.5/tdbcmysql.tcl
/usr/lib/tdbcodbc1.1.5/pkgIndex.tcl
/usr/lib/tdbcodbc1.1.5/tdbcodbc.tcl
/usr/lib/tdbcpostgres1.1.5/pkgIndex.tcl
/usr/lib/tdbcpostgres1.1.5/tdbcpostgres.tcl
/usr/lib/thread2.8.8/pkgIndex.tcl
/usr/lib/thread2.8.8/ttrace.tcl
/usr/share/man/man{1,3,n}/*

%defattr(755,root,root,755)
/usr/lib/itcl4.2.3/libitcl4.2.3.so
/usr/lib/libtcl%{version2}.so
/usr/lib/tdbc1.1.5/libtdbc1.1.5.so
/usr/lib/tdbcmysql1.1.5/libtdbcmysql1.1.5.so
/usr/lib/tdbcodbc1.1.5/libtdbcodbc1.1.5.so
/usr/lib/tdbcpostgres1.1.5/libtdbcpostgres1.1.5.so
/usr/lib/thread2.8.8/libthread2.8.8.so
