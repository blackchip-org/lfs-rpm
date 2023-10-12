%global version     6.3.0

Name:           gmp
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU arbitrary precision library
License:        LGPLv3+ or GPLv2+

Source0:        https://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.xz

%global _build_id_links none

%description
The gmp package contains GNU MP, a library for arbitrary precision arithmetic,
signed integers operations, rational numbers and floating point numbers. GNU MP
is designed for speed, for both small and very large operands. GNU MP is fast
because it uses fullwords as the basic arithmetic type, it uses fast
algorithms, it carefully optimizes assembly code for many CPUs' most common
inner loops, and it generally emphasizes speed over simplicity/elegance in its
operations.

Install the gmp package if you need a fast arbitrary precision library.


%prep
%setup -q


%build
./configure --prefix=/usr    \
            --enable-cxx     \
            --disable-static \
            --docdir=/usr/share/doc/gmp-%{version}
make
make html


%check
make check 2>&1 | tee gmp-check-log
awk '/# PASS:/{total+=$3} ; END{print total}' gmp-check-log


%install
make DESTDIR=%{buildroot} install install-html
rm -rf %{buildroot}/usr/share/info/dir


%files
/usr/include/*.h
/usr/lib/libgmp.so
/usr/lib/libgmp.so.10
/usr/lib/libgmpxx.so
/usr/lib/libgmpxx.so.4
/usr/lib/pkgconfig/gmp.pc
/usr/lib/pkgconfig/gmpxx.pc
/usr/share/doc/gmp-%{version}
/usr/share/info/*

%defattr(755,root,root,755)
/usr/lib/libgmp.so.10.5.0
/usr/lib/libgmpxx.so.4.7.0


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
