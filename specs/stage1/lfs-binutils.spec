Name:           lfs-binutils
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
%lfs_path
sed '6009s/$add_dir//' -i ltmain.sh
mkdir build
cd build
../configure                   \
    --prefix=/usr              \
    --build=$(../config.guess) \
    --host=%{lfs_tgt}          \
    --disable-nls              \
    --enable-shared            \
    --enable-gprofng=no        \
    --disable-werror           \
    --enable-64-bit-bfd
make


%install
%lfs_path
cd build
DESTDIR=%{buildroot}/%{lfs} make install
rm -v %{buildroot}/%{lfs}/usr/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/*
%{lfs}/usr/lib/bfd-plugins/libdep.so
%{lfs}/usr/lib/*.so*
%{lfs}/usr/%{lfs_tgt}/bin/*
%{lfs}/usr/%{lfs_tgt}/lib/ldscripts/*

%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 2.41-1
- Initial package
