# dnf

%global name            librepo
%global version         1.19.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Library for downloading linux repository metadata and packages
License:        LGPL-2.1

Source0:        https://github.com/rpm-software-management/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

Provides:       %{name}-devel

BuildRequires:  attr-devel
BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  glib-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconf
BuildRequires:  python-devel
BuildRequires:  zchunk-devel

%description
A library providing C and Python (libcURL like) API for downloading linux
repository metadata and packages.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DUSE_GPGME=OFF \
    -DENABLE_DOCS=OFF \
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
/usr/lib/lib*.so*
/usr/lib/pkgconfig
/usr/lib/python%{python_version}

%else
/usr/include/%{name}
/usr/lib/librepo.so
%shlib /usr/lib/librepo.so.0
/usr/lib/pkgconfig/librepo.pc
/usr/lib/python%{python_version}/site-packages/%{name}

%endif
