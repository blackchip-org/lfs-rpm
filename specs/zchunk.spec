Name:           zchunk
Version:        1.5.1
Release:        1%{?dist}
Summary:        Compressed file format that splits the file into independent chunks
License:        BSD-2

Source:         https://github.com/zchunk/zchunk/archive/refs/tags/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja

%package man
Summary:        Manual pages for %{name}

%description
zchunk is a compressed file format that splits the file into independent
chunks. This allows you to only download changed chunks when downloading a new
version of the file. Files can hosted on any web server that supports HTTP
ranged requests, with no special software required to serve the files (though
to download only the changed chunks, your client must be zchunk-aware).

zchunk files are protected with strong checksums to verify that the file you
downloaded is, in fact, the file you wanted.

%description man
Manual pages for %{name}

#---------------------------------------------------------------------------
%prep
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
/usr/bin/unzck
/usr/bin/zck
/usr/bin/zck_delta_size
/usr/bin/zck_gen_zdict
/usr/bin/zck_read_header
/usr/include/zck.h
/usr/lib/libzck.so
/usr/lib/libzck.so.1
/usr/lib/pkgconfig/zck.pc

%defattr(755,root,root,755)
/usr/lib/libzck.so.1.5.1

%files man
/usr/share/man/man1/*.gz
