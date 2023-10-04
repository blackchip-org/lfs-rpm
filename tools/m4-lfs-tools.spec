Name:           m4-lfs-tools
Version:        1.4.19
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        m4-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n m4-%{version}


%build
export PATH=%{tools}/bin:${PATH}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)
make


%install
export PATH=%{tools}/bin:${PATH}
DESTDIR=%{buildroot}/%{lfs} make install

rm -rf %{buildroot}/%{lfs}/usr/share/info
rm -rf %{buildroot}/%{lfs}/usr/share/man


%files
%{lfs}/usr/bin/*
%{lfs}/usr/share/locale/*/LC_MESSAGES/m4.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 1.4.19-1
- Initial package


