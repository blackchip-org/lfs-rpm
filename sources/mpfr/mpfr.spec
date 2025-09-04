# lfs

%global name            mpfr
%global version         4.2.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A C library for multiple-precision floating-point computations
License:        LGPLv3+ or GPLv2+

Source0:        https://ftpmirror.gnu.org/gnu/mpfr/mpfr-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  autoconf
BuildRequires:  texinfo

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
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and also has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit mantissa). MPFR
is based on the GMP multiple-precision library.

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
sed -e 's/+01,234,567/+1,234,567 /' \
    -e 's/13.10Pd/13Pd/'            \
    -i tests/tsprintf.c

%if %{with lfs}
./configure --prefix=/usr        \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}

%else
./configure --prefix=/usr        \
            --enable-thread-safe \
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
%files
%if %{with lfs}
/usr/include/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/lib/libmpfr.so.*

%files devel
/usr/include/*.h
/usr/lib/libmpfr.so
/usr/lib/pkgconfig/%{name}.pc

%files doc
/usr/share/doc/%{name}-%{version}

%files info
/usr/share/info/*.gz

%files static
/usr/lib/libmpfr.a

%endif