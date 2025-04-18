Name:           perl-File-Which
Version:        1.27
Release:        1%{?dist}
Summary:        Which
License:        GPLv2+

Source:         https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Which-%{version}.tar.gz

BuildRequires:  perl
Suggests:       %{name}-doc = %{version}

%description
Which

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n File-Which-%{version}

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
/usr/lib/perl5/%{perl_version}/site_perl/File/Which{,.pm}
/usr/lib/perl5/%{perl_version}/site_perl/auto/File/Which

%files doc
/usr/share/man/man*/*