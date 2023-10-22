Name:           pkg-config
Version:        0.29.2
Release:        1%{?dist}
Summary:        Helper tool used when compiling applications and libraries
License:        GPLv2+

Source0:        https://pkgconfig.freedesktop.org/releases/pkg-config-%{version}.tar.gz

%description
pkg-config is a helper tool used when compiling applications and libraries. It
helps you insert the correct compiler options on the command line so an
application can use gcc -o test test.c `pkg-config --libs --cflags glib-2.0`
for instance, rather than hard-coding values on where to find glib (or other
libraries). It is language-agnostic, so it can be used for defining the
location of documentation tools, for instance.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
./configure --prefix=/usr \
            --host=%{lfs_tgt}                   \
            --build=$(build-aux/config.guess)   \
            --with-internal-glib

%endif

%make
%lfs_build_end


#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/share/aclocal/*

%endif

