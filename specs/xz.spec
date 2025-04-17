# lfs

%global name        xz
%global version     5.6.4
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        LZMA compression utilities
License:        GPLv2+ and Public Domain

Source0:        https://github.com/tukaani-project/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as part
of 7-Zip. It provides high compression ratio while keeping the decompression
speed fast.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr                     \
            --host=%{lfs_tgt}                 \
            --build=$(build-aux/config.guess) \
            --disable-static                  \
            --docdir=/usr/share/doc/xz-%{version}

%else
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/xz-%{version}

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs}
%make DESTDIR=%{buildroot}/%{?lfs_dir} install
rm %{buildroot}/%{?lfs_dir}/usr/lib/liblzma.la
%discard_docs
%discard_locales

%else
%make DESTDIR=%{buildroot} install

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/lzma.h
%{?lfs_dir}/usr/include/lzma
%{?lfs_dir}/usr/lib/*.so*
%{?lfs_dir}/usr/lib/pkgconfig/liblzma.pc

%else
/usr/bin/lzcat
/usr/bin/lzcmp
/usr/bin/lzdiff
/usr/bin/lzegrep
/usr/bin/lzfgrep
/usr/bin/lzgrep
/usr/bin/lzless
/usr/bin/lzma
/usr/bin/lzmadec
/usr/bin/lzmainfo
/usr/bin/lzmore
/usr/bin/unlzma
/usr/bin/unxz
/usr/bin/xz
/usr/bin/xzcat
/usr/bin/xzcmp
/usr/bin/xzdec
/usr/bin/xzdiff
/usr/bin/xzegrep
/usr/bin/xzfgrep
/usr/bin/xzgrep
/usr/bin/xzless
/usr/bin/xzmore
/usr/include/lzma.h
/usr/include/lzma
/usr/lib/liblzma.so
/usr/lib/liblzma.so.5
%shlib /usr/lib/liblzma.so.%{version}
/usr/lib/pkgconfig/liblzma.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/xz-%{version}

%files man
/usr/share/man/{de,fr,ko,pt_BR,ro,uk}/man*/*
/usr/share/man/man*/*

%endif
