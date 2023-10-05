Name:           sed-lfs
Version:        4.9
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        sed-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n sed-%{version}


%build
%lfs_path
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/sed.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 4.9-1
- Initial package


