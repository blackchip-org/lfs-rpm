# lfs

%global name            expat
%global version         2.7.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        An XML parser library
License:        MIT

Source0:        https://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
This is expat, the C library for parsing XML, written by James Clark. Expat is
a stream oriented XML parser. This means that you register handlers with the
parser prior to starting the parse. These handlers are called when the parser
discovers the associated structures in the document being parsed. A start tag
is an example of the kind of structures for which you may register handlers.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs}
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/%{name}-%{version}

%else
./configure --prefix=/usr    \
            --docdir=/usr/share/doc/%{name}-%{version}

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
install -v -m644 -t %{buildroot}/usr/share/doc/%{name}-%{version} doc/*.{html,css}

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
/usr/lib/libexpat.so.*

%files devel
/usr/include/*.h
/usr/lib/cmake/expat-%{version}
/usr/lib/libexpat.so
/usr/lib/pkgconfig/%{name}.pc

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libexpat.a

%endif
