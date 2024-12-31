Name:           luv
Version:        1.48.0.2
Release:        1%{?dist}
Summary:        lubuv bindings for luajit
License:        GPLv2

%global         f_version   1.48.0-2

Source:         https://github.com/luvit/luv/releases/download/%{f_version}/luv-%{f_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  lua

%description
This library makes libuv available to lua scripts. It was made for the luvit
project but should usable from nearly any lua project.

The library can be used by multiple threads at once. Each thread is assumed to
load the library from a different lua_State. Luv will create a unique
uv_loop_t for each state. You can't share uv handles between states/loops.

#---------------------------------------------------------------------------
%prep
%setup -q -n luv-%{f_version}

#---------------------------------------------------------------------------
%build

mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DBUILD_MODULE=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DLUA_BUILD_TYPE=System \
    -DWITH_LUA_ENGINE=Lua \
    ..

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/include/luv
/usr/lib/libluv.so
/usr/lib/libluv.so.1
%shlib /usr/lib/libluv.so.1.48.0
/usr/lib/pkgconfig/libluv.pc
