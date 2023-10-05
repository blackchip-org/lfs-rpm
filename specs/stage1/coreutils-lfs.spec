Name:           coreutils-lfs
Version:        9.3
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        coreutils-%{version}.tar.xz

Prefix:         %lfs

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n coreutils-%{version}


%build
%lfs_path
./configure --prefix=/usr                     \
            --host=%{lfs_tgt}                 \
            --build=$(build-aux/config.guess) \
            --enable-install-program=hostname \
            --enable-no-install-program=kill,uptime \
            gl_cv_macro_MB_CUR_MAX_good=y
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
mkdir -p %{buildroot}/%{lfs}/usr/sbin
mv -v %{buildroot}/%{lfs}/usr/bin/chroot %{buildroot}/%{lfs}/usr/sbin
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/sbin/*
%{lfs}/usr/libexec/coreutils
%{lfs}/usr/share/locale/*/LC_MESSAGES/coreutils.mo
%{lfs}/usr/share/locale/*/LC_TIME/coreutils.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 9.3-1
- Initial package


