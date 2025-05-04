# dnf

%global name            glib
%global version_2       2.84
%global version         %{version_2}.0
%global major_version   2.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Low-level core library
License:        LGPLv2

Source0:        https://download.gnome.org/sources/%{name}/%{version_2}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  gettext
BuildRequires:  libffi-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pcre2-devel
BuildRequires:  pkgconf

%if !%{with lfs}
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%endif

%description
GLib is the low-level core library that forms the basis for projects such
as GTK and GNOME. It provides data structure handling for C, portability
wrappers, and interfaces for such runtime functionality as an event loop,
threads, dynamic loading, and an object system.

%if !%{with lfs}
%description devel
Development files for %{name}

%description lang
Language files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
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
%if %{with lfs}
/usr/bin/*
/usr/include/{gio-unix-%{major_version},glib-%{major_version}}
/usr/lib/lib*.so*
/usr/lib/%{name}-%{major_version}
/usr/lib/pkgconfig/*
/usr/libexec
/usr/share/aclocal/*
/usr/share/bash-completion/completions/*
/usr/share/gdb/*
/usr/share/gettext/*
/usr/share/%{name}-%{major_version}/*

%else
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
/usr/lib/libgio-%{major_version}.so.*
/usr/lib/libgirepository-%{major_version}.so.*
/usr/lib/libglib-%{major_version}.so.*
/usr/lib/libgmodule-%{major_version}.so.*
/usr/lib/libgobject-%{major_version}.so.*
/usr/lib/libgthread-%{major_version}.so.*
/usr/libexec/gio-launch-desktop
/usr/libexec/installed-tests/glib
/usr/share/bash-completion/completions/gapplication
/usr/share/bash-completion/completions/gdbus
/usr/share/bash-completion/completions/gio
/usr/share/bash-completion/completions/gresource
/usr/share/bash-completion/completions/gsettings
/usr/share/gdb/auto-load/usr/lib/libglib-%{major_version}.so.*
/usr/share/gdb/auto-load/usr/lib/libgobject-%{major_version}.so.*
/usr/share/gettext/its/gschema.its
/usr/share/gettext/its/gschema.loc
/usr/share/glib-%{major_version}

%files devel
/usr/include/gio-unix-%{major_version}
/usr/include/%{name}-%{major_version}
/usr/lib/glib-%{major_version}/include/glibconfig.h
/usr/lib/libgio-%{major_version}.so
/usr/lib/libgirepository-%{major_version}.so
/usr/lib/libglib-%{major_version}.so
/usr/lib/libgmodule-%{major_version}.so
/usr/lib/libgobject-%{major_version}.so
/usr/lib/libgthread-%{major_version}.so
/usr/lib/pkgconfig/gio-%{major_version}.pc
/usr/lib/pkgconfig/gio-unix-%{major_version}.pc
/usr/lib/pkgconfig/girepository-%{major_version}.pc
/usr/lib/pkgconfig/glib-%{major_version}.pc
/usr/lib/pkgconfig/gmodule-%{major_version}.pc
/usr/lib/pkgconfig/gmodule-export-%{major_version}.pc
/usr/lib/pkgconfig/gmodule-no-export-%{major_version}.pc
/usr/lib/pkgconfig/gobject-%{major_version}.pc
/usr/lib/pkgconfig/gthread-%{major_version}.pc
/usr/share/aclocal/glib-%{major_version}.m4
/usr/share/aclocal/glib-gettext.m4
/usr/share/aclocal/gsettings.m4

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%endif
