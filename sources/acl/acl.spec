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

Suggests:       %{name}-doc = %{version}

%description
This package contains the getfacl and setfacl utilities needed for manipulating
access control lists.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

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
/usr/include/acl/*.h
/usr/include/sys/*.h
/usr/lib/libacl.so
/usr/lib/libacl.so.1
%shlib /usr/lib/libacl.so.1.1.*
/usr/lib/pkgconfig/libacl.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*

%endif
