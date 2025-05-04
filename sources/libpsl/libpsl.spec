# dnf

%global name            libpsl
%global version         0.21.5
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A collection of Top Level Domains (TLDs) suffixes
License:        MIT

Source0:        https://github.com/rockdaboot/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  python-devel

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
A Public Suffix List is a collection of Top Level Domains (TLDs) suffixes. TLDs
include Global Top Level Domains (gTLDs) like .com and .net; Country Top Level
Domains (ccTLDs) like .de and .cn; and Brand Top Level Domains like .apple
and .google. Brand TLDs allows users to register their own top level domain
that exist at the same level as ICANN's gTLDs. Brand TLDs are sometimes
referred to as Vanity Domains.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

%if %{with lfs}
rm %{buildroot}/usr/lib/libpsl.a

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/bin/psl
/usr/bin/psl-make-dafsa
/usr/lib/libpsl.so.*

%files devel
/usr/include/libpsl.h
/usr/lib/libpsl.so
/usr/lib/pkgconfig/libpsl.pc

%files man
/usr/share/man/man*/*

%files static
/usr/lib/libpsl.a

%endif
