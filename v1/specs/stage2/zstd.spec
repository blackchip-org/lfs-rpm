%global version     1.5.5

Name:           zstd
Version:        %{version}
Release:        1%{?dist}
Summary:        Zstd compression library
License:        BSD and GPLv2

Source0:        https://github.com/facebook/zstd/releases/download/v%{version}/zstd-%{version}.tar.gz


%description
Zstd, short for Zstandard, is a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level compression ratio.


%global _build_id_links none


%prep
%setup -q


%build
make prefix=/usr


%install
make prefix=%{buildroot}/usr install
rm -f %{buildroot}/usr/lib/libzstd.a


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
%attr(755,root,root) /usr/lib/libzstd.so.%{version}
/usr/lib/pkgconfig/libzstd.pc
/usr/share/man/man1/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial pack/etc/ld.so.cache
