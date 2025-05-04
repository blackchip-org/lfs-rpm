# beyond

%global source_name     File-Which
%global name            perl-%{source_name}
%global version         1.27
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Perl implementation of the which utility as an API
License:        GPLv2+

Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  perl

Recommends:     %{name}-man  = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%description
File::Which finds the full or relative paths to executable programs on the
system. This is normally the function of which utility. which is typically
implemented as either a program or a built in shell command. On some platforms,
such as Microsoft Windows it is not provided as part of the core operating
system. This module provides a consistent API to this functionality regardless
of the underlying platform.

The focus of this module is correctness and portability. As a consequence
platforms where the current directory is implicitly part of the search path
such as Microsoft Windows will find executables in the current directory,
whereas on platforms such as UNIX where this is not the case executables in
the current directory will only be found if the current directory is explicitly
added to the path.

If you need a portable which on the command line in an environment that does
not provide it, install App::pwhich which provides a command line interface
to this API.

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
/usr/lib/perl5/%{perl_version}/site_perl/File/Which{,.pm}
/usr/lib/perl5/%{perl_version}/site_perl/auto/File/Which

%files man
/usr/share/man/man*/*