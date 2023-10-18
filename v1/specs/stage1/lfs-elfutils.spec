Name:           lfs-elfutils
Version:        0.189
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://sourceware.org/elfutils/ftp/%{version}/elfutils-%{version}.tar.bz2

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n elfutils-%{version}


%build
%lfs_path 
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=x86_64-pc-linux-gnu           \
            --disable-demangler                   \
            --disable-libdebuginfod               \
            --disable-debuginfod


%install
%lfs_path 
make DESTDIR=%{buildroot}/%{lfs} install 
%lfs_remove_docs


%files
%{lfs}/usr/bin/* 
%{lfs}/usr/include/*.h 
%{lfs}/usr/include/elfutils 
%{lfs}/usr/lib/*.{a,so*}
%{lfs}/usr/lib/pkgconfig/* 
%{lfs}/usr/share/locale/*/LC_MESSAGES/elfutils.mo 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
