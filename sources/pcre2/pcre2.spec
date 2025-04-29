# dnf

%global name            pcre2
%global version         10.45
%global release         1
%global so_version      8

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Regular expression pattern matching
License:        BSD

Source0:        https://github.com/PCRE2Project/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The PCRE2 library is a set of C functions that implement regular expression
pattern matching using the same syntax and semantics as Perl 5. PCRE2 has its
own native API, as well as a set of wrapper functions that correspond to the
POSIX regular expression API. The PCRE2 library is free, even for building
proprietary software. It comes in three forms, for processing 8-bit, 16-bit,
or 32-bit code units, in either literal or UTF encoding.

PCRE2 was first released in 2015 to replace the API in the original PCRE
library, which is now obsolete and no longer maintained. As well as a more
flexible API, the code of PCRE2 has been much improved since the fork.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

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
./configure --prefix=/usr
make

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*.h
/usr/lib/lib*.{so*,a}
/usr/lib/pkgconfig

%else
/usr/bin/pcre2-config
/usr/bin/pcre2grep
/usr/bin/pcre2test
/usr/lib/libpcre2-%{so_version}.so.*
/usr/lib/libpcre2-posix.so.*

%files devel
/usr/include/*.h
/usr/lib/libpcre2-%{so_version}.so
/usr/lib/libpcre2-posix.so
/usr/lib/pkgconfig/libpcre2-%{so_version}.pc
/usr/lib/pkgconfig/libpcre2-posix.pc

%files doc
/usr/share/doc/pcre2

%files man
/usr/share/man/man*/*

%files static
/usr/lib/libpcre2-%{so_version}.a
/usr/lib/libpcre2-posix.a

%endif
