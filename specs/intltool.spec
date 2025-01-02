Name:           intltool
Version:        0.51.0
Release:        1%{?dist}
Summary:        Utility for internationalizing various kinds of data files
License:        GPLv2 with exceptions

Source:         https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz

BuildRequires:  perl-XML-Parser
Suggests:       %{name}-doc = %{version}

%description
This tool automatically extracts translatable strings from oaf, glade, bonobo
ui, nautilus theme, .desktop, and other data files and puts them in the po
files.

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
sed -i 's:\\\${:\\\$\\{:' intltool-update.in
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
install -v -Dm644 doc/I18N-HOWTO %{buildroot}/usr/share/doc/intltool-%{version}/I18N-HOWTO

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
/usr/bin/intltool-extract
/usr/bin/intltool-merge
/usr/bin/intltool-prepare
/usr/bin/intltool-update
/usr/bin/intltoolize
/usr/share/aclocal/*
/usr/share/intltool

%files doc
/usr/share/doc/intltool-%{version}

%files man
/usr/share/man/man*/*
