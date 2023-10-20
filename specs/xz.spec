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

%if %{with lfs_bootstrap}
./configure --prefix=/usr                     \
            --host=%{lfs_tgt}                 \
            --build=$(build-aux/config.guess) \
            --disable-static                  \
            --docdir=/usr/share/doc/xz-%{version}

%endif
%make
%lfs_build_end


#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install
rm %{buildroot}/%{lfs_dir}/usr/lib/liblzma.la

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/lzma.h
%{lfs_dir}/usr/include/lzma
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/liblzma.pc
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/xz.mo
%endif
