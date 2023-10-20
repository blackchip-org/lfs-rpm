Name:           gettext
Version:        0.22.3
Release:        1%{?dist}
Summary:        GNU libraries and utilities for producing multi-lingual messages
License:        GPLv3+ and LGPLv2+

Source0:        https://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.gz

%description
The GNU gettext package provides a set of tools and documentation for producing
multi-lingual messages in programs. Tools include a set of conventions about
how programs should be written to support message catalogs, a directory and
file naming organization for the message catalogs, a runtime library which
supports the retrieval of translated messages, and stand-alone programs for
handling the translatable and the already translated strings. Gettext provides
an easy to use library and tools for creating, using, and modifying natural
language catalogs and is a powerful and simple method for internationalizing
programs.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(./build-aux/config.guess)

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/gettext
%{lfs_dir}/usr/lib/*.{a,so*}
%{lfs_dir}/usr/share/aclocal/*
%{lfs_dir}/usr/share/gettext-%{version}
%{lfs_dir}/usr/share/gettext
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/*.mo

%endif
