Name:           intltool
Version:        0.51.0
Release:        1%{?dist}
Summary:        Utility for internationalizing various kinds of data files
License:        GPLv2 with exceptions

Source0:        https://launchpad.net/intltool/trunk/%{version}/+download/intltool-%{version}.tar.gz

%description
This tool automatically extracts translatable strings from oaf, glade, bonobo
ui, nautilus theme, .desktop, and other data files and puts them in the po
files.

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
/usr/share/doc/intltool-%{version}
/usr/share/intltool
/usr/share/man/man8/*
