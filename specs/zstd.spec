Name:           zstd
Version:        1.5.7
Release:        1%{?dist}
Summary:        Zstd compression library
License:        BSD and GPLv2

Source:         https://github.com/facebook/zstd/releases/download/v%{version}/zstd-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
Zstd, short for Zstandard, is a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level compression ratio.

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
%make prefix=/usr

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1b}
%make DESTDIR=%{buildroot}/%{lfs_dir} prefix=/usr install
rm -f %{buildroot}/%{lfs_dir}/usr/lib/libzstd.a
%discard_docs

%else
%make DESTDIR=%{buildroot} prefix=/usr install
rm -f %{buildroot}/usr/lib/libzstd.a

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1b}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/*

%else
/usr/bin/unzstd
/usr/bin/zstd
/usr/bin/zstdcat
/usr/bin/zstdgrep
/usr/bin/zstdless
/usr/bin/zstdmt
/usr/include/*.h
/usr/lib/libzstd.so
/usr/lib/libzstd.so.1
%shlib /usr/lib/libzstd.so.%{version}
/usr/lib/pkgconfig/libzstd.pc

%files doc
/usr/share/man/man1/*

%endif
