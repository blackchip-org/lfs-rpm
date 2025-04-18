# lfs

%global name        flex
%global version     2.6.4
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A tool for generating scanners (text pattern recognizers)
License:        BSD and LGPLv2+

Source0:        https://github.com/westes/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

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

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr \
            --docdir=/usr/share/doc/flex-%{version} \
            --disable-static
%make

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
ln -sv flex   %{buildroot}/usr/bin/lex
ln -sv flex.1 %{buildroot}/usr/share/man/man1/lex.1
%remove_info_dir

%if %{with lfs}
%discard_docs
%discard_locales
%endif

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

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
/usr/include/*
/usr/lib/libfl.so
/usr/lib/libfl.so.2
%shlib /usr/lib/libfl.so.2.0.0

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/flex-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
