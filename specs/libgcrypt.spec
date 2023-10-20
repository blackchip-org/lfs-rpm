Name:           libgcrypt
Version:        1.10.2
Release:        1%{?dist}
Summary:        A general-purpose cryptography library
License:        LGPLv2+

Source0:        https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2

%description
Libgcrypt is a general purpose crypto library based on the code use in GNU
Privacy Guard. This is a development version.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(build-aux/config.guess)     \
            --with-libgpg-error-prefix=%{lfs_dir}/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/*
%{lfs_dir}/usr/share/aclocal/*

%endif

