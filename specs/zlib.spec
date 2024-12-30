Name:           zlib
Version:        1.3.1
Release:        1%{?dist}
Summary:        The compression and decompression library
License:        zlib and Boost

Source:         https://zlib.net/fossils/zlib-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
Zlib is a general-purpose, patent-free, lossless data compression library which
is used by many different programs.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

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
%shlib /usr/lib/libz.so.%{version}
/usr/lib/pkgconfig/zlib.pc

%files doc
/usr/share/man/man*/*

%endif

