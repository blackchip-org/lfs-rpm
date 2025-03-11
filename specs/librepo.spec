# extra

Name:           librepo
Version:        1.19.0
Release:        1%{?dist}
Summary:        Library for downloading linux repository metadata and packages
License:        LGPL-2.1

Source:         https://github.com/rpm-software-management/librepo/archive/refs/tags/%{version}.tar.gz

BuildRequires:  attr
BuildRequires:  check
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  glib
BuildRequires:  libxml2
BuildRequires:  openssl
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  zchunk

%description
A library providing C and Python (libcURL like) API for downloading linux
repository metadata and packages.

#---------------------------------------------------------------------------
%prep
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
%make

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/include/%{name}
/usr/lib/librepo.so
%shlib /usr/lib/librepo.so.0
/usr/lib/pkgconfig/librepo.pc
/usr/lib/python%{python_version}/site-packages/%{name}
