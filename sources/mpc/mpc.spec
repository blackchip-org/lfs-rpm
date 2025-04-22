# lfs

%global name        mpc
%global version     1.3.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        C library for multiple precision complex arithmetic
License:        LGPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/mpc-%{version}
make %{?_smp_mflags}
make html

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install install-html

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include
/usr/lib/lib*.so*

%else
/usr/include/*.h
/usr/lib/libmpc.so
/usr/lib/libmpc.so.3
%shlib /usr/lib/libmpc.so.3.3.1

%files doc
/usr/share/doc/mpc-%{version}
/usr/share/info/*

%endif
