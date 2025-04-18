Name:           perl-XML-Parser
Version:        2.47
Release:        1%{?dist}
Summary:        Perl module for parsing XML documents
License:        GPL+ or Artistic

Source:         https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-%{version}.tar.gz

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
%setup -q -n XML-Parser-%{version}

#---------------------------------------------------------------------------
%build
perl Makefile.PL
make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/perl5/%{perl_version}/core_perl/perllocal.pod

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
%files
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser.pm
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser
/usr/lib/perl5/%{perl_version}/site_perl/auto/XML/Parser

%files doc
/usr/share/man/man*/*