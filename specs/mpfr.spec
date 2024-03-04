Name:           mpfr
Version:        4.2.1
Release:        1%{?dist}
Summary:        A C library for multiple-precision floating-point computations
License:        LGPLv3+ or GPLv2+

Source0:        https://ftp.gnu.org/gnu/mpfr/mpfr-%{version}.tar.xz

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and also has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit mantissa). MPFR
is based on the GMP multiple-precision library.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

sed -e 's/+01,234,567/+1,234,567 /' \
    -e 's/13.10Pd/13Pd/'            \
    -i tests/tsprintf.c

./configure --prefix=/usr        \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/mpfr-%{version}
%make
%make html
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install install-html
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
/usr/include/*
/usr/lib/libmpfr.so
/usr/lib/libmpfr.so.6
/usr/lib/pkgconfig/mpfr.pc
/usr/share/doc/mpfr-%{version}
/usr/share/info/*

%defattr(755,root,root,755)
/usr/lib/libmpfr.so.6.2.1
