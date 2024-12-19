Name:           gmp
Version:        6.3.0
Release:        1%{?dist}
Summary:        A GNU arbitrary precision library
License:        LGPLv3+ or GPLv2+

Source0:        https://ftp.gnu.org/gnu/gmp/gmp-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}

%description
The gmp package contains GNU MP, a library for arbitrary precision arithmetic,
signed integers operations, rational numbers and floating point numbers. GNU MP
is designed for speed, for both small and very large operands. GNU MP is fast
because it uses fullwords as the basic arithmetic type, it uses fast
algorithms, it carefully optimizes assembly code for many CPUs' most common
inner loops, and it generally emphasizes speed over simplicity/elegance in its
operations.

Install the gmp package if you need a fast arbitrary precision library.

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr    \
            --enable-cxx     \
            --disable-static \
            --docdir=/usr/share/doc/gmp-%{version}
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
/usr/include/*.h
/usr/lib/libgmp.so
/usr/lib/libgmp.so.10
%shlib /usr/lib/libgmp.so.10.5.0
/usr/lib/libgmpxx.so
/usr/lib/libgmpxx.so.4
%shlib /usr/lib/libgmpxx.so.4.7.0
/usr/lib/pkgconfig/gmp.pc
/usr/lib/pkgconfig/gmpxx.pc

%files doc
/usr/share/doc/gmp-%{version}
/usr/share/info/*
