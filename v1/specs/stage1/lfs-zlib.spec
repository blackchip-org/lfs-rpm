Name:           lfs-zlib
Version:        1.2.13
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://anduin.linuxfromscratch.org/LFS/zlib-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n zlib-%{version}


%build
%lfs_path 
./configure --prefix=/usr     
make CC="%{lfs_tools}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools}/bin/%{lfs_tgt}-ar" \
     RANLIB="%{lfs_tools}/bin/%{lfs_tgt}-ranlib" \
     CHOST=${lfs_tgt}


%install
%lfs_path 
make DESTDIR=%{buildroot}/%{lfs} install 
%lfs_remove_docs


%files
%{lfs}/usr/include/* 
%{lfs}/usr/lib/*.{a,so*}
%{lfs}/usr/lib/pkgconfig/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
