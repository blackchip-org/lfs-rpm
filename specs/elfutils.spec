Name:           elfutils
Version:        0.189
Release:        1%{?dist}
Summary:        A collection of utilities and DSOs to handle ELF files and DWARF data
License:        GPLv2+

Source0:        https://sourceware.org/ftp/elfutils/%{version}/elfutils-%{version}.tar.bz2

%description
Elfutils is a collection of utilities, including stack (to show backtraces), nm
(for listing symbols from object files), size (for listing the section sizes of
an object or archive file), strip (for discarding symbols), readelf (to see the
raw ELF file structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=x86_64-pc-linux-gnu           \
            --disable-demangler                   \
            --disable-libdebuginfod               \
            --disable-debuginfod

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*.h
%{lfs_dir}/usr/include/elfutils
%{lfs_dir}/usr/lib/*.{a,so*}
%{lfs_dir}/usr/lib/pkgconfig/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/elfutils.mo

%endif
