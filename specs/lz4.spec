Name:           lz4
Version:        1.10.0
Release:        1%{?dist}
Summary:        Extremely fast compression algorithm
License:        GPLv2+ and BSD

Source0:        https://github.com/lz4/lz4/releases/download/v%{version}/lz4-%{version}.tar.gz

%description
LZ4 is an extremely fast loss-less compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-core CPU. It also features
an extremely fast decoder, with speed in multiple GB/s per core, typically
reaching RAM speed limits on multi-core systems.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%make BUILD_STATIC=no PREFIX=/usr

%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} BUILD_STATIC=no PREFIX=/usr install

%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/lz4
/usr/bin/lz4c
/usr/bin/lz4cat
/usr/bin/unlz4
/usr/include/lz4.h
/usr/include/lz4frame.h
/usr/include/lz4hc.h
/usr/lib/liblz4.so
/usr/lib/liblz4.so.1
/usr/lib/pkgconfig/liblz4.pc
/usr/share/man/man1/lz4.1.gz
/usr/share/man/man1/lz4c.1.gz
/usr/share/man/man1/lz4cat.1.gz
/usr/share/man/man1/unlz4.1.gz

%defattr(755,root,root,755)
/usr/lib/liblz4.so.%{version}
