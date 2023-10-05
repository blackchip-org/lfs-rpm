Name:           tar-lfs
Version:        1.35
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        tar-%{version}.tar.xz

Prefix:         %lfs

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n tar-%{version}


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
%{lfs}/usr/libexec/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/tar.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 1.35-1
- Initial package


