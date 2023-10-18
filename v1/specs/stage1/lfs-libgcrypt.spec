Name:           lfs-libgcrypt
Version:        1.10.2
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n libgcrypt-%{version}


%build
%lfs_path 
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(build-aux/config.guess)     \
            --with-libgpg-error-prefix=%{lfs}/usr 
make 


%install
%lfs_path 
make DESTDIR=%{buildroot}/%{lfs} install 
%lfs_remove_docs


%files
%{lfs}/usr/bin/* 
%{lfs}/usr/include/* 
%{lfs}/usr/lib/*.so*
%{lfs}/usr/lib/pkgconfig/* 
%{lfs}/usr/share/aclocal/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
