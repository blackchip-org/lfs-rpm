# lfs

%global name        pkgconf
%global version     2.3.0
%global release     1
%global so_version  5

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
%use_lfs_tools
./configure --prefix=/usr         \
            --host=%{lfs_tgt}     \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}

%else
./configure --prefix=/usr         \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}

%endif
%make


#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

ln -sv pkgconf   %{buildroot}/%{lfs_dir}/usr/bin/pkg-config
rm -rf           %{buildroot}/%{lfs_dir}/usr/share/aclocal
%discard_docs

%else
%make DESTDIR=%{buildroot} install
mkdir -p         %{buildroot}/usr/bin
mkdir -p         %{buildroot}/usr/share/man/man1
ln -sv pkgconf   %{buildroot}/usr/bin/pkg-config
ln -sv pkgconf.1 %{buildroot}/usr/share/man/man1/pkg-config.1

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/pkgconf
%{lfs_dir}/usr/lib/libpkgconf.so
%{lfs_dir}/usr/lib/libpkgconf.so.%{so_version}
%shlib %{lfs_dir}/usr/lib/libpkgconf.so.%{so_version}.*
%{lfs_dir}/usr/lib/pkgconfig/*

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