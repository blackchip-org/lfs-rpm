Name:           lfs-tools-binutils
Version:        2.41
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        https://sourceware.org/pub/binutils/releases/binutils-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n binutils-%{version}


%build
mkdir build
cd build

../configure --prefix=%{lfs_tools} \
             --with-sysroot=%{lfs} \
             --target=%{lfs_tgt}   \
             --disable-nls         \
             --enable-gprofng=no   \
             --disable-werror
make


%install
cd build
DESTDIR=%{buildroot} make install
%lfs_remove_docs


%files
%{lfs_tools}/bin/*
%{lfs_tools}/lib/*
%{lfs_tools}/%{lfs_tgt}/bin/*
%{lfs_tools}/%{lfs_tgt}/lib/*


%changelog
* Tue Oct 3 2023 Mike McGann <mike.mcgann@blackchip.org> - 13.2.0-1
- Initial package


