Name:           libgpg-error
Version:        1.50
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
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   \
            --enable-install-gpg-error-config

%else
./configure --prefix=/usr \
            --enable-install-gpg-error-config

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install

%endif

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

%else
/usr/bin/gpg-error
/usr/bin/gpg-error-config
/usr/bin/gpgrt-config
/usr/bin/yat2m
/usr/include/*.h
/usr/lib/libgpg-error.so
/usr/lib/libgpg-error.so.0
/usr/lib/pkgconfig/gpg-error.pc
/usr/share/aclocal/*
/usr/share/common-lisp/source/gpg-error
/usr/share/info/*
/usr/share/libgpg-error
/usr/share/locale/*/LC_MESSAGES/libgpg-error.mo
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libgpg-error.so.0.*

%endif
