Name:           msgpack
Version:        6.1.0
Release:        1%{?dist}
Summary:        It's like JSON but smaller and faster
License:        BSL-1.0

Source:         https://github.com/msgpack/msgpack-c/releases/download/c-%{version}/msgpack-c-%{version}.tar.gz

BuildRequires:  cmake

%description
MessagePack is an efficient binary serialization format, which lets you
exchange data among multiple languages like JSON, except that it's faster and
smaller. Small integers are encoded into a single byte and short strings
require only one extra byte in addition to the strings themselves.

#---------------------------------------------------------------------------
%prep
%setup -q -n msgpack-c-%{version}

#---------------------------------------------------------------------------
%build
mkdir -v build
cd       build

cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DBUILD_SHARED_LIBS=ON \
    ..

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/include/msgpack{,.h}
/usr/lib/cmake/msgpack-c
/usr/lib/libmsgpack-c.so
/usr/lib/libmsgpack-c.so.2
%shlib /usr/lib/libmsgpack-c.so.2.0.0
/usr/lib/pkgconfig/msgpack-c.pc
