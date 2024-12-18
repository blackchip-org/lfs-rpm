Name:           perl
Version:        5.40.0
%global         perl_version 5.40
Release:        1%{?dist}
Summary:        Practical Extraction and Report Language
License:        GPL+ or Artistic

Source0:        https://www.cpan.org/src/5.0/perl-%{version}.tar.xz

# If yes, this calls a perl script to find this information but perl isn't
# installed yet
%if %{with lfs_stage1}
AutoReqProv:    no
%else
AutoReq:        no
%endif

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
%if %{with lfs_stage1}
%use_lfs_tools
unset LC_ALL

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

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
make DESTDIR=%{buildroot} install
%discard_docs

%else
make DESTDIR=%{buildroot} install

%endif
mkdir -p %{buildroot}/usr/lib/rpm/macros.d
cat <<EOF | sed 's/@/%/' > %{buildroot}/usr/lib/rpm/macros.d/macros.perl
@perl_version %{perl_version}
EOF

find \
    %{buildroot}/usr/lib/perl5/%{perl_version} \
    -name "*.so" \
    -exec chmod 755 {} \;

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