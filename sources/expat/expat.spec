# lfs

%global name        expat
%global version     2.7.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        An XML parser library
License:        MIT

Source0:        https://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
This is expat, the C library for parsing XML, written by James Clark. Expat is
a stream oriented XML parser. This means that you register handlers with the
parser prior to starting the parse. These handlers are called when the parser
discovers the associated structures in the document being parsed. A start tag
is an example of the kind of structures for which you may register handlers.

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/expat-%{version}
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
install -v -m644 -t %{buildroot}/usr/share/doc/expat-%{version} doc/*.{html,css}

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include
/usr/lib/cmake/expat-%{version}
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/bin/xmlwf
/usr/include/*.h
/usr/lib/cmake/expat-%{version}
/usr/lib/libexpat.so
/usr/lib/libexpat.so.1
%shlib /usr/lib/libexpat.so.1.10.2
/usr/lib/pkgconfig/expat.pc

%files doc
/usr/share/doc/expat-%{version}

%files man
/usr/share/man/man*/*

%endif
