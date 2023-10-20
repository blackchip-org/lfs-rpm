Name:           zlib
Version:        1.2.13
Release:        1%{?dist}
Summary:        The compression and decompression library
License:        zlib and Boost

Source0:        https://anduin.linuxfromscratch.org/LFS/zlib-%{version}.tar.xz

%description
Zlib is a general-purpose, patent-free, lossless data compression library which
is used by many different programs.

#---------------------------------------------------------------------------
%prep
%setup -q -n zlib-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr
%make CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     CHOST=%{lfs_tgt}

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#--------------------------_dir-------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.{a,so*}
%{lfs_dir}/usr/lib/pkgconfig/*

%endif

