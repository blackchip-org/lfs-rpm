# lfs

%global name            autoconf
%global version         2.72
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU tool for automatically configuring source code
License:        GPLv2+ and GFDL

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
GNU's Autoconf is a tool for configuring source code and Makefiles. Using
Autoconf, programmers can create portable and configurable packages, since the
person building the package is allowed to specify various configuration
options.

You should install Autoconf if you are developing software and would like to
create shell scripts that configure your source code packages. If you are
installing Autoconf, you will also need to install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who may be
configuring software with an Autoconf-generated script; Autoconf is only
required for the generation of the scripts, not their use.

%if !%{with lfs}
%description info
Info documentation for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
sed -e 's/SECONDS|/&SHLVL|/'               \
    -e '/BASH_ARGV=/a\        /^SHLVL=/ d' \
    -i.orig tests/local.at

./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/share/%{name}

%else
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autom4te
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames
/usr/share/autoconf

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif