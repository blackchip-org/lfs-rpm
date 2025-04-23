# lfs

%global source_name XML-Parser
%global name        perl-%{source_name}
%global version     2.47
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Perl module for parsing XML documents
License:        GPL+ or Artistic

Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  expat
BuildRequires:  perl
Suggests:       %{name}-doc = %{version}

%description
This module provides ways to parse XML documents. It is built on top of
XML::Parser::Expat, which is a lower level interface to James Clark's expat
library. Each call to one of the parsing methods creates a new instance of
XML::Parser::Expat which is then used to parse the document. Expat options may
be provided when the XML::Parser object is created. These options are then
passed on to the Expat object on each parse call. They can also be given as
extra arguments to the parse methods, in which case they override options given
at XML::Parser creation time.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
perl Makefile.PL
make %{_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/perl5/%{perl_version}/core_perl/perllocal.pod

#---------------------------------------------------------------------------
%check
make test

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/lib/perl5/%{perl_version}/site_perl

%else
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser.pm
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser
/usr/lib/perl5/%{perl_version}/site_perl/auto/XML/Parser

%files doc
/usr/share/man/man*/*

%endif
