Name:           mpfr
Version:        4.2.1
Release:        1%{?dist}
Summary:        A C library for multiple-precision floating-point computations
License:        LGPLv3+ or GPLv2+

Source0:        https://ftp.gnu.org/gnu/mpfr/mpfr-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and also has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit mantissa). MPFR
is based on the GMP multiple-precision library.

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
sed -e 's/+01,234,567/+1,234,567 /' \
    -e 's/13.10Pd/13Pd/'            \
    -i tests/tsprintf.c

./configure --prefix=/usr        \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/mpfr-%{version}
%make
%make html

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install install-html
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/include/*
/usr/lib/libmpfr.so
/usr/lib/libmpfr.so.6
%shlib /usr/lib/libmpfr.so.6.2.1
/usr/lib/pkgconfig/mpfr.pc

%files doc
/usr/share/doc/mpfr-%{version}
/usr/share/info/*
