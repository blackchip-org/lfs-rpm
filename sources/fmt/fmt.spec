# lfs

%global name            fmt
%global version         11.1.4
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Fast and safe alternative to C stdio and C++ iostreams
License:        {fmt}

Source0:        https://github.com/fmtlib/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  cmake

%description
{fmt} is an open-source formatting library providing a fast and safe
alternative to C stdio and C++ iostreams.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
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
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build
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
/usr/lib/libfmt.so
/usr/lib/libfmt.so.11
%shlib /usr/lib/libfmt.so.%{version}
/usr/lib/pkgconfig/%{name}.pc

%endif
