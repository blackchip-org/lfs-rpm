%global version     4.2.0

Name:           mpfr
Version:        %{version}
Release:        1%{?dist}
Summary:        A C library for multiple-precision floating-point computations
License:        LGPLv3+ or GPLv2+

Source0:        https://ftp.gnu.org/gnu/mpfr/mpfr-%{version}.tar.xz

%global _build_id_links none

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and also has a
well-defined semantics. It copies the good ideas from the ANSI/IEEE-754
standard for double-precision floating-point arithmetic (53-bit mantissa). MPFR
is based on the GMP multiple-precision library.


%prep
%setup -q


%build
sed -e 's/+01,234,567/+1,234,567 /' \
    -e 's/13.10Pd/13Pd/'            \
    -i tests/tsprintf.c

./configure --prefix=/usr        \
            --disable-static     \
            --enable-thread-safe \
            --docdir=/usr/share/doc/mpfr-%{version}
make
make html


%check
make check


%install
make DESTDIR=%{buildroot} install install-html
rm -rf %{buildroot}/usr/share/info/dir


%files
/usr/include/*
/usr/lib/libmpfr.so
/usr/lib/libmpfr.so.6
/usr/lib/pkgconfig/mpfr.pc
/usr/share/doc/mpfr-%{version}
/usr/share/info/*

%defattr(755,root,root,755)
/usr/lib/libmpfr.so.6.2.0


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
