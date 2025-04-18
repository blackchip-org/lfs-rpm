Name:           autoconf
Version:        2.72
Release:        1%{?dist}
Summary:        A GNU tool for automatically configuring source code
License:        GPLv2+ and GFDL

Source0:        https://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

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

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
sed -e 's/SECONDS|/&SHLVL|/'               \
    -e '/BASH_ARGV=/a\        /^SHLVL=/ d' \
    -i.orig tests/local.at

./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/autoconf
/usr/bin/autoheader
/usr/bin/autom4te
/usr/bin/autoreconf
/usr/bin/autoscan
/usr/bin/autoupdate
/usr/bin/ifnames
/usr/share/autoconf

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*
