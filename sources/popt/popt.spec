# rpm

%global name            popt
%global version         1.19
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        C library for parsing command line parameters
License:        MIT

Source0:        http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
Popt is a C library for parsing command line parameters. Popt was heavily
influenced by the getopt() and getopt_long() functions, but it improves on them
by allowing more powerful argument expansion. Popt can parse arbitrary argv[]
style arrays and automatically set variables based on command line arguments.
Popt allows command line arguments to be aliased via configuration files and
includes utility functions for parsing arbitrary strings into argv[] arrays
using shell-like rules.

%if !%{with lfs}
%description devel
Development files for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*

%else
/usr/lib/libpopt.so.*

%files devel
/usr/include/*.h
/usr/lib/libpopt.so
/usr/lib/pkgconfig/popt.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man3/*.gz

%files static
/usr/lib/libpopt.a

%endif
