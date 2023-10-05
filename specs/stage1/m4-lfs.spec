Name:           m4-lfs
Version:        1.4.19
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        m4-%{version}.tar.xz

Prefix:         %lfs

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n m4-%{version}


%build
%lfs_path
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)
make


%install
%lfs_path
DESTDIR=%{buildroot}/%{lfs} make install
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/m4.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 1.4.19-1
- Initial package


