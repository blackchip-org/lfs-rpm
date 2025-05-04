# beyond

%global source_name     File-HomeDir
%global name            perl-%{source_name}
%global version         1.006
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Find your home and other directories on any platform
License:        GPLv2+

Source0:        https://github.com/perl5-utils/%{source_name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

BuildArch:      noarch

BuildRequires:  perl

Recommends:     %{name}-man  = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%description
File::HomeDir is a module for locating the directories that are "owned" by a
user (typically your user) and to solve the various issues that arise trying to
find them consistently across a wide variety of platforms.

The end result is a single API that can find your resources on any platform,
making it relatively trivial to create Perl software that works elegantly and
correctly no matter where you run it.

%description man
Manual pages for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

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

%files man
/usr/share/man/man*/*.gz

