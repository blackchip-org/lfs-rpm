# lfs

%global name            perl
%global major_name      perl5
%global perl_version    5.40
%global version         %{perl_version}.1
%global smash_version   5.00401
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Practical Extraction and Report Language
License:        GPL+ or Artistic

Source0:        https://www.cpan.org/src/5.0/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Requires:       less
Requires:       libxcrypt

Provides:       perl = %smash_version
Provides:       perl = 1:%{version}

# If yes, this calls a perl script to find this information but perl isn't
# installed yet
%if %{with lfs_stage1}
AutoReqProv:    no
%endif

%if !%{with lfs}
Recommends:     %{name}-doc = %{version}
Recommends:     %{name}-man = %{version}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%man_package

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

%if !%{with lfs}
%description doc
Documentation for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
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
             -Dman1dir=none                                             \
             -Dman3dir=none

%elif %{with lfs}
#export BUILD_ZLIB=False
#export BUILD_BZIP2=0

sh Configure -des                                                    \
             -Dprefix=/usr                                           \
             -Dvendorprefix=/usr                                     \
             -Dprivlib=/usr/lib/perl5/%{perl_version}/core_perl      \
             -Darchlib=/usr/lib/perl5/%{perl_version}/core_perl      \
             -Dsitelib=/usr/lib/perl5/%{perl_version}/site_perl      \
             -Dsitearch=/usr/lib/perl5/%{perl_version}/site_perl     \
             -Dvendorlib=/usr/lib/perl5/%{perl_version}/vendor_perl  \
             -Dvendorarch=/usr/lib/perl5/%{perl_version}/vendor_perl \
             -Dman1dir=none                                          \
             -Dman3dir=none                                          \
             -Dpager="/usr/bin/less -isR"                            \
             -Duseshrplib                                            \
             -Dusethreads

%else
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
             -Dusethreads                                            \
             -Dusershrplib

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/lib/rpm/macros.d
cat <<EOF | sed 's/@/%/' > %{buildroot}/usr/lib/rpm/macros.d/macros.perl
@perl_version %{perl_version}
EOF

find \
    %{buildroot}/usr/lib/%{major_name}/%{perl_version} \
    -name "*.so" \
    -exec chmod 755 {} \;

pushd %{buildroot}

find usr/lib/%{major_name}/%{perl_version} -type f \
    | grep -v .pod \
    | grep -v libperl.so \
    | sed 's_^usr_/usr_' \
    > %{_builddir}/files-lib.txt

find usr/lib/%{major_name}/%{perl_version} -type f \
    | grep .pod \
    | sed 's_^usr_/usr_' \
    > %{_builddir}/files-doc.txt

popd

#---------------------------------------------------------------------------
%check
make test

#---------------------------------------------------------------------------
%files -f %{_builddir}/files-lib.txt
%if %{with lfs}
/usr/bin/*
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

%files devel
/usr/lib/%{major_name}/%{perl_version}/core_perl/CORE/libperl.so
/usr/lib/rpm/macros.d/macros.perl

%files doc -f %{_builddir}/files-doc.txt

%endif
