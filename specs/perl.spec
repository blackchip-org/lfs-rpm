Name:           perl
Version:        5.38.2
%global         perl_version 5.38
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

#---------------------------------------------------------------------------
%prep
%setup -q


#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
sh Configure -des                                                       \
             -Dprefix=/usr                                              \
             -Dvendorprefix=/usr                                        \
             -Duseshrplib                                               \
             -Dprivlib=/usr/lib/perl5/%{perl_version}/core_perl         \
             -Darchlib=/usr/lib/perl5/%{perl_version}/core_perl         \
             -Dsitelib=/usr/lib/perl5/%{perl_version}/site_perl         \
             -Dsitearch=/usr/lib/perl5/%{perl_version}/site_perl        \
             -Dvendorlib=/usr/lib/perl5/%{perl_version}/vendor_perl     \
             -Dvendorarch=/usr/lib/perl5/%{perl_version}/vendor_perl    \
             -Dman1dir=/usr/share/man/man1                              \
             -Dman3dir=/usr/share/man/man3                              \

%else
export BUILD_ZLIB=False
export BUILD_BZIP2=0
sh Configure -des                                                    \
             -Dprefix=/usr                                           \
             -Dvendorprefix=/usr                                     \
             -Dprivlib=/usr/lib/perl5/%{perl_version}/core_perl      \
             -Darchlib=/usr/lib/perl5/%{perl_version}/core_perl      \
             -Dsitelib=/usr/lib/perl5/%{perl_version}/site_perl      \
             -Dsitearch=/usr/lib/perl5/%{perl_version}/site_perl     \
             -Dvendorlib=/usr/lib/perl5/%{perl_version}/vendor_perl  \
             -Dvendorarch=/usr/lib/perl5/%{perl_version}/vendor_perl \
             -Dman1dir=/usr/share/man/man1                           \
             -Dman3dir=/usr/share/man/man3                           \
             -Dpager="/usr/bin/less -isR"                            \
             -Duseshrplib                                            \
             -Dusethreads

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/lib/rpm/macros.d
cat <<EOF | sed 's/@/%/' > %{buildroot}/usr/lib/rpm/macros.d/macros.perl
@perl_version %{perl_version}
EOF
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
/usr/bin/*
/usr/lib/perl5/%{perl_version}
/usr/lib/rpm/macros.d/macros.perl

%else
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
/usr/lib/perl5/%{perl_version}
/usr/lib/rpm/macros.d/macros.perl
/usr/share/man/man{1,3}/*

%endif