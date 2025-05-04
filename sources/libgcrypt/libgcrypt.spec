# rpm

%global name            libgcrypt
%global version         1.11.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A general-purpose cryptography library
License:        LGPLv2+

Source0:        https://www.gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
Libgcrypt is a general purpose crypto library based on the code use in GNU
Privacy Guard. This is a development version.

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(build-aux/config.guess)     \
            --with-libgpg-error-prefix=%{lfs_dir}/usr

%else
./configure --prefix=/usr

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*.h
%{?lfs_dir}/usr/lib/lib*.so*
%{?lfs_dir}/usr/lib/pkgconfig/*
%{?lfs_dir}/usr/share/aclocal/*

%else
/usr/bin/dumpsexp
/usr/bin/hmac256
/usr/bin/libgcrypt-config
/usr/bin/mpicalc
/usr/lib/libgcrypt.so.*

%files devel
/usr/include/*.h
/usr/lib/libgcrypt.so
/usr/lib/pkgconfig/libgcrypt.pc
/usr/share/aclocal/%{name}.m4

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif

