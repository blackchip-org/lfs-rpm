# lfs

%global name        gettext
%global version     0.24
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        GNU libraries and utilities for producing multi-lingual messages
License:        GPLv3+ and LGPLv2+

Source0:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

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

%if !%{with lfs}
%description doc
Documentation for %{name}

%description devel
Development files for %{name}

%description info
Info documentation for %{name}

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
./configure --prefix=/usr                         \
            --host=%{lfs_tgt}                     \
            --build=$(./build-aux/config.guess)

%else
./configure --prefix=/usr    \
            --docdir=/usr/share/doc/%{name}-%{version}

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install
chmod -v 0755 %{buildroot}/%{?lfs_dir}/usr/lib/preloadable_libintl.so

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin
%{?lfs_dir}/usr/include
%{?lfs_dir}/usr/lib/gettext
%{?lfs_dir}/usr/lib/*.{a,so*}
%{?lfs_dir}/usr/libexec/%{name}
%{?lfs_dir}/usr/share/aclocal
%{?lfs_dir}/usr/share/gettext-%{version}
%{?lfs_dir}/usr/share/gettext

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
/usr/lib/gettext
/usr/lib/libasprintf.so.*
/usr/lib/libgettextlib-%{version}.so
/usr/lib/libgettextpo.so.*
/usr/lib/libgettextsrc-%{version}.so
/usr/lib/libtextstyle.so.*
/usr/lib/preloadable_libintl.so
/usr/libexec/%{name}
/usr/share/%{name}-%{version}
/usr/share/%{name}

%files devel
/usr/include/*.h
/usr/include/textstyle
/usr/lib/libasprintf.so
/usr/lib/libgettextlib.so
/usr/lib/libgettextpo.so
/usr/lib/libgettextsrc.so
/usr/lib/libtextstyle.so
/usr/share/aclocal/build-to-host.m4
/usr/share/aclocal/gettext.m4
/usr/share/aclocal/host-cpu-c-abi.m4
/usr/share/aclocal/iconv.m4
/usr/share/aclocal/intlmacosx.m4
/usr/share/aclocal/lib-ld.m4
/usr/share/aclocal/lib-link.m4
/usr/share/aclocal/lib-prefix.m4
/usr/share/aclocal/nls.m4
/usr/share/aclocal/po.m4
/usr/share/aclocal/progtest.m4

%files doc
/usr/share/doc/%{name}-%{version}

%files info
/usr/share/info/*

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*

%files static
/usr/lib/libasprintf.a
/usr/lib/libgettextlib.a
/usr/lib/libgettextpo.a
/usr/lib/libgettextsrc.a
/usr/lib/libtextstyle.a

%endif
