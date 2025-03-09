# extra

Name:           libgcrypt
Version:        1.11.0
Release:        1%{?dist}
Summary:        A general-purpose cryptography library
License:        LGPLv2+

Source:         https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2

Suggests:       %{name}-doc = %{version}

%description
Libgcrypt is a general purpose crypto library based on the code use in GNU
Privacy Guard. This is a development version.

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

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
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(build-aux/config.guess)     \
            --with-libgpg-error-prefix=%{lfs_dir}/usr

%else
./configure --prefix=/usr

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

%else
/usr/bin/dumpsexp
/usr/bin/hmac256
/usr/bin/libgcrypt-config
/usr/bin/mpicalc
/usr/include/*.h
/usr/lib/libgcrypt.so
/usr/lib/libgcrypt.so.20
%shlib /usr/lib/libgcrypt.so.20.5.0
/usr/lib/pkgconfig/libgcrypt.pc
/usr/share/aclocal/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif

