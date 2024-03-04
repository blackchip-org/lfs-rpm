Name:           acl
Version:        2.3.2
Release:        1%{?dist}
Summary:        Access control list utilities
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/acl/acl-%{version}.tar.xz

%description
This package contains the getfacl and setfacl utilities needed for manipulating
access control lists.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/acl-%{version}
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/chacl
/usr/bin/getfacl
/usr/bin/setfacl
/usr/include/acl/*.h
/usr/include/sys/*.h
/usr/lib/libacl.so
/usr/lib/libacl.so.1
/usr/lib/pkgconfig/libacl.pc
/usr/share/doc/acl-%{version}
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man{1,3,5}/*

%defattr(755,root,root,755)
/usr/lib/libacl.so.1.1.*
