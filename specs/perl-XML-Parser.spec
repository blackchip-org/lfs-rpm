Name:           perl-XML-Parser
Version:        2.47
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

#---------------------------------------------------------------------------
%prep
%setup -q -n XML-Parser-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

perl Makefile.PL
make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/perl5/%{perl_version}/core_perl/perllocal.pod
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
%files
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser.pm
/usr/lib/perl5/%{perl_version}/site_perl/XML/Parser
/usr/lib/perl5/%{perl_version}/site_perl/auto/XML/Parser
/usr/share/man/man3/*