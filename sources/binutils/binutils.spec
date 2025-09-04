# lfs

%global name            binutils
%global version         2.45
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU collection of binary utilities
License:        GPLv3+

Source0:        https://sourceware.org/pub/%{name}/releases/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

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

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir -p    build
cd          build

%if %{with lfs_stage1a}
../configure --prefix=%{lfs_tools_dir}  \
             --with-sysroot=%{lfs_dir}  \
             --target=%{lfs_tgt}        \
             --disable-nls              \
             --enable-gprofng=no        \
             --disable-werror           \
             --enable-new-dtags         \
             --enable-default-hash-style=gnu
make %{?_smp_mflags}

%elif %{with lfs_stage1b}
sed '6031s/$add_dir//' -i ../ltmain.sh
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
make %{?_smp_mflags}

%else
../configure --prefix=/usr       \
             --sysconfdir=/etc   \
             --enable-ld=default \
             --enable-plugins    \
             --enable-shared     \
             --disable-werror    \
             --enable-64-bit-bfd \
             --enable-new-dtags  \
             --with-system-zlib  \
             --enable-default-hash-style=gnu
make %{?_smp_mflags} tooldir=/usr

%endif

#---------------------------------------------------------------------------
%install
cd build

%if %{with lfs_stage1a}
DESTDIR=%{buildroot} make install

%elif %{with lfs_stage1b}
DESTDIR=%{buildroot}/%{lfs_dir} make install

%else
make tooldir=/usr DESTDIR=%{buildroot} install

%endif

rm -fv %{buildroot}/%{?lfs_dir}/usr/lib/lib{bfd,ctf,ctf-nobfd,gprofng,opcodes,sframe}.a

#---------------------------------------------------------------------------
%check
cd build
make -k check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1a}
%{lfs_tools_dir}/bin
%{lfs_tools_dir}/lib
%{lfs_tools_dir}/%{lfs_tgt}/bin
%{lfs_tools_dir}/%{lfs_tgt}/lib

%elif %{with lfs}
%{?lfs_dir}/usr/bin
%{?lfs_dir}/usr/include
%{?lfs_dir}/usr/lib
%if %{with lfs_stage1b}
%{?lfs_dir}/usr/%{lfs_tgt}/bin
%{?lfs_dir}/usr/%{lfs_tgt}/lib/ldscripts
%else
%{?lfs_dir}/etc
%endif

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
/usr/lib/bfd-plugins/*
/usr/lib/gprofng
/usr/lib/ldscripts
/usr/lib/libbfd-%{version}.so
/usr/lib/libctf-nobfd.so.*
/usr/lib/libctf.so.*
/usr/lib/libgprofng.so.*
/usr/lib/libopcodes-%{version}.so
/usr/lib/libsframe.so.*

%files devel
/usr/include/*.h
/usr/lib/libbfd.so
/usr/lib/libctf-nobfd.so
/usr/lib/libctf.so
/usr/lib/libgprofng.so
/usr/lib/libopcodes.so
/usr/lib/libsframe.so

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%endif

