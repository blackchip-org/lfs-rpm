# deprecated

Name:           pkg-config
Version:        0.29.2
Release:        1%{?dist}
Summary:        Helper tool used when compiling applications and libraries
License:        GPLv2+

Source:         https://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

#FIXME: See below
#BuildRequires:  glib

%description
pkg-config is a helper tool used when compiling applications and libraries. It
helps you insert the correct compiler options on the command line so an
application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
for instance, rather than hard-coding values on where to find glib (or other
libraries). It is language-agnostic, so it can be used for defining the
location of documentation tools, for instance.

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
%if %{with lfs_stage1}
%use_lfs_tools
./configure \
    --prefix=/usr \
    --host=%{lfs_tgt}                   \
    --build=$(build-aux/config.guess)   \
    --with-internal-glib

%else
#FIXME: pkg-config depends on glib and glib depends on pkg-config. Find
#a way to allow pkg-config to use the installed glib.
./configure \
    --prefix=/usr \
    --with-internal-glib

%endif

%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install

# Let's remove this 'arch' specific binary for now until it becomes useful.
rm -f %{buildroot}/usr/bin/x86_64-unknown-linux-gnu-pkg-config

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/share/aclocal/*

%else
/usr/bin/pkg-config
/usr/share/aclocal/pkg.m4

%files doc
/usr/share/doc/pkg-config/pkg-config-guide.html

%files man
/usr/share/man/man*/*

%endif