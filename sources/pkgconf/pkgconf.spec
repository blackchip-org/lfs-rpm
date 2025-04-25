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

%if !%{with lfs}
Recommends:     %{name}-doc = %{version}
Recommends:     %{name}-man = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
pkgconf is a program which helps to configure compiler and linker flags for
development frameworks. It is similar to pkg-config from freedesktop.org and
handles .pc files in a similar manner as pkg-config.

%if !%{with lfs}
%description devel
Development files for %{name}

%description static
Static libraries for %{name}

%description doc
Documentation for %{name}

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
./configure --prefix=/usr         \
            --host=%{lfs_tgt}     \
            --disable-static      \
            --docdir=/usr/share/doc/%{name}-%{version}

%else
./configure --prefix=/usr         \
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
/usr/bin/pkg-config
/usr/lib/libpkgconf.so.*

%files devel
/usr/include/pkgconf/libpkgconf
/usr/lib/libpkgconf.so
/usr/lib/pkgconfig/libpkgconf.pc
/usr/share/aclocal/pkg.m4

%files static
/usr/lib/libpkgconf.a

%files doc
/usr/share/doc/%{name}-%{version}

%endif
