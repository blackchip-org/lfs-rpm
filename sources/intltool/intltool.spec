# lfs

%global name        intltool
%global version     0.51.0
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utility for internationalizing various kinds of data files
License:        GPLv2 with exceptions

Source0:        https://launchpad.net/intltool/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
sed -i 's:\\\${:\\\$\\{:' intltool-update.in
./configure --prefix=/usr
make %{_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
install -v -Dm644 doc/I18N-HOWTO %{buildroot}/usr/share/doc/intltool-%{version}/I18N-HOWTO

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/share/{aclocal,intltool}

%else
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

%endif