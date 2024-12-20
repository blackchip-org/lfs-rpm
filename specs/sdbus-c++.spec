Name:           sdbus-c++
Version:        2.1.0
Release:        1%{?dist}
Summary:        Library for Linux designed to provide expressive, easy-to-use API in modern C++.
License:        LGPL-2.1

Source:         https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
Suggests:       %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}

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

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n sdbus-cpp-%{version}

#---------------------------------------------------------------------------
%build
mkdir -p _build
cd _build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ..
%make

#---------------------------------------------------------------------------
%install
cd _build
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/include/sdbus-c++
/usr/lib/cmake/sdbus-c++
/usr/lib/libsdbus-c++.so
/usr/lib/libsdbus-c++.so.2
%shlib /usr/lib/libsdbus-c++.so.2.1.0
/usr/lib/pkgconfig/sdbus-c++.pc

%files doc
/usr/share/doc/sdbus-c++
