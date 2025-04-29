# lfs

%global name            flex
%global version         2.6.4
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A tool for generating scanners (text pattern recognizers)
License:        BSD and LGPLv2+

Source0:        https://github.com/westes/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

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

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The flex program generates scanners. Scanners are programs which can recognize
lexical patterns in text. Flex takes pairs of regular expressions and C code as
input and generates a C source file as output. The output file is compiled and
linked with a library to produce an executable. The executable searches through
its input for occurrences of the regular expressions. When a match is found, it
executes the corresponding C code. Flex was designed to work with both Yacc and
Bison, and is used by many programs as part of their build process.

You should install flex if you are going to use your system for application
development.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description info
Info documentation for %{name}

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
%if %{with lfs}
./configure --prefix=/usr \
            --docdir=/usr/share/doc/%{name}-%{version} \
            --disable-static

%else
./configure --prefix=/usr \
            --docdir=/usr/share/doc/%{name}-%{version}

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
ln -sv flex   %{buildroot}/usr/bin/lex
ln -sv flex.1 %{buildroot}/usr/share/man/man1/lex.1

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/lib/lib*so*

%else
/usr/bin/flex
/usr/bin/flex++
/usr/bin/lex
/usr/lib/libfl.so.*

%files devel
/usr/include/*.h
/usr/lib/libfl.so

%files doc
/usr/share/doc/flex-%{version}

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libfl.a

%endif
