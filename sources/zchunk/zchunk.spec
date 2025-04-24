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
Suggests:       %{name}-doc = %{version}

%description
zchunk is a compressed file format that splits the file into independent
chunks. This allows you to only download changed chunks when downloading a new
version of the file. Files can hosted on any web server that supports HTTP
ranged requests, with no special software required to serve the files (though
to download only the changed chunks, your client must be zchunk-aware).

zchunk files are protected with strong checksums to verify that the file you
downloaded is, in fact, the file you wanted.

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
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/bin/unzck
/usr/bin/zck
/usr/bin/zck_delta_size
/usr/bin/zck_gen_zdict
/usr/bin/zck_read_header
/usr/include/zck.h
/usr/lib/libzck.so
/usr/lib/libzck.so.1
%shlib /usr/lib/libzck.so.1.5.1
/usr/lib/pkgconfig/zck.pc

%files doc
/usr/share/man/man*/*.gz

%endif
