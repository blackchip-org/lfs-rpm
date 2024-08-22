Name:           libcap
Version:        2.70
Release:        1%{?dist}
Summary:        Library for getting and setting POSIX.1e capabilities
License:        BSD or GPLv2

Source0:        https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.xz

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6) draft
15 capabilities.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

sed -i '/install -m.*STA/d' libcap/Makefile
%make prefix=/usr lib=lib
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make prefix=%{buildroot}/usr lib=lib install
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
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
/usr/share/man/man{1,3,5,8}/*

%defattr(755,root,root,755)
/usr/lib/libcap.so.%{version}
/usr/lib/libpsx.so.%{version}
