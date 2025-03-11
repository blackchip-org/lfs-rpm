# extra

Name:           fmt
Version:        11.1.4
Release:        1%{?dist}
Summary:        Fast and safe alternative to C stdio and C++ iostreams
License:        {fmt}

Source:         https://github.com/fmtlib/fmt/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake

%description
{fmt} is an open-source formatting library providing a fast and safe
alternative to C stdio and C++ iostreams.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DBUILD_SHARED_LIBS=TRUE \
    ..
%make

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/libfmt.so
/usr/lib/libfmt.so.11
%shlib /usr/lib/libfmt.so.%{version}
/usr/lib/pkgconfig/%{name}.pc