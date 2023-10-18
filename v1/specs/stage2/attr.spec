%global version     2.5.1

Name:           attr
Version:        %{version}
Release:        1%{?dist}
Summary:        Utilities for managing filesystem extended attributes
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz

%global _build_id_links none

%description
A set of tools for manipulating extended attributes on filesystem objects, in
particular getfattr(1) and setfattr(1). An attr(1) command is also provided
which is largely compatible with the SGI IRIX tool of the same name.


%prep
%setup -q


%build
./configure --prefix=/usr     \
            --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-%{version}
make


%check
make check


%install
make DESTDIR=%{buildroot} install


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
/usr/lib/libattr.so.1.1.2501


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
