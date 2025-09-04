# lfs

%global name            elfutils
%global version         0.193
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A collection of utilities and DSOs to handle ELF files and DWARF data
License:        GPLv2+

Source0:        https://sourceware.org/ftp/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}.sha256

BuildRequires:  pkgconf

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
Elfutils is a collection of utilities, including stack (to show backtraces), nm
(for listing symbols from object files), size (for listing the section sizes of
an object or archive file), strip (for discarding symbols), readelf (to see the
raw ELF file structures), elflint (to check for well-formed ELF files) and
elfcompress (to compress or decompress ELF sections).

%if !%{with lfs}
%description devel
Development files for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr                \
            --disable-debuginfod         \
            --enable-libdebuginfod=dummy
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}/usr/lib/pkgconfig
install -vm644 -t %{buildroot}/usr/lib/pkgconfig config/libelf.pc
\
%if %{with lfs}
rm -rf %{buildroot}/usr/etc
rm -rf %{buildroot}/usr/share
rm     %{buildroot}/usr/lib/*.a
%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
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
/usr/lib/libasm.so.*
/usr/lib/libasm-%{version}.so
/usr/lib/libdebuginfod.so.*
/usr/lib/libdebuginfod-%{version}.so
/usr/lib/libdw.so.*
/usr/lib/libdw-%{version}.so
/usr/lib/libelf.so.*
/usr/lib/libelf-%{version}.so
/usr/share/fish/vendor_conf.d/debuginfod.fish

%files devel
/usr/include/*.h
/usr/include/%{name}
/usr/lib/libasm.so
/usr/lib/libdebuginfod.so
/usr/lib/libdw.so
/usr/lib/libelf.so
/usr/lib/pkgconfig/libelf.pc
/usr/lib/pkgconfig/libdebuginfod.pc
/usr/lib/pkgconfig/libdw.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libasm.a
/usr/lib/libdw.a
/usr/lib/libelf.a

%endif