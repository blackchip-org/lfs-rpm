Name:           swig
Version:        4.3.0
Release:        1%{?dist}
Summary:        Simplified Wrapper and Interface Generator
License:        GPLv3+

Source:         https://github.com/swig/swig/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  pcre2

%description
SWIG is a compiler that integrates C and C++ with languages including Perl,
Python, Tcl, Ruby, PHP, Java, C#, D, Go, Lua, Octave, R, Scheme (Guile,
MzScheme/Racket), Scilab, Ocaml. SWIG can also export its parse tree into XML.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./autogen.sh
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/bin/ccache-swig
/usr/bin/swig
/usr/share/swig/%{version}
