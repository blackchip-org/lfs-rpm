Name:           elfutils
Version:        0.192
Release:        1%{?dist}
Summary:        A collection of utilities and DSOs to handle ELF files and DWARF data
License:        GPLv2+

Source:         https://sourceware.org/ftp/elfutils/%{version}/elfutils-%{version}.tar.bz2

Suggests:       %{name}-doc = %{version}

%description
Elfutils is a collection of utilities, including stack (to show backtraces), nm
(for listing symbols from object files), size (for listing the section sizes of
an object or archive file), strip (for discarding symbols), readelf (to see the
raw ELF file structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr                \
            --disable-debuginfod         \
            --enable-libdebuginfod=dummy
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
install -d %{buildroot}/usr/lib/pkgconfig
install -vm644 -t %{buildroot}/usr/lib/pkgconfig config/libelf.pc

rm %{buildroot}/usr/lib/*.a

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
/usr/bin/debuginfod-find
/usr/bin/eu-addr2line
/usr/bin/eu-ar
/usr/bin/eu-elfclassify
/usr/bin/eu-elfcmp
/usr/bin/eu-elfcompress
/usr/bin/eu-elflint
/usr/bin/eu-findtextrel
/usr/bin/eu-make-debug-archive
/usr/bin/eu-nm
/usr/bin/eu-objdump
/usr/bin/eu-ranlib
/usr/bin/eu-readelf
/usr/bin/eu-size
/usr/bin/eu-srcfiles
/usr/bin/eu-stack
/usr/bin/eu-strings
/usr/bin/eu-strip
/usr/bin/eu-unstrip
/usr/etc/profile.d/debuginfod.csh
/usr/etc/profile.d/debuginfod.sh
/usr/include/elfutils
/usr/include/*.h
/usr/lib/libasm.so
/usr/lib/libasm.so.1
%shlib /usr/lib/libasm-%{version}.so
/usr/lib/libdebuginfod.so
/usr/lib/libdebuginfod.so.1
%shlib /usr/lib/libdebuginfod-%{version}.so
/usr/lib/libdw.so
/usr/lib/libdw.so.1
%shlib /usr/lib/libdw-%{version}.so
/usr/lib/libelf.so
/usr/lib/libelf.so.1
%shlib /usr/lib/libelf-%{version}.so
/usr/lib/pkgconfig/libelf.pc
/usr/lib/pkgconfig/libdebuginfod.pc
/usr/lib/pkgconfig/libdw.pc
/usr/share/fish/vendor_conf.d/debuginfod.fish

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/man/man*/*
