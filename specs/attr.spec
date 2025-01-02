Name:           attr
Version:        2.5.2
Release:        1%{?dist}
Summary:        Utilities for managing filesystem extended attributes
License:        GPLv2+

Source0:        https://download.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
A set of tools for manipulating extended attributes on filesystem objects, in
particular getfattr(1) and setfattr(1). An attr(1) command is also provided
which is largely compatible with the SGI IRIX tool of the same name.

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
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr     \
            --disable-static  \
            --sysconfdir=/etc \
            --docdir=/usr/share/doc/attr-%{version}
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%config(noreplace) /etc/xattr.conf
/usr/bin/attr
/usr/bin/getfattr
/usr/bin/setfattr
/usr/include/attr
/usr/lib/libattr.so
/usr/lib/libattr.so.1
%shlib /usr/lib/libattr.so.1.*
/usr/lib/pkgconfig/libattr.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*
