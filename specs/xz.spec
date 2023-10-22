Name:           xz
Version:        5.4.4
Release:        1%{?dist}
Summary:        LZMA compression utilities
License:        GPLv2+ and Public Domain

Source0:        https://tukaani.org/xz/xz-%{version}.tar.xz

%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as part
of 7-Zip. It provides high compression ratio while keeping the decompression
speed fast.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
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
%lfs_build_end


#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install
rm %{buildroot}/%{lfs_dir}/usr/lib/liblzma.la

%else 
%make DESTDIR=%{buildroot} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/lzma.h
%{lfs_dir}/usr/include/lzma
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/liblzma.pc
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/xz.mo

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
/usr/lib/pkgconfig/liblzma.pc
/usr/share/doc/xz-%{version}
/usr/share/locale/*/LC_MESSAGES/xz.mo
/usr/share/man/{de,fr,ko,pt_BR,ro,uk}/man1/*
/usr/share/man/man1/*

%defattr(755,root,root,755) 
/usr/lib/liblzma.so.%{version}

%endif
