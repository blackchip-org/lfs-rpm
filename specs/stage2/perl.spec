%global version         5.38.0
%global version2        5.38
%global _build_id_links none

Name:           perl
Version:        %{version}
Release:        1%{?dist}
Summary:        Practical Extraction and Report Language
License:        GPL+ or Artistic

Source0:        https://www.cpan.org/src/5.0/perl-%{version}.tar.xz

%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting. Perl is good at handling processes and files, and is especially good
at handling text. Perl's hallmarks are practicality and efficiency. While it is
used to do a lot of different things, Perl's most common applications are
system administration utilities and web programming.

This is a metapackage with all the Perl bits and core modules that can be found
in the upstream tarball from perl.org.

If you need only a specific feature, you can install a specific package
instead. E.g. to handle Perl scripts with /usr/bin/perl interpreter, install
perl-interpreter package. See perl-interpreter description for more details on
the Perl decomposition into packages.


%prep
%setup -q


%build
export BUILD_ZLIB=False
export BUILD_BZIP2=0

sh Configure -des                                                \
             -Dprefix=/usr                                       \
             -Dvendorprefix=/usr                                 \
             -Dprivlib=/usr/lib/perl5/%{version2}/core_perl      \
             -Darchlib=/usr/lib/perl5/%{version2}/core_perl      \
             -Dsitelib=/usr/lib/perl5/%{version2}/site_perl      \
             -Dsitearch=/usr/lib/perl5/%{version2}/site_perl     \
             -Dvendorlib=/usr/lib/perl5/%{version2}/vendor_perl  \
             -Dvendorarch=/usr/lib/perl5/%{version2}/vendor_perl \
             -Dman1dir=/usr/share/man/man1                       \
             -Dman3dir=/usr/share/man/man3                       \
             -Dpager="/usr/bin/less -isR"                        \
             -Duseshrplib                                        \
             -Dusethreads
make


%check
make test


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/corelist
/usr/bin/cpan
/usr/bin/enc2xs
/usr/bin/encguess
/usr/bin/h2ph
/usr/bin/h2xs
/usr/bin/instmodsh
/usr/bin/json_pp
/usr/bin/libnetcfg
/usr/bin/perl
/usr/bin/perl%{version}
/usr/bin/perlbug
/usr/bin/perldoc
/usr/bin/perlivp
/usr/bin/perlthanks
/usr/bin/piconv
/usr/bin/pl2pm
/usr/bin/pod2html
/usr/bin/pod2man
/usr/bin/pod2text
/usr/bin/pod2usage
/usr/bin/podchecker
/usr/bin/prove
/usr/bin/ptar
/usr/bin/ptardiff
/usr/bin/ptargrep
/usr/bin/shasum
/usr/bin/splain
/usr/bin/streamzip
/usr/bin/xsubpp
/usr/bin/zipdetails
/usr/lib/perl5/%{version2}
/usr/share/man/man{1,3}/*
