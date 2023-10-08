Name:           lfs-rpm
Version:        4.19.0
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        https://ftp.osuosl.org/pub/rpm/releases/rpm-4.19.x/rpm-%{version}.tar.bz2

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n rpm-%{version}


%build
%lfs_path
mkdir _build 
cd _build 
cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DENABLE_PYTHON=OFF \
      -DENABLE_SQLITE=OFF \
      -DENABLE_TESTSUITE=OFF \
      -DRPM_CONFIGDIR=/usr/lib/rpm \
      -DRPM_VENDOR=lfs \
      ..
make


%install
%lfs_path
DESTDIR=%{buildroot}/%{lfs} make install
%lfs_remove_docs


%files



%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 1.4.19-1
- Initial package


