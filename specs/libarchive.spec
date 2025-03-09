Name:           libarchive
Version:        3.7.7
Release:        1%{?dist}
Summary:        Multi-format archive and compression library
License:        BSD

Source:         https://www.libarchive.org/downloads/libarchive-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
The libarchive library features:

* Support for a variety of archive and compression formats.
* Robust automatic format detection, including archive/compression combinations
such as tar.gz.
* Zero-copy internal architecture for high performance.
* Streaming architecture eliminates all limits on size of archive, limits on
entry sizes depend on particular formats.
* Carefully factored code to minimize bloat when programs are statically linked.
* Growing test suite to verify correctness of new ports.
* Works on most POSIX-like systems (including FreeBSD, Linux, Solaris, etc.)
* Supports Windows, including Cygwin, MinGW, and Visual Studio.

The bsdtar and bsdcpio command-line u1tilities are feature- and
performance-competitive with other tar and cpio implementations:

* Reads a variety of formats, including tar, pax, cpio, zip, xar, lha, ar, cab,
mtree, rar, and ISO images.
* Writes tar, pax, cpio, zip, xar, ar, ISO, mtree, and shar archives.
* Automatically handles archives compressed with gzip, bzip2, lzip, xz, lzma,
or compress.
* Unique format conversion feature.

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
./configure
%{make}

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1b}
%make DESTDIR=%{buildroot}/%{lfs_dir} prefix=/usr install
rm %{buildroot}/%{lfs_dir}/usr/lib/*.a

%discard_docs

%else
%make DESTDIR=%{buildroot} prefix=/usr install
rm %{buildroot}/usr/lib/*.a

%endif

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1b}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/*

%else
%files

%files doc
/usr/share/man/man*/*

%endif
