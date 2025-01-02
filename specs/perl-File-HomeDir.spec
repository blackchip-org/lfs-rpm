Name:           perl-File-HomeDir
Version:        1.006
Release:        1%{?dist}
Summary:        Find your home and other directories on any platform
License:        GPLv2+

Source:        https://github.com/perl5-utils/File-HomeDir/archive/refs/tags/%{version}.tar.gz

BuildRequires:  perl
Suggests:       %{name}-doc = %{version}

%description
File::HomeDir is a module for locating the directories that are "owned" by a
user (typically your user) and to solve the various issues that arise trying to
find them consistently across a wide variety of platforms.

The end result is a single API that can find your resources on any platform,
making it relatively trivial to create Perl software that works elegantly and
correctly no matter where you run it.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n File-HomeDir-%{version}

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
/usr/lib/perl5/%{perl_version}/site_perl/File/HomeDir{,.pm}
/usr/lib/perl5/%{perl_version}/site_perl/auto/File/HomeDir

%files doc
/usr/share/man/man*/*