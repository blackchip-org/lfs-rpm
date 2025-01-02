Name:           mpc
Version:        1.3.1
Release:        1%{?dist}
Summary:        C library for multiple precision complex arithmetic
License:        LGPLv3+

Source0:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  texinfo
Suggests:       %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo

%description
MPC is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows the
same principles as Mpfr.

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/mpc-%{version}
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
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/include/*.h
/usr/lib/libmpc.so
/usr/lib/libmpc.so.3
%shlib /usr/lib/libmpc.so.3.3.1

%files doc
/usr/share/doc/mpc-%{version}
/usr/share/info/*
