# dnf

%global name                yaml-cpp
%global version             0.9.0
%global release             1

# https://github.com/jbeder/yaml-cpp

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        https://github.com/jbeder/yaml-cpp
License:        MIT

Source0:        https://github.com/jbeder/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  cmake

%if !%{with lfs}
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%endif

%description
yaml-cpp is a YAML parser and emitter in C++ matching the YAML 1.2 spec.

%if !%{with lfs}
%description devel
Development files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{name}-%{name}-%{version}

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DYAML_BUILD_SHARED_LIBS=on \
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
/usr/lib/lib%{name}.so*
/usr/lib/pkgconfig/%{name}.pc

%else
/usr/lib/lib%{name}.so*

%files devel
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/pkgconfig/%{name}.pc

%endif
