Name:           binutils
Version:        2.41
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
             --disable-werror

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

%endif
%make
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

%endif
%lfs_install_end

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

%endif

