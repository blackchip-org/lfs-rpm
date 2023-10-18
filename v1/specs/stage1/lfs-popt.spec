Name:           lfs-popt
Version:        1.19
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n popt-%{version}


%build
%lfs_path 
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   


%install
%lfs_path 
make DESTDIR=%{buildroot}/%{lfs} install 
%lfs_remove_docs


%files
%{lfs}/usr/include/*
%{lfs}/usr/lib/* 
%{lfs}/usr/share/locale/*/LC_MESSAGES/popt.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
