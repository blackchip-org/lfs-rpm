%global version     2.41

Name:           binutils
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU collection of binary utilities
License:        GPLv3+

Source0:        https://sourceware.org/pub/binutils/releases/binutils-%{version}.tar.xz

%global _build_id_links none

%description
Binutils is a collection of binary utilities, including ar (for creating,
modifying and extracting from archives), as (a family of GNU assemblers), gprof
(for displaying call graph profile data), ld (the GNU linker), nm (for listing
symbols from object files), objcopy (for copying and translating object files),
objdump (for displaying information from object files), ranlib (for generating
an index for the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes of an
object or archive file), strings (for listing printable strings from files),
strip (for discarding symbols), and addr2line (for converting addresses to file
and line).


%prep
%setup -q


%build
mkdir -v build
cd       build

../configure --prefix=/usr       \
             --sysconfdir=/etc   \
             --enable-gold       \
             --enable-ld=default \
             --enable-plugins    \
             --enable-shared     \
             --disable-werror    \
             --enable-64-bit-bfd \
             --with-system-zlib
make tooldir=/usr


%check
cd build
make -k check


%install
cd build
make tooldir=/usr DESTDIR=%{buildroot} install
rm -fv %{buildroot}/usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a
rm -rf %{buildroot}/usr/share/info/dir


%files
%config(noreplace) /etc/gprofng.rc
/usr/bin/addr2line
/usr/bin/ar
/usr/bin/as
/usr/bin/c++filt
/usr/bin/dwp
/usr/bin/elfedit
/usr/bin/gp-archive
/usr/bin/gp-collect-app
/usr/bin/gp-display-html
/usr/bin/gp-display-src
/usr/bin/gp-display-text
/usr/bin/gprof
/usr/bin/gprofng
/usr/bin/ld
/usr/bin/ld.bfd
/usr/bin/ld.gold
/usr/bin/nm
/usr/bin/objcopy
/usr/bin/objdump
/usr/bin/ranlib
/usr/bin/readelf
/usr/bin/size
/usr/bin/strings
/usr/bin/strip
/usr/include/*.h
/usr/lib/bfd-plugins/*
/usr/lib/gprofng
/usr/lib/ldscripts
/usr/lib/libbfd-2.41.so
/usr/lib/libbfd.so
/usr/lib/libctf-nobfd.so
/usr/lib/libctf-nobfd.so.0
/usr/lib/libctf.so
/usr/lib/libctf.so.0
/usr/lib/libgprofng.so
/usr/lib/libgprofng.so.0
/usr/lib/libopcodes-2.41.so
/usr/lib/libopcodes.so
/usr/lib/libsframe.so
/usr/lib/libsframe.so.1
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libctf-nobfd.so.0.0.0
/usr/lib/libctf.so.0.0.0
/usr/lib/libgprofng.so.0.0.0
/usr/lib/libsframe.so.1.0.0


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
