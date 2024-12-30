Name:           libgpg-error
Version:        1.50
Release:        1%{?dist}
Summary:        Library for error values used by GnuPG components
License:        LGPLv2+

Source:         https://www.gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2

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
%remove_info_dir

%endif

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

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
%shlib /usr/lib/libgpg-error.so.0.37.0
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
