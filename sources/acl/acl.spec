# lfs

%global name            acl
%global version         2.3.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Access control list utilities
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
This package contains the getfacl and setfacl utilities needed for manipulating
access control lists.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/acl-%{version}
make %{?%_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/{acl,sys}
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/bin/chacl
/usr/bin/getfacl
/usr/bin/setfacl
/usr/lib/libacl.so.*

%files devel
/usr/include/%{name}
/usr/include/sys/*.h
/usr/lib/libacl.so
/usr/lib/pkgconfig/libacl.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*.gz

%endif
