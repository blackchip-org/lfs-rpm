Name:           libgpg-error
Version:        1.47
Release:        1%{?dist}
Summary:        Library for error values used by GnuPG components
License:        LGPLv2+

Source0:        https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2

%description
This is a library that defines common error values for all GnuPG components.
Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt, pinentry, SmartCard
Daemon and possibly more in the future.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   \
            --enable-install-gpg-error-config

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/*
%{lfs_dir}/usr/share/aclocal/*
%{lfs_dir}/usr/share/common-lisp/source/gpg-error
%{lfs_dir}/usr/share/libgpg-error
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/libgpg-error.mo

%endif
