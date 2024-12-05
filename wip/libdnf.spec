Name:       libdnf
Version:    0.73.4
Release:    1%{?dist}
Summary:    High level package manager
License:    GPLv2

Source0:    https://github.com/rpm-software-management/libdnf/archive/refs/tags/%{version}.tar.gz

%description
This library provides a high level package-manager. It's core library of dnf,
PackageKit and rpm-ostree. It's replacement for deprecated hawkey library which
it contains inside and uses librepo under the hood.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DPYTHON_DESIRED="3" \
    ..
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd build
make DESTDIR=%{buildroot} install

%lfs_install_end

#---------------------------------------------------------------------------
%files
