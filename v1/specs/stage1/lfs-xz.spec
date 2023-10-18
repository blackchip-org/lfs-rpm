Name:           lfs-xz
Version:        5.4.4
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        Public Domain, GPL, LGPL

Source0:        https://tukaani.org/xz/xz-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n xz-%{version}


%build
%lfs_path
./configure --prefix=/usr                     \
            --host=%{lfs_tgt}                 \
            --build=$(build-aux/config.guess) \
            --disable-static                  \
            --docdir=/usr/share/doc/xz-%{version}
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
rm %{buildroot}/%{lfs}/usr/lib/liblzma.la
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/lzma.h
%{lfs}/usr/include/lzma
%{lfs}/usr/lib/*.so*
%{lfs}/usr/lib/pkgconfig/liblzma.pc
%{lfs}/usr/share/locale/*/LC_MESSAGES/xz.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.4.4-1
- Initial package


