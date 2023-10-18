%define version   0.22

Name:           gettext
Version:        %{version}
Release:        1%{?dist}
Summary:        GNU libraries and utilities for producing multi-lingual messages
License:        GPLv3+ and LGPLv2+

Source0:        https://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz

%global _build_id_links none

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


%prep
%setup -q


%build
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/%{name}-%{version}
make


%check
make check


%install
make DESTDIR=%{buildroot} install
chmod -v 0755 %{buildroot}/usr/lib/preloadable_libintl.so
rm -rf %{buildroot}/usr/share/info/dir


%files
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
/usr/lib/libgettextlib-0.22.so
/usr/lib/libgettextlib.so
/usr/lib/libgettextpo.so
/usr/lib/libgettextpo.so.0
/usr/lib/libgettextsrc-0.22.so
/usr/lib/libgettextsrc.so
/usr/lib/libtextstyle.so
/usr/lib/libtextstyle.so.0
/usr/lib/preloadable_libintl.so
/usr/share/%{name}-%{version}
/usr/share/%{name}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man{1,3}/*

%defattr(755,root,root,755)
/usr/lib/libasprintf.so.0.0.0
/usr/lib/libgettextpo.so.0.5.9
/usr/lib/libtextstyle.so.0.2.0
/usr/share/aclocal/*.m4
/usr/share/doc/%{name}-%{version}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4-1
- Initial package


