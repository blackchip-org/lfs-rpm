# extra

Name:           pcre2
Version:        10.45
Release:        1%{?dist}
Summary:        Regular expression pattern matching
License:        BSD

Source:         https://github.com/PCRE2Project/pcre2/releases/download/pcre2-%{version}/pcre2-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

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

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/bin/pcre2-config
/usr/bin/pcre2grep
/usr/bin/pcre2test
/usr/include/*
/usr/lib/libpcre2-8.a
/usr/lib/libpcre2-8.so
/usr/lib/libpcre2-8.so.0
%shlib /usr/lib/libpcre2-8.so.0.14.0
/usr/lib/libpcre2-posix.a
/usr/lib/libpcre2-posix.so
/usr/lib/libpcre2-posix.so.3
%shlib /usr/lib/libpcre2-posix.so.3.0.6
/usr/lib/pkgconfig/libpcre2-8.pc
/usr/lib/pkgconfig/libpcre2-posix.pc

%files doc
/usr/share/doc/pcre2

%files man
/usr/share/man/man*/*
