Name:           lz4
Version:        1.10.0
Release:        1%{?dist}
Summary:        Extremely fast compression algorithm
License:        GPLv2+ and BSD

Source:         https://github.com/lz4/lz4/releases/download/v%{version}/lz4-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
LZ4 is an extremely fast loss-less compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-core CPU. It also features
an extremely fast decoder, with speed in multiple GB/s per core, typically
reaching RAM speed limits on multi-core systems.

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
%make BUILD_STATIC=no PREFIX=/usr

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} BUILD_STATIC=no PREFIX=/usr install

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
%shlib /usr/lib/liblz4.so.%{version}
/usr/lib/pkgconfig/liblz4.pc

%files doc
/usr/share/man/man*/*