Name:           popt
Version:        1.19
Release:        1%{?dist}
Summary:        C library for parsing command line parameters
License:        MIT

Source0:        http://ftp.rpm.org/popt/releases/popt-1.x/popt-%{version}.tar.gz

%description
Popt is a C library for parsing command line parameters. Popt was heavily
influenced by the getopt() and getopt_long() functions, but it improves on them
by allowing more powerful argument expansion. Popt can parse arbitrary argv[]
style arrays and automatically set variables based on command line arguments.
Popt allows command line arguments to be aliased via configuration files and
includes utility functions for parsing arbitrary strings into argv[] arrays
using shell-like rules.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
./configure --prefix=/usr                       \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/popt.mo

%endif
