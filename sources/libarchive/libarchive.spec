# rpm

%global name        libarchive
%global version     3.7.7
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Multi-format archive and compression library
License:        BSD

Source0:        https://www.libarchive.org/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
mkdir -p _build
cd _build

cat > x86_64-lfs-linux-gnu.cmake <<EOF
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSROOT %{lfs_dir})

set(CMAKE_C_COMPILER %{lfs_tools_dir}/bin/x86_64-lfs-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER %{lfs_tools_dir}/bin/x86_64-lfs-linux-gnu-g++)

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

set(ENV{PKG_CONFIG_PATH} %{lfs_dir}/usr/lib/pkgconfig)
EOF

cmake --toolchain x86_64-lfs-linux-gnu.cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ..
make -j %{nproc}

%else
./configure
make -j %{nproc}
%endif


#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
cd _build
make DESTDIR=%{buildroot}/%{lfs_dir} install

%else
make DESTDIR=%{buildroot} prefix=/usr install

%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/{*.a,*.so*}
%{?lfs_dir}/usr/lib/pkgconfig/*

%else
/usr/bin/bsdcat
/usr/bin/bsdcpio
/usr/bin/bsdtar
/usr/bin/bsdunzip
/usr/include/archive.h
/usr/include/archive_entry.h
/usr/lib/libarchive.so
/usr/lib/libarchive.so.13
/usr/lib/libarchive.so.13.7.7
/usr/lib/pkgconfig/libarchive.pc

%files doc
/usr/share/man/man*/*

%endif
