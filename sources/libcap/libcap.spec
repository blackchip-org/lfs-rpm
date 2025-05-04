# lfs

%global name            libcap
%global version         2.73
%global revision        1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{revision}%{?dist}
Summary:        Library for getting and setting POSIX.1e capabilities
License:        BSD or GPLv2

Source0:        https://www.kernel.org/pub/linux/libs/security/linux-privs/%{name}2/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
libcap is a library for getting and setting POSIX.1e (formerly POSIX 6) draft
15 capabilities.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%endif

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
/usr/include/sys/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*
/usr/sbin/*

%else
/usr/lib/libcap.so.*
/usr/lib/libpsx.so.*
/usr/sbin/capsh
/usr/sbin/getcap
/usr/sbin/getpcaps
/usr/sbin/setcap

%files devel
/usr/include/sys/*.h
/usr/lib/libcap.so
/usr/lib/libpsx.so
/usr/lib/pkgconfig/libcap.pc
/usr/lib/pkgconfig/libpsx.pc

%files man
/usr/share/man/man*/*.gz

%endif

