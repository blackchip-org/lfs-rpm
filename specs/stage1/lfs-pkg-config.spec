Name:           lfs-pkg-config
Version:        0.29.2
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz 

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n pkg-config-%{version}


%build
%lfs_path 
./configure --prefix=/usr \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   \
            --with-internal-glib


%install
%lfs_path 
make DESTDIR=%{buildroot}/%{lfs} install 
%lfs_remove_docs


%files
%{lfs}/usr/bin/* 
%{lfs}/usr/share/aclocal/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
