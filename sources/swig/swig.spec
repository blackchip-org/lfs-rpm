# dnf

%global name            swig
%global version         4.3.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Simplified Wrapper and Interface Generator
License:        GPLv3+

Source0:        https://github.com/swig/swig/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  pcre2-devel

%description
SWIG is a compiler that integrates C and C++ with languages including Perl,
Python, Tcl, Ruby, PHP, Java, C#, D, Go, Lua, Octave, R, Scheme (Guile,
MzScheme/Racket), Scilab, Ocaml. SWIG can also export its parse tree into XML.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./autogen.sh
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/share/swig

%else
/usr/bin/ccache-swig
/usr/bin/swig
/usr/share/swig/%{version}

%endif
