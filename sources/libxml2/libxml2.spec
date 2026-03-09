# dnf - blfs

%global name            libxml2
%global version_2       2.15
%global version         %{version_2}.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        XML C parser and toolkit developed for the GNOME project
License:        MIT

Source0:        https://download.gnome.org/sources/%{name}/%{version_2}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  pkgconf
BuildRequires:  python-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%endif

%description
Libxml2 is the XML C parser and toolkit developed for the GNOME project
(but usable outside of the GNOME platform), it is free software available
under the MIT License. XML itself is a metalanguage to design markup languages,
i.e. text language where semantic and structure are added to the content using
extra "markup" information enclosed between angle brackets. HTML is the most
well-known markup language. Though the library is written in C a variety of
language bindings make it available in other environments.

%if !%{with lfs}
%description devel
Development files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/lib/%{python_version}/__pycache__

%if %{with lfs}
rm -rf %{buildroot}/usr/share/gtk-doc
%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/%{name}
/usr/lib/cmake/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint
/usr/lib/libxml2.so.*

%files devel
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/libxml2.so
/usr/lib/pkgconfig/libxml-2.0.pc

%endif

