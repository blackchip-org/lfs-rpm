Name:           binutils
Version:        2.44
Release:        1%{?dist}
Summary:        A GNU collection of binary utilities
License:        GPLv3+

Source0:        https://sourceware.org/pub/binutils/releases/%{name}-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

BuildRequires:  texinfo

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
%setup -q

#---------------------------------------------------------------------------
%build
mkdir -p    build
cd          build

%if %{with lfs_stage1a}
%use_lfs_tools
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
%use_lfs_tools
sed '6009s/$add_dir//' -i ../ltmain.sh
../configure --prefix=/usr              \
             --build=$(../config.guess) \
             --host=%{lfs_tgt}          \
             --disable-nls              \
             --enable-shared            \
             --enable-gprofng=no        \
             --disable-werror           \
             --enable-64-bit-bfd        \
             --enable-new-dtags         \
             --enable-default-hash-style=gnu
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
             --with-system-zlib  \
             --enable-new-dtags  \
             --enable-default-hash-style=gnu
%make tooldir=/usr

%endif

#---------------------------------------------------------------------------
%install
cd build

%if %{with lfs_stage1a}
%use_lfs_tools
DESTDIR=%{buildroot} %make install
%discard_docs

%elif %{with lfs_stage1b}
%use_lfs_tools
DESTDIR=%{buildroot}/%{lfs_dir} %make install
rm -v %{buildroot}/%{lfs_dir}/usr/lib/lib{bfd,ctf,ctf-nobfd,opcodes,sframe}.{a,la}
%discard_docs

%else
%make tooldir=/usr DESTDIR=%{buildroot} install
rm -fv %{buildroot}/usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a
rm -rf %{buildroot}/usr/share/info/dir

%endif

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
/usr/bin/elfedit
/usr/bin/gp-archive
/usr/bin/gp-collect-app
/usr/bin/gp-display-html
/usr/bin/gp-display-src
/usr/bin/gp-display-text
/usr/bin/gprof
/usr/bin/gprofng
/usr/bin/gprofng-archive
/usr/bin/gprofng-collect-app
/usr/bin/gprofng-display-html
/usr/bin/gprofng-display-src
/usr/bin/gprofng-display-text
/usr/bin/ld
/usr/bin/ld.bfd
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
%shlib /usr/lib/libctf-nobfd.so.0.0.0
/usr/lib/libctf.so
/usr/lib/libctf.so.0
%shlib /usr/lib/libctf.so.0.0.0
/usr/lib/libgprofng.so
/usr/lib/libgprofng.so.0
%shlib /usr/lib/libgprofng.so.0.0.0
/usr/lib/libopcodes-%{version}.so
/usr/lib/libopcodes.so
/usr/lib/libsframe.so
/usr/lib/libsframe.so.1
%shlib /usr/lib/libsframe.so.1.0.0

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*
/usr/share/doc/gprofng

%files man
/usr/share/man/man*/*

%endif

