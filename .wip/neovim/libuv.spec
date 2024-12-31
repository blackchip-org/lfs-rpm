Name:           libuv
Version:        1.49.2
Release:        1%{?dist}
Summary:        Multi-platform support library with a focus on asynchronous I/O
License:        MIT

Source:         https://github.com/libuv/libuv/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake

%description
This library makes libuv available to lua scripts. It was made for the luvit
project but should usable from nearly any lua project.

The library can be used by multiple threads at once. Each thread is assumed to
load the library from a different lua_State. Luv will create a unique
uv_loop_t for each state. You can't share uv handles between states/loops.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build

mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ..

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/lib/*.a

#---------------------------------------------------------------------------
%files
/usr/include/*
/usr/lib/cmake/libuv/libuvConfig-noconfig.cmake
/usr/lib/cmake/libuv/libuvConfig.cmake
/usr/lib/libuv.so
/usr/lib/libuv.so.1
%shlib /usr/lib/libuv.so.1.0.0
/usr/lib/pkgconfig/libuv-static.pc
/usr/lib/pkgconfig/libuv.pc
/usr/share/doc/libuv/LICENSE
/usr/share/doc/libuv/LICENSE-extra
