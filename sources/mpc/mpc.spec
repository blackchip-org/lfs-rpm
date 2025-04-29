# lfs

%global name            mpc
%global version         1.3.1
%global release         1

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
MPC is a C library for the arithmetic of complex numbers with arbitrarily high
precision and correct rounding of the result. It is built upon and follows the
same principles as Mpfr.

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
%if %{with lfs}
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}

%else
./configure --prefix=/usr    \
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
/usr/lib/lib*.so*

%else
/usr/lib/libmpc.so.*

%files devel
/usr/include/*.h
/usr/lib/libmpc.so

%files doc
/usr/share/doc/%{name}-%{version}

%files info
/usr/share/info/*.gz

%files static
/usr/lib/libmpc.a

%endif
