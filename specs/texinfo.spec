Name:           texinfo
Version:        7.2
Release:        1%{?dist}
Summary:        Programs for reading, writing, and converting info pages
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz

BuildRequires:  perl-libintl

%description
Texinfo uses a single source file to produce output in a number of formats,
both online and printed (HTML, PDF, DVI, Info, DocBook, LaTeX, EPUB 3). This
means that instead of writing different documents for online information and
another for a printed manual, you need write only one document. The Texinfo
system is well-integrated with GNU Emacs.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr

%else
./configure --prefix=/usr       \
            --with-external-libintl
%endif

%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/info
/usr/bin/install-info
/usr/bin/makeinfo
/usr/bin/pdftexi2dvi
/usr/bin/pod2texi
/usr/bin/texi2any
/usr/bin/texi2dvi
/usr/bin/texi2pdf
/usr/bin/texindex
%shlib /usr/lib/texi2any/ConvertXS.so
%shlib /usr/lib/texi2any/DocumentXS.so
%shlib /usr/lib/texi2any/IndicesXS.so
%shlib /usr/lib/texi2any/MiscXS.so
%shlib /usr/lib/texi2any/Parsetexi.so
%shlib /usr/lib/texi2any/StructuringTransfoXS.so
%shlib /usr/lib/texi2any/XSParagraph.so
/usr/lib/texi2any/libtexinfo-convert.so
/usr/lib/texi2any/libtexinfo-convert.so.0
%shlib /usr/lib/texi2any/libtexinfo-convert.so.0.0.0
/usr/lib/texi2any/libtexinfo-convertxs.so
/usr/lib/texi2any/libtexinfo-convertxs.so.0
%shlib /usr/lib/texi2any/libtexinfo-convertxs.so.0.0.0
/usr/lib/texi2any/libtexinfo.so
/usr/lib/texi2any/libtexinfo.so.0
%shlib /usr/lib/texi2any/libtexinfo.so.0.0.0
/usr/lib/texi2any/libtexinfoxs.so
/usr/lib/texi2any/libtexinfoxs.so.0
%shlib /usr/lib/texi2any/libtexinfoxs.so.0.0.0
/usr/share/texi2any
/usr/share/texinfo

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*
