# extra

Name:           libxml2
Version:        2.13.6
%global         version2 2.13
Release:        1%{?dist}
Summary:        XML C parser and toolkit developed for the GNOME project
License:        MIT

Source:         https://download.gnome.org/sources/libxml2/%{version2}/libxml2-%{version}.tar.xz

BuildRequires:  pkg-config
BuildRequires:  python
Suggests:       %{name}-doc = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Recommends:     %{name}-man = %{version}

%description
Libxml2 is the XML C parser and toolkit developed for the GNOME project
(but usable outside of the GNOME platform), it is free software available
under the MIT License. XML itself is a metalanguage to design markup languages,
i.e. text language where semantic and structure are added to the content using
extra "markup" information enclosed between angle brackets. HTML is the most
well-known markup language. Though the library is written in C a variety of
language bindings make it available in other environments.

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/lib/%{python_version}/__pycache__

#---------------------------------------------------------------------------
%files
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint
/usr/include/%{name}
/usr/lib/python%{python_version}/site-packages/*
/usr/share/aclocal/libxml.m4
/usr/lib/cmake/%{name}
/usr/lib/libxml2.so
/usr/lib/libxml2.so.2
%shlib /usr/lib/libxml2.so.2.13.6
/usr/lib/pkgconfig/libxml-2.0.pc

%files doc
/usr/share/doc/%{name}
/usr/share/gtk-doc/html/%{name}

%files man
/usr/share/man/man*/*

