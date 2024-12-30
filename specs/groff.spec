Name:           groff
Version:        1.23.0
Release:        1%{?dist}
Summary:        Groff formatting system
License:        GPLv3+ and GFDL and BSD and MIT

Source:         https://ftp.gnu.org/gnu/groff/groff-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

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
PAGE=letter ./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
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
/usr/share/doc/groff-%{version}
/usr/share/groff/%{version}
/usr/share/groff/current
/usr/share/groff/site-tmac/man.local
/usr/share/groff/site-tmac/mdoc.local

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*