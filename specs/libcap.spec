Name:           libcap
Version:        2.70
Release:        1%{?dist}
Summary:        Library for getting and setting POSIX.1e capabilities
License:        BSD or GPLv2

Source:         https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.xz

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
%setup -q

#---------------------------------------------------------------------------
%build
sed -i '/install -m.*STA/d' libcap/Makefile
%make prefix=/usr lib=lib

#---------------------------------------------------------------------------
%install
%make prefix=%{buildroot}/usr lib=lib install

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
%files
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

