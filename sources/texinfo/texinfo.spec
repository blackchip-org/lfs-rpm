# lfs

%global name        texinfo
%global version     7.2
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Programs for reading, writing, and converting info pages
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  perl-libintl

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
Texinfo uses a single source file to produce output in a number of formats,
both online and printed (HTML, PDF, DVI, Info, DocBook, LaTeX, EPUB 3). This
means that instead of writing different documents for online information and
another for a printed manual, you need write only one document. The Texinfo
system is well-integrated with GNU Emacs.

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr

%else
./configure --prefix=/usr       \
            --with-external-libintl
%endif

make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/lib/texi2any
/usr/share/texi2any
/usr/share/%{name}

%else
/usr/bin/info
/usr/bin/install-info
/usr/bin/makeinfo
/usr/bin/pdftexi2dvi
/usr/bin/pod2texi
/usr/bin/texi2any
/usr/bin/texi2dvi
/usr/bin/texi2pdf
/usr/bin/texindex
/usr/lib/texi2any/ConvertXS.so
/usr/lib/texi2any/DocumentXS.so
/usr/lib/texi2any/IndicesXS.so
/usr/lib/texi2any/MiscXS.so
/usr/lib/texi2any/Parsetexi.so
/usr/lib/texi2any/StructuringTransfoXS.so
/usr/lib/texi2any/XSParagraph.so
/usr/lib/texi2any/libtexinfo-convert.so.*
/usr/lib/texi2any/libtexinfo-convertxs.*
/usr/lib/texi2any/libtexinfo.so.*
/usr/lib/texi2any/libtexinfoxs.so.*
/usr/share/texi2any
/usr/share/texinfo

%files devel
/usr/lib/texi2any/libtexinfo-convert.so
/usr/lib/texi2any/libtexinfo-convertxs.so
/usr/lib/texi2any/libtexinfo.so
/usr/lib/texi2any/libtexinfoxs.so

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif