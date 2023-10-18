Name:           lfs-diffutils
Version:        3.10
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL
Prefix:         %lfs

Source0:        https://ftp.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n diffutils-%{version}


%build
%lfs_path
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(./build-aux/config.guess)
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/diffutils.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 3.10-1
- Initial package


