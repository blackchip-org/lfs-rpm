Name:           json-c
Version:        0.18
Release:        1%{?dist}
Summary:        JSON implementation in C
License:        MIT

%global date    20240915

Source0:        https://github.com/json-c/json-c/archive/refs/tags/json-c-%{version}-%{date}.tar.gz

%description
JSON-C implements a reference counting object model that allows you to easily
construct JSON objects in C, output them as JSON formatted strings and parse
JSON formatted strings back into the C representation of JSON objects. It aims
to conform to RFC 8259.

#---------------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{name}-%{version}-%{date}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir   json-c-build
cd      json-c-build
cmake   -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=/usr/lib \
        ..

%lfs_build_begin

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd json-c-build
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/libjson-c.a

%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/include/json-c
/usr/lib/cmake/json-c
/usr/lib/libjson-c.so
/usr/lib/libjson-c.so.5
/usr/lib/pkgconfig/json-c.pc

%defattr(755,root,root,755)
/usr/lib/libjson-c.so.5.4.0

