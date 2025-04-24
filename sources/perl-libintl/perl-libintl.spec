# beyond

%global name            perl-libintl
%global version         1.31
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Internationalization library for Perl
License:        GPLv3+

Source0:        https://github.com/gflohr/libintl-perl/archive/refs/tags/release-%{version}.tar.gz
Source1:        %{name}.sha256

Requires:       perl
BuildRequires:  perl
Recommends:     %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description
The package libintl-perl is an internationalization library for Perl that aims
to be compatible with the Uniforum message translations system as implemented
for example in GNU gettext.

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n libintl-perl-release-%{version}

#---------------------------------------------------------------------------
%build
perl Makefile.PL
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/lib/perl5/%{perl_version}/core_perl/perllocal.pod
/usr/lib/perl5/%{perl_version}/site_perl/Locale
/usr/lib/perl5/%{perl_version}/site_perl/auto/Locale/gettext_xs
/usr/lib/perl5/%{perl_version}/site_perl/auto/libintl-perl

%files doc
/usr/share/man/man*

