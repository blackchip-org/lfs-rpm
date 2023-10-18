%global version         0.189
%global _build_id_links none

Name:           elfutils
Version:        %{version}
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


%prep
%setup -q


%build
./configure --prefix=/usr                \
            --disable-debuginfod         \
            --enable-libdebuginfod=dummy
make


%check
make check


%install
make -C libelf DESTDIR=%{buildroot} install
install -d %{buildroot}/usr/lib/pkgconfig
install -vm644 -t %{buildroot}/usr/lib/pkgconfig config/libelf.pc
rm %{buildroot}/usr/lib/libelf.a


%files
/usr/include/elfutils
/usr/include/*.h
/usr/lib/libelf.so
/usr/lib/libelf.so.1
/usr/lib/pkgconfig/libelf.pc

%defattr(755,root,root,755)
/usr/lib/libelf-%{version}.so
