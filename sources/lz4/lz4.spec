# lfs

%global name            lz4
%global version         1.10.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Extremely fast compression algorithm
License:        GPLv2+ and BSD

Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
LZ4 is an extremely fast loss-less compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-core CPU. It also features
an extremely fast decoder, with speed in multiple GB/s per core, typically
reaching RAM speed limits on multi-core systems.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs}
make %{?_smp_mflags} BUILD_STATIC=no PREFIX=/usr

%else
make %{?_smp_mflags} PREFIX=/usr

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs}
make DESTDIR=%{buildroot} BUILD_STATIC=no PREFIX=/usr install

%else
make DESTDIR=%{buildroot} PREFIX=/usr install

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/bin/lz4
/usr/bin/lz4c
/usr/bin/lz4cat
/usr/bin/unlz4
/usr/lib/liblz4.so.*

%files devel
/usr/include/*.h
/usr/lib/liblz4.so
/usr/lib/pkgconfig/liblz4.pc

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/liblz4.a

%endif
