# rpm

%global name        libgpg-error
%global version     1.51
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Library for error values used by GnuPG components
License:        LGPLv2+

Source0:        https://www.gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
This is a library that defines common error values for all GnuPG components.
Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt, pinentry, SmartCard
Daemon and possibly more in the future.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   \
            --enable-install-gpg-error-config

%else
./configure --prefix=/usr \
            --enable-install-gpg-error-config

%endif
make -j %{nproc}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*.so*
%{?lfs_dir}/usr/lib/pkgconfig/*
%{?lfs_dir}/usr/share/aclocal/*
%{?lfs_dir}/usr/share/common-lisp/source/gpg-error
%{?lfs_dir}/usr/share/libgpg-error

%else
/usr/bin/gpg-error
/usr/bin/gpg-error-config
/usr/bin/gpgrt-config
/usr/bin/yat2m
/usr/include/*.h
/usr/lib/libgpg-error.so
/usr/lib/libgpg-error.so.0
%shlib /usr/lib/libgpg-error.so.0.38.0
/usr/lib/pkgconfig/gpg-error.pc
/usr/share/aclocal/*
/usr/share/common-lisp/source/gpg-error
/usr/share/libgpg-error

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
