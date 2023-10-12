%global version     2.3.1

Name:           acl
Version:        %{version}
Release:        1%{?dist}
Summary:        Access control list utilities
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/acl/acl-%{version}.tar.xz

%global _build_id_links none

%description
This package contains the getfacl and setfacl utilities needed for manipulating
access control lists.


%prep
%setup -q


%build
./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/acl-%{version}
make


%install
make DESTDIR=%{buildroot} install


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
/usr/lib/libacl.so.1.1.2301


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
