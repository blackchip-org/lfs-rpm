# lfs

%global name             zlib
%global version          1.3.1
%global release          1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The compression and decompression library
License:        zlib and Boost

Source0:        https://zlib.net/fossils/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

Provides:       zlib-devel

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
Zlib is a general-purpose, patent-free, lossless data compression library which
is used by many different programs.

%if !%{with lfs}
%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr
make %{?_smp_mflags} \
     CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     CHOST=%{lfs_tgt}

%else
./configure --prefix=/usr
make %{?_smp_mflags}

%endif

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*.{a,so*}
%{?lfs_dir}/usr/lib/pkgconfig/*

%else
/usr/include/*.h
/usr/lib/libz.so*
/usr/lib/pkgconfig/zlib.pc

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libz.a

%endif

