# lfs

%global name        pkgconf
%global version     2.3.0
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Package compiler and linker metadata toolkit
License:        ISC

Source0:        https://distfiles.ariadne.space/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Provides:       pkg-config
Suggests:       %{name}-doc = %{version}

%description
pkgconf is a program which helps to configure compiler and linker flags for
development frameworks. It is similar to pkg-config from freedesktop.org and
handles .pc files in a similar manner as pkg-config.

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr         \
            --host=%{lfs_tgt}     \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}

%else
./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

mkdir -p         %{buildroot}/%{?lfs_dir}/usr/bin
ln -sv pkgconf   %{buildroot}/%{?lfs_dir}/usr/bin/pkg-config

mkdir -p         %{buildroot}/%{?lfs_dir}/usr/share/man/man1
ln -sv pkgconf.1 %{buildroot}/%{?lfs_dir}/usr/share/man/man1/pkg-config.1

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/pkgconf
%{?lfs_dir}/usr/lib/libpkgconf.so*
%{?lfs_dir}/usr/lib/pkgconfig/*
%{?lfs_dir}/usr/share/aclocal/*

%else
/usr/bin/bomtool
/usr/bin/pkgconf
/usr/include/pkgconf/libpkgconf
/usr/lib/libpkgconf.so
/usr/lib/libpkgconf.so.5
%shlib /usr/lib/libpkgconf.so.5.0.0
/usr/lib/pkgconfig/libpkgconf.pc
/usr/share/aclocal/*

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*

%endif