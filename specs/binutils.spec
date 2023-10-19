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


%prep
%setup -q


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
%endif
%make
%lfs_build_end


%install
%lfs_install_begin
cd build
DESTDIR=%{buildroot} %make install
%lfs_install_end


%files
%if %{with lfs_stage1a}
%{lfs_tools_dir}/bin/*
%{lfs_tools_dir}/lib/*
%{lfs_tools_dir}/%{lfs_tgt}/bin/*
%{lfs_tools_dir}/%{lfs_tgt}/lib/*
%endif


