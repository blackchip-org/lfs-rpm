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

./configure --prefix=/usr

%if %{with lfs_stage1}
%make CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     CHOST=%{lfs_tgt}

%else 
%make 

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%else 
%make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/lib/libz.a

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.{a,so*}
%{lfs_dir}/usr/lib/pkgconfig/*

%else 
/usr/include/*
/usr/lib/libz.so{,.1}
/usr/lib/pkgconfig/zlib.pc
/usr/share/man/man3/*

%defattr(755,root,root,755) 
/usr/lib/libz.so.%{version}

%endif

