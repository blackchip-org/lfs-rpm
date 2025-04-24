# dnf

%global name            toml11
%global version         4.4.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Feature-rich TOML language library for C++11/14/17/20
License:        MIT

Source0:        https://github.com/ToruNiina/toml11/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  cmake

%description
toml11 is a feature-rich TOML language library for C++11/14/17/20.

- It complies with the latest TOML language specification.
- It passes all the standard TOML language test cases.
- It supports new features merged into the upcoming TOML version (v1.1.0).
- It provides clear error messages, including the location of the error.
- It parses and retains comments, associating them with corresponding values.
- It maintains formatting information such as hex integers and considers these
  during serialization.
- It provides exception-less parse function.
- It supports complex type conversions from TOML values.
- It allows customization of the types stored in toml::value.
- It provides some extensions not present in the TOML language standard.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ..
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include
/usr/lib/cmake/%{name}

%else
/usr/include/toml.hpp
/usr/include/%{name}
/usr/lib/cmake/%{name}

%endif

