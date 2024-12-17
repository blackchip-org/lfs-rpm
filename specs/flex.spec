Name:           flex
Version:        2.6.4
Release:        1%{?dist}
Summary:        A tool for generating scanners (text pattern recognizers)
License:        BSD and LGPLv2+

Source0:        https://github.com/westes/flex/releases/download/v%{version}/flex-%{version}.tar.gz

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

#---------------------------------------------------------------------------
%prep
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

#---------------------------------------------------------------------------
%post
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/flex
/usr/bin/flex++
/usr/bin/lex
/usr/include/*
/usr/lib/libfl.so
/usr/lib/libfl.so.2
/usr/share/doc/flex-%{version}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/flex.mo
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libfl.so.2.0.0
