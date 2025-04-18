# lfs

%global name        lz4
%global version     1.10.0
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Extremely fast compression algorithm
License:        GPLv2+ and BSD

Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%make BUILD_STATIC=no PREFIX=/usr

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} BUILD_STATIC=no PREFIX=/usr install

%if %{with lfs}
%discard_docs
%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
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

%endif
