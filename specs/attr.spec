Name:           attr
Version:        2.5.2
Release:        1%{?dist}
Summary:        Utilities for managing filesystem extended attributes
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz

%description
A set of tools for manipulating extended attributes on filesystem objects, in
particular getfattr(1) and setfattr(1). An attr(1) command is also provided
which is largely compatible with the SGI IRIX tool of the same name.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr     \
            --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-%{version}
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
%config(noreplace) /etc/xattr.conf
/usr/bin/attr
/usr/bin/getfattr
/usr/bin/setfattr
/usr/include/attr
/usr/lib/libattr.so
/usr/lib/libattr.so.1
/usr/lib/pkgconfig/libattr.pc
/usr/share/doc/attr-%{version}
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man{1,3}/*

%defattr(755,root,root,755)
/usr/lib/libattr.so.1.*