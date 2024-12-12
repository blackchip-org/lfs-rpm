Name:           texinfo
Version:        7.1
Release:        1%{?dist}
Summary:        Programs for reading, writing, and converting info pages
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz


%description
Texinfo uses a single source file to produce output in a number of formats,
both online and printed (HTML, PDF, DVI, Info, DocBook, LaTeX, EPUB 3). This
means that instead of writing different documents for online information and
another for a printed manual, you need write only one document. The Texinfo
system is well-integrated with GNU Emacs.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%post
%{?update_info_dir}

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
/usr/lib/texinfo/MiscXS.so
/usr/lib/texinfo/Parsetexi.so
/usr/lib/texinfo/XSParagraph.so
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/texinfo

%if %{without lfs_stage1}
/usr/share/info/*
/usr/share/man/man{1,5}/*

%endif