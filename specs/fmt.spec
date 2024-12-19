Name:           fmt
Version:        11.0.2
Release:        1%{?dist}
Summary:        Fast and safe alternative to C stdio and C++ iostreams
License:        {fmt}

Source0:        https://github.com/fmtlib/fmt/archive/refs/tags/%{version}.tar.gz

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
    -DPYTHON_DESIRED="3" \
    -DWITH_MAN=0 \
    ..
%make

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/lib/libfmt.a

#---------------------------------------------------------------------------
%files
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/pkgconfig/%{name}.pc