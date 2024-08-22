Name:           zstd
Version:        1.5.6
Release:        1%{?dist}
Summary:        Zstd compression library
License:        BSD and GPLv2

Source0:        https://github.com/facebook/zstd/releases/download/v%{version}/zstd-%{version}.tar.gz

%description
Zstd, short for Zstandard, is a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level compression ratio.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%make prefix=/usr
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make prefix=%{buildroot}/usr install
rm -f %{buildroot}/usr/lib/libzstd.a
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt
/usr/include/*.h
/usr/lib/libzstd.so
/usr/lib/libzstd.so.1
/usr/lib/pkgconfig/libzstd.pc
/usr/share/man/man1/*

%defattr(755,root,root,755) 
/usr/lib/libzstd.so.%{version}
