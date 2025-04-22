# lfs

%global name        zstd
%global version     1.5.7
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Zstd compression library
License:        BSD and GPLv2

Source0:        https://github.com/facebook/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
make %{_smp_mflags} prefix=/usr

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} prefix=/usr install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/{lib*.so*,*.a}
%{?lfs_dir}/usr/lib/pkgconfig/*

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
