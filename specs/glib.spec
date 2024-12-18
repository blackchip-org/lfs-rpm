Name:           glib
Version:        2.83.0
Release:        1%{?dist}
Summary:        Low-level core library
License:        LGPLv2

%global         version2 2.83

Source0:        https://download.gnome.org/sources/glib/%{version2}/glib-%{version}.tar.xz

BuildRequires:  meson

%description
GLib is the low-level core library that forms the basis for projects such
as GTK and GNOME. It provides data structure handling for C, portability
wrappers, and interfaces for such runtime functionality as an event loop,
threads, dynamic loading, and an object system.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
meson setup --prefix=/usr _build
meson compile -C _build

#---------------------------------------------------------------------------
%install
DESTDIR=%{buildroot} meson install -C _build

#---------------------------------------------------------------------------
%files
/usr/bin/gapplication
/usr/bin/gdbus
/usr/bin/gdbus-codegen
/usr/bin/gi-compile-repository
/usr/bin/gi-decompile-typelib
/usr/bin/gi-inspect-typelib
/usr/bin/gio
/usr/bin/gio-querymodules
/usr/bin/glib-compile-resources
/usr/bin/glib-compile-schemas
/usr/bin/glib-genmarshal
/usr/bin/glib-gettextize
/usr/bin/glib-mkenums
/usr/bin/gobject-query
/usr/bin/gresource
/usr/bin/gsettings
/usr/bin/gtester
/usr/bin/gtester-report
/usr/include/gio-unix-2.0
/usr/include/glib-2.0
/usr/lib/glib-2.0/include/glibconfig.h
/usr/lib/libgio-2.0.so
/usr/lib/libgio-2.0.so.0
/usr/lib/libgirepository-2.0.so
/usr/lib/libgirepository-2.0.so.0
/usr/lib/libglib-2.0.so
/usr/lib/libglib-2.0.so.0
/usr/lib/libgmodule-2.0.so
/usr/lib/libgmodule-2.0.so.0
/usr/lib/libgobject-2.0.so
/usr/lib/libgobject-2.0.so.0
/usr/lib/libgthread-2.0.so
/usr/lib/libgthread-2.0.so.0
/usr/lib/pkgconfig/gio-2.0.pc
/usr/lib/pkgconfig/gio-unix-2.0.pc
/usr/lib/pkgconfig/girepository-2.0.pc
/usr/lib/pkgconfig/glib-2.0.pc
/usr/lib/pkgconfig/gmodule-2.0.pc
/usr/lib/pkgconfig/gmodule-export-2.0.pc
/usr/lib/pkgconfig/gmodule-no-export-2.0.pc
/usr/lib/pkgconfig/gobject-2.0.pc
/usr/lib/pkgconfig/gthread-2.0.pc
/usr/libexec/gio-launch-desktop
/usr/share/aclocal/glib-2.0.m4
/usr/share/aclocal/glib-gettext.m4
/usr/share/aclocal/gsettings.m4
/usr/share/bash-completion/completions/gapplication
/usr/share/bash-completion/completions/gdbus
/usr/share/bash-completion/completions/gio
/usr/share/bash-completion/completions/gresource
/usr/share/bash-completion/completions/gsettings
/usr/share/gdb/auto-load/usr/lib/libglib-2.0.so.0.8300.0-gdb.py
/usr/share/gdb/auto-load/usr/lib/libgobject-2.0.so.0.8300.0-gdb.py
/usr/share/gettext/its/gschema.its
/usr/share/gettext/its/gschema.loc
/usr/share/glib-2.0
/usr/share/locale/*/LC_MESSAGES/glib20.mo

%defattr(755,root,root,755)
/usr/lib/libgio-2.0.so.0.8300.0
/usr/lib/libgirepository-2.0.so.0.8300.0
/usr/lib/libglib-2.0.so.0.8300.0
/usr/lib/libgmodule-2.0.so.0.8300.0
/usr/lib/libgobject-2.0.so.0.8300.0
/usr/lib/libgthread-2.0.so.0.8300.0
