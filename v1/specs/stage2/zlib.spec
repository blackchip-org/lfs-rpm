%global version     1.2.13

Name:           zlib
Version:        %{version}
Release:        1%{?dist}
Summary:        The compression and decompression library
License:        zlib and Boost

Source0:        https://anduin.linuxfromscratch.org/LFS/zlib-%{version}.tar.xz


%description
Zlib is a general-purpose, patent-free, lossless data compression library which
is used by many different programs.


%global _build_id_links none


%prep
%setup -q


%build
./configure --prefix=/usr
make


%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/usr/lib/libz.a


%files
/usr/include/*
%attr(755,root,root) /usr/lib/libz.so.%{version}
/usr/lib/libz.so{,.1}
/usr/lib/pkgconfig/zlib.pc
/usr/share/man/man3/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial pack/etc/ld.so.cache
