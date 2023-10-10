%global version     5.45
%global so_version  1.0.0

Name:           file
Version:        %{version}
Release:        1%{?dist}
Summary:        A utility for determining file types
License:        BSD

Source0:        https://astron.com/pub/file/file-%{version}.tar.gz


%description
The file command is used to identify a particular file according to the type of
data contained by the file. File can identify many different file types,
including ELF binaries, system libraries, RPM packages, and different graphics
formats.


%global _build_id_links none


%prep
%setup -q


%build
./configure --prefix=/usr
make


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/file
/usr/include/magic.h
/usr/lib/libmagic.so
/usr/lib/libmagic.so.1
%attr(755,root,root) /usr/lib/libmagic.so.%{so_version}
/usr/lib/pkgconfig/libmagic.pc
/usr/share/man/man{1,3,4}/*
/usr/share/misc/magic.mgc


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial pack/etc/ld.so.cache
