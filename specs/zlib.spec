Name:           zlib
Version:        1.3.1
Release:        1%{?dist}
Summary:        The compression and decompression library
License:        zlib and Boost

Source0:        https://zlib.net/fossils/zlib-%{version}.tar.gz

%description
Zlib is a general-purpose, patent-free, lossless data compression library which
is used by many different programs.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr
%make CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     CHOST=%{lfs_tgt}

%else
./configure --prefix=/usr
%make

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/lib/libz.a

%endif

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

