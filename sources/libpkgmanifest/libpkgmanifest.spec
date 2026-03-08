# dnf

%global name            libpkgmanifest
%global version         0.5.9
%global release         1

# https://github.com/rpm-software-management/libpkgmanifest

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Library for working with RPM manifests
License:        GPLv2+

Source0:        https://github.com/rpm-software-management/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  python-devel
BuildRequires:  yaml-cpp

%if !%{with lfs}
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package python
Summary:        Python files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%endif

%description
This library provides functionality for parsing and serializing RPM package
manifest files.

It is primarily designed for use by package managers like DNF, which populate
information into manifest files. However, it can also be used directly to
interact with manifest objects in custom applications.

The primary purpose of this library is to streamline internal workflows for
building container images, while also providing foundational building blocks
to tackle general build system management challenges highlighted in this
upstream ticket.

Written in C++ with TDD, the library offers a simple, ABI-compatible API layer
for users. Python bindings are also available, automatically generated from
the C++ API.

%if !%{with lfs}
%description devel
Development files for %{name}

%description python
Python files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DWITH_TESTS=OFF \
    ..

make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/%{name}
/usr/lib/%{name}.so*
/usr/lib/pkgconfig/%{name}.pc
/usr/lib/python%{python_version}/site-packages/%{name}
/usr/lib/python%{python_version}/site-packages/%{name}-*.dist-info

%else
/usr/lib/lib%{name}.so.*

%files devel
/usr/include/%{name}
/usr/lib/%{name}.so
/usr/lib/pkgconfig/%{name}.pc

%files python
/usr/lib/python%{python_version}/site-packages/%{name}
/usr/lib/python%{python_version}/site-packages/%{name}-*.dist-info

%endif


