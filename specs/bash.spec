Name:           bash
Version:        5.2.15
Release:        1%{?dist}
Summary:        The GNU Bourne Again shell
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/bash/bash-%{version}.tar.gz

%description
The GNU Bourne Again shell (Bash) is a shell or command language interpreter
that is compatible with the Bourne shell (sh). Bash incorporates useful
features from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr                      \
            --build=$(sh support/config.guess) \
            --host=%{lfs_tgt}                  \
            --without-bash-malloc

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install
mkdir -p %{buildroot}/%{lfs_dir}/bin
ln -s bash %{buildroot}/%{lfs_dir}/usr/bin/sh

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/bash
%{lfs_dir}/usr/lib/bash
%{lfs_dir}/usr/lib/pkgconfig/bash.pc
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/bash.mo
%endif
