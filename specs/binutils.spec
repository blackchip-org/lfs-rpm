Name:           binutils
Version:        2.43.1
Release:        1%{?dist}
Summary:        A GNU collection of binary utilities
License:        GPLv3+

Source0:        https://sourceware.org/pub/binutils/releases/binutils-%{version}.tar.xz

%description
Binutils is a collection of binary utilities, including ar (for creating,
modifying and extracting from archives), as (a family of GNU assemblers), gprof
(for displaying call graph profile data), ld (the GNU linker), nm (for listing
symbols from object files), objcopy (for copying and translating object files),
objdump (for displaying information from object files), ranlib (for generating
an index for the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes of an
object or archive file), strings (for listing printable strings from files),
strip (for discarding symbols), and addr2line (for converting addresses to file
and line).

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir build
cd build

%if %{with lfs_stage1a}
../configure --prefix=%{lfs_tools_dir}  \
             --with-sysroot=%{lfs_dir}  \
             --target=%{lfs_tgt}        \
             --disable-nls              \
             --enable-gprofng=no        \
             --disable-werror           \
             --enable-new-dtags         \
             --enable-default-hash-style=gnu
%make

%elif %{with lfs_stage1b}
sed '6009s/$add_dir//' -i ../ltmain.sh
../configure --prefix=/usr              \
             --build=$(../config.guess) \
             --host=%{lfs_tgt}          \
             --disable-nls              \
             --enable-shared            \
             --enable-gprofng=no        \
             --disable-werror           \
             --enable-64-bit-bfd
%make

%else
../configure --prefix=/usr       \
             --sysconfdir=/etc   \
             --enable-gold       \
             --enable-ld=default \
             --enable-plugins    \
             --enable-shared     \
             --disable-werror    \
             --enable-64-bit-bfd \
             --with-system-zlib
%make tooldir=/usr

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin
cd build

%if %{with lfs_stage1a}
DESTDIR=%{buildroot} %make install

%elif %{with lfs_stage1b}
DESTDIR=%{buildroot}/%{lfs_dir} %make install
rm -v %{buildroot}/%{lfs_dir}/usr/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}

%else
%make tooldir=/usr DESTDIR=%{buildroot} install
rm -fv %{buildroot}/usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a
rm -rf %{buildroot}/usr/share/info/dir

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%check
cd build
make -k check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1a}
%{lfs_tools_dir}/bin/*
%{lfs_tools_dir}/lib/*
%{lfs_tools_dir}/%{lfs_tgt}/bin/*
%{lfs_tools_dir}/%{lfs_tgt}/lib/*

%elif %{with lfs_stage1b}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/bfd-plugins/libdep.so
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/%{lfs_tgt}/bin/*
%{lfs_dir}/usr/%{lfs_tgt}/lib/ldscripts/*

%else
%config(noreplace) /etc/gprofng.rc
/usr/bin/addr2line
/usr/bin/ar
/usr/bin/as
/usr/bin/c++filt
/usr/bin/dwp
/usr/bin/elfedit
/usr/bin/gp-archive
/usr/bin/gp-collect-app
/usr/bin/gp-display-html
/usr/bin/gp-display-src
/usr/bin/gp-display-text
/usr/bin/gprof
/usr/bin/gprofng
/usr/bin/ld
/usr/bin/ld.bfd
/usr/bin/ld.gold
/usr/bin/nm
/usr/bin/objcopy
/usr/bin/objdump
/usr/bin/ranlib
/usr/bin/readelf
/usr/bin/size
/usr/bin/strings
/usr/bin/strip
/usr/include/*.h
/usr/lib/bfd-plugins/*
/usr/lib/gprofng
/usr/lib/ldscripts
/usr/lib/libbfd-%{version}.so
/usr/lib/libbfd.so
/usr/lib/libctf-nobfd.so
/usr/lib/libctf-nobfd.so.0
/usr/lib/libctf.so
/usr/lib/libctf.so.0
/usr/lib/libgprofng.so
/usr/lib/libgprofng.so.0
/usr/lib/libopcodes-%{version}.so
/usr/lib/libopcodes.so
/usr/lib/libsframe.so
/usr/lib/libsframe.so.1
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libctf-nobfd.so.0.0.0
/usr/lib/libctf.so.0.0.0
/usr/lib/libgprofng.so.0.0.0
/usr/lib/libsframe.so.1.0.0

%endif

