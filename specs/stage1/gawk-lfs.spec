Name:           gawk-lfs
Version:        5.2.2
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        gawk-%{version}.tar.xz

Prefix:         %lfs

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n gawk-%{version}


%build
%lfs_path
sed -i 's/extras//' Makefile.in
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
%{lfs}/usr/include/*
%{lfs}/usr/lib/gawk
%{lfs}/usr/libexec/awk
%{lfs}/usr/share/awk
%{lfs}/usr/share/locale/*/LC_MESSAGES/gawk.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.2-1
- Initial package


