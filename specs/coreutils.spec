Name:           coreutils
Version:        9.3
Release:        1%{?dist}
Summary:        A set of basic GNU tools commonly used in shell scripts
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz

%if %{without lfs_bootstrap}
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/coreutils-%{version}-i18n-1.patch
%endif

%description
These are the GNU core utilities. This package is the combination of the old
GNU fileutils, sh-utils, and textutils packages.

#---------------------------------------------------------------------------
%prep
%setup -q


#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr                     \
            --host=%{lfs_tgt}                 \
            --build=$(build-aux/config.guess) \
            --enable-install-program=hostname \
            --enable-no-install-program=kill,uptime \
            gl_cv_macro_MB_CUR_MAX_good=y

%endif
%make
%lfs_build_end
%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 9.3-1
- Initial package
#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
make DESTDIR=%{buildroot}/%{lfs_dir} install
mkdir -p %{buildroot}/%{lfs_dir}/usr/sbin
mv -v %{buildroot}/%{lfs_dir}/usr/bin/chroot %{buildroot}/%{lfs_dir}/usr/sbin

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/sbin/*
%{lfs_dir}/usr/libexec/coreutils
%{lfs_dir}/usr/share/locale/*/LC_{MESSAGES,TIME}/coreutils.mo
%endif

