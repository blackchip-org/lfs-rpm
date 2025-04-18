Name:           perl-libintl
Version:        1.31
Release:        1%{?dist}
Summary:        Internationalization library for Perl
License:        GPLv3+

Source0:        https://github.com/gflohr/libintl-perl/archive/refs/tags/release-%{version}.tar.gz

Requires:       perl
Suggests:       %{name}-doc = %{version}

%description
The package libintl-perl is an internationalization library for Perl that aims
to be compatible with the Uniforum message translations system as implemented
for example in GNU gettext.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n libintl-perl-release-%{version}

#---------------------------------------------------------------------------
%build
perl Makefile.PL
make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/perl5/%{perl_version}/core_perl/perllocal.pod

#---------------------------------------------------------------------------
%files
/usr/lib/perl5/%{perl_version}/site_perl/Locale/*
/usr/lib/perl5/%{perl_version}/site_perl/auto/Locale/gettext_xs
/usr/lib/perl5/%{perl_version}/site_perl/auto/libintl-perl

%files doc
/usr/share/man/man*/*

