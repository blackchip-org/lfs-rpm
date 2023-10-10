%global version     1.0.8
%global lfs_version 12.0

Name:           bzip2
Version:        %{version}
Release:        1%{?dist}
Summary:        A file compression utility
License:        BSD

Source0:        https://www.sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/bzip2-%{version}-install_docs-1.patch

%description
Bzip2 is a freely available, patent-free, high quality data compressor. Bzip2
compresses files to within 10 to 15 percent of the capabilities of the best
techniques available. However, bzip2 has the added benefit of being
approximately two times faster at compression and six times faster at
decompression than those techniques. Bzip2 is not the fastest compression
utility, but it does strike a balance between speed and compression capability.

Install bzip2 if you need a compression utility.


%global _build_id_links none


%prep
%setup -q
%patch 0 -p1


%build
sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile
make -f Makefile-libbz2_so
make clean
make


%install
make PREFIX=%{buildroot}/usr install
cp -av libbz2.so.* %{buildroot}/usr/lib
ln -sv libbz2.so.%{version} %{buildroot}/usr/lib/libbz2.so

cp -v bzip2-shared %{buildroot}/usr/bin/bzip2
for i in /usr/bin/{bzcat,bunzip2}; do
  ln -sfv bzip2 %{buildroot}/$i
done

rm -f %{buildroot}/usr/lib/libbz2.a


%files
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzcmp
/usr/bin/bzdiff
/usr/bin/bzegrep
/usr/bin/bzfgrep
/usr/bin/bzgrep
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/bzless
/usr/bin/bzmore
/usr/include/bzlib.h
/usr/lib/libbz2.so
/usr/lib/libbz2.so.1.0
%attr(755,root,root) /usr/lib/libbz2.so.%{version}
%doc /usr/share/doc/bzip2-%{version}
/usr/share/man/man1/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial pack/etc/ld.so.cache
