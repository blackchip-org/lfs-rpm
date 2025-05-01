# dnf

%global name            zchunk
%global version         1.5.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Compressed file format that splits the file into independent chunks
License:        BSD-2

Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  meson
BuildRequires:  ninja

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
zchunk is a compressed file format that splits the file into independent
chunks. This allows you to only download changed chunks when downloading a new
version of the file. Files can hosted on any web server that supports HTTP
ranged requests, with no special software required to serve the files (though
to download only the changed chunks, your client must be zchunk-aware).

zchunk files are protected with strong checksums to verify that the file you
downloaded is, in fact, the file you wanted.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
meson --prefix=/usr build
cd build
ninja

#---------------------------------------------------------------------------
%install
cd build
DESTDIR=%{buildroot} ninja install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/bin/unzck
/usr/bin/zck
/usr/bin/zck_delta_size
/usr/bin/zck_gen_zdict
/usr/bin/zck_read_header
/usr/lib/libzck.so.*

%files devel
/usr/include/zck.h
/usr/lib/libzck.so
/usr/lib/pkgconfig/zck.pc

%files man
/usr/share/man/man*/*.gz

%endif
