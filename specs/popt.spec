# extra

Name:           popt
Version:        1.19
Release:        1%{?dist}
Summary:        C library for parsing command line parameters
License:        MIT

Source:         http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz

%description
Popt is a C library for parsing command line parameters. Popt was heavily
influenced by the getopt() and getopt_long() functions, but it improves on them
by allowing more powerful argument expansion. Popt can parse arbitrary argv[]
style arrays and automatically set variables based on command line arguments.
Popt allows command line arguments to be aliased via configuration files and
includes utility functions for parsing arbitrary strings into argv[] arrays
using shell-like rules.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/libpopt.a

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/popt.mo

%else
/usr/include/*.h
/usr/lib/libpopt.so
/usr/lib/libpopt.so.0
%shlib /usr/lib/libpopt.so.0.0.2
/usr/lib/pkgconfig/popt.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/man/man3/*

%endif
