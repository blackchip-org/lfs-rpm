# lfs

%global name            attr
%global version         2.5.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utilities for managing filesystem extended attributes
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
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

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
A set of tools for manipulating extended attributes on filesystem objects, in
particular getfattr(1) and setfattr(1). An attr(1) command is also provided
which is largely compatible with the SGI IRIX tool of the same name.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs}
./configure --prefix=/usr     \
            --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-%{version}

%else
./configure --prefix=/usr     \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-%{version}

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/etc/*
/usr/bin/*
/usr/include/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
%config(noreplace) /etc/xattr.conf
/usr/bin/attr
/usr/bin/getfattr
/usr/bin/setfattr
/usr/lib/libattr.so.*

%files devel
/usr/include/%{name}
/usr/lib/libattr.so
/usr/lib/pkgconfig/libattr.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libattr.a

%endif
