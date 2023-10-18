Name:           lfs-libgpg-error
Version:        1.47
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n libgpg-error-%{version}


%build
%lfs_path 
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   \
            --enable-install-gpg-error-config
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
%{lfs}/usr/share/common-lisp/source/gpg-error 
%{lfs}/usr/share/libgpg-error 
%{lfs}/usr/share/locale/*/LC_MESSAGES/libgpg-error.mo 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
