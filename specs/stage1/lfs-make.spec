Name:           lfs-make
Version:        4.4.1
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        https://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n make-%{version}


%build
%lfs_path
./configure --prefix=/usr   \
            --without-guile \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/make.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 4.4.1-1
- Initial package


