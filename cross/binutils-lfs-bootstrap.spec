Name:           binutils-lfs-bootstrap
Version:        2.41
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        binutils-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n binutils-%{version}


%build
mkdir build
cd build

../configure --prefix=%{tools} \
             --with-sysroot=%{lfs} \
             --target=%{lfs_tgt}   \
             --disable-nls         \
             --enable-gprofng=no   \
             --disable-werror
make


%install
cd build
DESTDIR=%{buildroot} make install

rm -rf %{buildroot}/%{tools}/share/info
rm -rf %{buildroot}/%{tools}/share/man*


%files
%{tools}/bin/*
%{tools}/lib/*
%{tools}/%{lfs_tgt}/bin/*
%{tools}/%{lfs_tgt}/lib/*


%changelog
* Tue Oct 3 2023 Mike McGann <mike.mcgann@blackchip.org> - 13.2.0-1
- Initial package


