# lfs

%global name            gmp
%global version         6.3.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU arbitrary precision library
License:        LGPLv3+ or GPLv2+

Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  texinfo
Suggests:       %{name}-doc = %{version}

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The gmp package contains GNU MP, a library for arbitrary precision arithmetic,
signed integers operations, rational numbers and floating point numbers. GNU MP
is designed for speed, for both small and very large operands. GNU MP is fast
because it uses fullwords as the basic arithmetic type, it uses fast
algorithms, it carefully optimizes assembly code for many CPUs' most common
inner loops, and it generally emphasizes speed over simplicity/elegance in its
operations.

Install the gmp package if you need a fast arbitrary precision library.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description info
Info documentation for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
sed -i '/long long t1;/,+1s/()/(...)/' configure
%if %{with lfs}
./configure --prefix=/usr    \
            --enable-cxx     \
            --disable-static \
            --docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}

%else
./configure --prefix=/usr    \
            --enable-cxx     \
            --docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}
make html

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs}
make DESTDIR=%{buildroot} install

%else
make DESTDIR=%{buildroot} install install-html

%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/*
/usr/lib/*

%else
/usr/lib/libgmp.so.*
/usr/lib/libgmpxx.so.*

%files devel
/usr/include/*.h
/usr/lib/libgmp.so
/usr/lib/libgmpxx.so
/usr/lib/pkgconfig/%{name}.pc
/usr/lib/pkgconfig/%{name}xx.pc

%files doc
/usr/share/doc/gmp-%{version}

%files info
/usr/share/info/*.gz

%files static
/usr/lib/libgmp.a
/usr/lib/libgmpxx.a

%endif
