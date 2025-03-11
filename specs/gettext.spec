Name:           gettext
Version:        0.24
Release:        1%{?dist}
Summary:        GNU libraries and utilities for producing multi-lingual messages
License:        GPLv3+ and LGPLv2+

Source:         https://ftp.gnu.org/pub/gnu/gettext/gettext-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

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

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

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
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(./build-aux/config.guess)

%else
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/%{name}-%{version}

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
chmod -v 0755 %{buildroot}/usr/lib/preloadable_libintl.so
%remove_info_dir

%endif

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
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/gettext
%{lfs_dir}/usr/lib/*.{a,so*}
%{lfs_dir}/usr/libexec/%{name}
%{lfs_dir}/usr/share/aclocal/*
%{lfs_dir}/usr/share/gettext-%{version}
%{lfs_dir}/usr/share/gettext
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/*.mo

%else
/usr/bin/autopoint
/usr/bin/envsubst
/usr/bin/gettext
/usr/bin/gettext.sh
/usr/bin/gettextize
/usr/bin/msgattrib
/usr/bin/msgcat
/usr/bin/msgcmp
/usr/bin/msgcomm
/usr/bin/msgconv
/usr/bin/msgen
/usr/bin/msgexec
/usr/bin/msgfilter
/usr/bin/msgfmt
/usr/bin/msggrep
/usr/bin/msginit
/usr/bin/msgmerge
/usr/bin/msgunfmt
/usr/bin/msguniq
/usr/bin/ngettext
/usr/bin/recode-sr-latin
/usr/bin/xgettext
/usr/include/*.h
/usr/include/textstyle
/usr/lib/gettext
/usr/lib/libasprintf.so
/usr/lib/libasprintf.so.0
%shlib /usr/lib/libasprintf.so.0.0.0
/usr/lib/libgettextlib.so
%shlib /usr/lib/libgettextlib-0.24.so
/usr/lib/libgettextpo.so
/usr/lib/libgettextpo.so.0
%shlib /usr/lib/libgettextpo.so.0.5.13
/usr/lib/libgettextsrc.so
%shlib /usr/lib/libgettextsrc-0.24.so
/usr/lib/libtextstyle.so
/usr/lib/libtextstyle.so.0
%shlib /usr/lib/libtextstyle.so.0.2.4
%shlib /usr/lib/preloadable_libintl.so
/usr/libexec/%{name}
/usr/share/aclocal/*.m4
/usr/share/%{name}-%{version}
/usr/share/%{name}

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
