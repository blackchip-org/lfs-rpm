%global version     5.4.4

Name:           xz
Version:        %{version}
Release:        1%{?dist}
Summary:        LZMA compression utilities
License:        GPLv2+ and Public Domain

Source0:        https://tukaani.org/xz/xz-%{version}.tar.xz


%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as part
of 7-Zip. It provides high compression ratio while keeping the decompression
speed fast.


%global _build_id_links none


%prep
%setup -q


%build
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/xz-%{version}
make


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/lzcat
/usr/bin/lzcmp
/usr/bin/lzdiff
/usr/bin/lzegrep
/usr/bin/lzfgrep
/usr/bin/lzgrep
/usr/bin/lzless
/usr/bin/lzma
/usr/bin/lzmadec
/usr/bin/lzmainfo
/usr/bin/lzmore
/usr/bin/unlzma
/usr/bin/unxz
/usr/bin/xz
/usr/bin/xzcat
/usr/bin/xzcmp
/usr/bin/xzdec
/usr/bin/xzdiff
/usr/bin/xzegrep
/usr/bin/xzfgrep
/usr/bin/xzgrep
/usr/bin/xzless
/usr/bin/xzmore
/usr/include/lzma.h
/usr/include/lzma
/usr/lib/liblzma.so
/usr/lib/liblzma.so.5
/usr/lib/pkgconfig/liblzma.pc
%attr(755,root,root) /usr/lib/liblzma.so.%{version}
%doc /usr/share/doc/xz-%{version}
/usr/share/locale/*/LC_MESSAGES/xz.mo
/usr/share/man/{de,fr,ko,pt_BR,ro,uk}/man1/*
/usr/share/man/man1/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial pack/etc/ld.so.cache
