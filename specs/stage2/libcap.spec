%global version     2.69

Name:           libcap
Version:        %{version}
Release:        1%{?dist}
Summary:        Library for getting and setting POSIX.1e capabilities
License:        BSD or GPLv2

Source0:        https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.xz

%global _build_id_links none

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6) draft
15 capabilities.


%prep
%setup -q


%build
sed -i '/install -m.*STA/d' libcap/Makefile
make prefix=/usr lib=lib


%check
make test


%install
make prefix=%{buildroot}/usr lib=lib install


%files
/usr/include/sys/*.h
/usr/lib/libcap.so
/usr/lib/libcap.so.2
/usr/lib/libpsx.so
/usr/lib/libpsx.so.2
/usr/lib/pkgconfig/libcap.pc
/usr/lib/pkgconfig/libpsx.pc
/usr/sbin/capsh
/usr/sbin/getcap
/usr/sbin/getpcaps
/usr/sbin/setcap
/usr/share/man/man{1,3,8}/*


%defattr(755,root,root,755)
/usr/lib/libcap.so.%{version}
/usr/lib/libpsx.so.%{version}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
