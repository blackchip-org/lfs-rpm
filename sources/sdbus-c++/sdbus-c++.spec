# dnf

%global name            sdbus-c++
%global source_name     sdbus-cpp
%global version         2.1.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Library for Linux designed to provide expressive, easy-to-use API in modern C++.
License:        LGPL-2.1

Source0:        https://github.com/Kistler-Group/%{source_name}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.sha256

Provides:       %{name}-devel
BuildRequires:  cmake
BuildRequires:  pkgconf
BuildRequires:  systemd-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%endif

%description
sdbus-c++ is a high-level C++ D-Bus library for Linux designed to provide
expressive, easy-to-use API in modern C++. It adds another layer of abstraction
on top of sd-bus, a nice, fresh C D-Bus implementation by systemd.

sdbus-c++ has been written primarily as a replacement of dbus-c++, which
currently suffers from a number of (unresolved) bugs, concurrency issues and
inherent design complexities and limitations. sdbus-c++ has learned from
dbus-c++ and has chosen a different path, a path of simple yet powerful design
that is intuitive and friendly to the user and inherently free of those bugs.

Even though sdbus-c++ uses sd-bus library, it is not necessarily constrained
to systemd and can perfectly be used in non-systemd environments as well.

%if !%{with lfs}
%description doc
Documentation for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
mkdir -p _build
cd _build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ..
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd _build
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/libsdbus-c++.so*
/usr/lib/pkgconfig/%{name}.pc

%files doc
/usr/share/doc/%{name}

%endif
