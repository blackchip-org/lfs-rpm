# lfs

%global name            groff
%global version         1.23.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Groff formatting system
License:        GPLv3+ and GFDL and BSD and MIT

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  perl

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
groff (GNU roff) is a typesetting system that reads plain text input files that
include formatting commands to produce output in PostScript, PDF, HTML, or DVI
formats or for display to a terminal. Formatting commands can be low-level
typesetting primitives, macros from a supplied package, or user-defined macros.
All three approaches can be combined.

A reimplementation and extension of the typesetter from AT&T Unix, groff is
present on most POSIX systems owing to its long association with Unix manuals
(including man pages). It and its predecessor are notable for their production
of several best-selling software engineering texts. groff is capable of
producing typographically sophisticated documents while consuming minimal
system resources.

%if !%{with lfs}
%description doc
Documentation for %{name}

%description info
Info documentation for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
PAGE=letter ./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/share/%{name}

%else
/usr/bin/addftinfo
/usr/bin/afmtodit
/usr/bin/chem
/usr/bin/eqn
/usr/bin/eqn2graph
/usr/bin/gdiffmk
/usr/bin/glilypond
/usr/bin/gperl
/usr/bin/gpinyin
/usr/bin/grap2graph
/usr/bin/grn
/usr/bin/grodvi
/usr/bin/groff
/usr/bin/grog
/usr/bin/grolbp
/usr/bin/grolj4
/usr/bin/gropdf
/usr/bin/grops
/usr/bin/grotty
/usr/bin/hpftodit
/usr/bin/indxbib
/usr/bin/lkbib
/usr/bin/lookbib
/usr/bin/mmroff
/usr/bin/neqn
/usr/bin/nroff
/usr/bin/pdfmom
/usr/bin/pdfroff
/usr/bin/pfbtops
/usr/bin/pic
/usr/bin/pic2graph
/usr/bin/post-grohtml
/usr/bin/pre-grohtml
/usr/bin/preconv
/usr/bin/refer
/usr/bin/soelim
/usr/bin/tbl
/usr/bin/tfmtodit
/usr/bin/troff
/usr/share/%{name}/%{version}
/usr/share/%{name}/current
/usr/share/%{name}/site-tmac

%files doc
/usr/share/doc/%{name}-%{version}

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif