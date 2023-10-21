Name:           mpc
Version:        1.3.1
Release:        1%{?dist}
Summary:        C library for multiple precision complex arithmetic
License:        LGPLv3+

Source0:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz

%description
MPC is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows the
same principles as Mpfr.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/mpc-%{version}
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
/usr/include/*.h
/usr/lib/libmpc.so
/usr/lib/libmpc.so.3
/usr/share/doc/mpc-%{version}
/usr/share/info/*

%defattr(755,root,root,755)
/usr/lib/libmpc.so.3.3.1