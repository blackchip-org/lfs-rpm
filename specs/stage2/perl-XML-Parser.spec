%global version         2.46
%global perl_version    5.38
%global _build_id_links none

Name:           perl-XML-Parser
Version:        %{version}
Release:        1%{?dist}
Summary:        Perl module for parsing XML documents
License:        GPL+ or Artistic

Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-%{version}.tar.gz

%description
This module provides ways to parse XML documents. It is built on top of
XML::Parser::Expat, which is a lower level interface to James Clark's expat
library. Each call to one of the parsing methods creates a new instance of
XML::Parser::Expat which is then used to parse the document. Expat options may
be provided when the XML::Parser object is created. These options are then
passed on to the Expat object on each parse call. They can also be given as
extra arguments to the parse methods, in which case they override options given
at XML::Parser creation time.


%prep
%setup -q -n XML-Parser-%{version}


%build
perl Makefile.PL
make


%check
make test


%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/perl5/%{perl_version}/core_perl/perllocal.pod


%files
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser.pm
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser
/usr/lib/perl5/%{perl_version}/site_perl/auto/XML/Parser
/usr/share/man/man3/*
