# lfs

%global name        libcap
%global version     2.73
%global revision    1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{revision}%{?dist}
Summary:        Library for getting and setting POSIX.1e capabilities
License:        BSD or GPLv2

Source0:        https://www.kernel.org/pub/linux/libs/security/linux-privs/%{name}2/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6) draft
15 capabilities.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
sed -i '/install -m.*STA/d' libcap/Makefile
make %{?_smp_mflags} prefix=/usr lib=lib

#---------------------------------------------------------------------------
%install
make prefix=%{buildroot}/usr lib=lib install

#---------------------------------------------------------------------------
%check
make test

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/sys
/usr/lib/lib*.so*
/usr/lib/pkgconfig
/usr/sbin

%else
/usr/include/sys/*.h
/usr/lib/libcap.so
/usr/lib/libcap.so.2
%shlib /usr/lib/libcap.so.%{version}
/usr/lib/libpsx.so
/usr/lib/libpsx.so.2
%shlib /usr/lib/libpsx.so.%{version}
/usr/lib/pkgconfig/libcap.pc
/usr/lib/pkgconfig/libpsx.pc
/usr/sbin/capsh
/usr/sbin/getcap
/usr/sbin/getpcaps
/usr/sbin/setcap

%files doc
/usr/share/man/man*/*

%endif

