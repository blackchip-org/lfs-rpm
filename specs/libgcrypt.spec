Name:           libgcrypt
Version:        1.10.3
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

%if %{with lfs_stage1}
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(build-aux/config.guess)     \
            --with-libgpg-error-prefix=%{lfs_dir}/usr

%else
./configure --prefix=/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%else
%make DESTDIR=%{buildroot} install

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

%else
/usr/bin/dumpsexp
/usr/bin/hmac256
/usr/bin/libgcrypt-config
/usr/bin/mpicalc
/usr/include/*.h
/usr/lib/libgcrypt.so
/usr/lib/libgcrypt.so.20
/usr/lib/pkgconfig/libgcrypt.pc
/usr/share/aclocal/*
/usr/share/info/*
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libgcrypt.so.20.4.2

%endif

