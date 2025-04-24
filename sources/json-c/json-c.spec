# dnf

%global name            json-c
%global version         0.18
%global release         1
%global date            20240915

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        JSON implementation in C
License:        MIT

Source0:        https://github.com/json-c/json-c/archive/refs/tags/json-c-%{version}-%{date}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  cmake

%description
JSON-C implements a reference counting object model that allows you to easily
construct JSON objects in C, output them as JSON formatted strings and parse
JSON formatted strings back into the C representation of JSON objects. It aims
to conform to RFC 8259.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{name}-%{name}-%{version}-%{date}

#---------------------------------------------------------------------------
%build
mkdir   json-c-build
cd      json-c-build
cmake   -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=/usr/lib \
        ..
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd json-c-build
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/libjson-c.a

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/json-c
/usr/lib/cmake/json-c
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/include/json-c
/usr/lib/cmake/json-c
/usr/lib/libjson-c.so
/usr/lib/libjson-c.so.5
%shlib /usr/lib/libjson-c.so.5.4.0
/usr/lib/pkgconfig/json-c.pc

%endif

