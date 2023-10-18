%global version         2.5.0
%global _build_id_links none

Name:           expat
Version:        %{version}
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


%prep
%setup -q


%build
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/expat-%{version}
make


%check
make check


%install
make DESTDIR=%{buildroot} install
install -v -m644 -t %{buildroot}/usr/share/doc/expat-%{version} doc/*.{html,css}

%files
/usr/bin/xmlwf
/usr/include/*.h
/usr/lib/cmake/expat-%{version}
/usr/lib/libexpat.so
/usr/lib/libexpat.so.1
/usr/lib/pkgconfig/expat.pc
/usr/share/doc/expat-%{version}

%defattr(755,root,root,755)
/usr/lib/libexpat.so.1.8.10
