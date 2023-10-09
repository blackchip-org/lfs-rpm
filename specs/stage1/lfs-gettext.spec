Name:           lfs-gettext
Version:        0.22.3
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.gz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n gettext-%{version}


%build
%lfs_path 
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(./build-aux/config.guess)
make 


%install
%lfs_path 
make DESTDIR=%{buildroot}/%{lfs} install 
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/* 
%{lfs}/usr/lib/gettext 
%{lfs}/usr/lib/*.{a,so*}
%{lfs}/usr/share/aclocal/*
%{lfs}/usr/share/gettext-%{version}
%{lfs}/usr/share/gettext
%{lfs}/usr/share/locale/*/LC_MESSAGES/*.mo 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
