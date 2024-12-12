Name:           expat
Version:        2.6.4
Release:        1%{?dist}
Summary:        An XML parser library
License:        MIT

Source0:        https://prdownloads.sourceforge.net/expat/expat-%{version}.tar.xz


%description
This is expat, the C library for parsing XML, written by James Clark. Expat is
a stream oriented XML parser. This means that you register handlers with the
parser prior to starting the parse. These handlers are called when the parser
discovers the associated structures in the document being parsed. A start tag
is an example of the kind of structures for which you may register handlers.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/expat-%{version}
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
install -v -m644 -t %{buildroot}/usr/share/doc/expat-%{version} doc/*.{html,css}
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
/usr/bin/xmlwf
/usr/include/*.h
/usr/lib/cmake/expat-%{version}
/usr/lib/libexpat.so
/usr/lib/libexpat.so.1
/usr/lib/pkgconfig/expat.pc
/usr/share/doc/expat-%{version}
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libexpat.so.1.*
