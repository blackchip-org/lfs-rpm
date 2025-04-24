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

BuildRequires:  python
Suggests:       %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description
A Public Suffix List is a collection of Top Level Domains (TLDs) suffixes. TLDs
include Global Top Level Domains (gTLDs) like .com and .net; Country Top Level
Domains (ccTLDs) like .de and .cn; and Brand Top Level Domains like .apple
and .google. Brand TLDs allows users to register their own top level domain
that exist at the same level as ICANN's gTLDs. Brand TLDs are sometimes
referred to as Vanity Domains.

%description doc
Documentation for %{name}

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

# Remove static library
rm %{buildroot}/usr/lib/libpsl.a

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/bin/psl
/usr/bin/psl-make-dafsa
/usr/include/libpsl.h
/usr/lib/libpsl.so
/usr/lib/libpsl.so.5
%shlib /usr/lib/libpsl.so.5.3.5
/usr/lib/pkgconfig/libpsl.pc

%files doc
/usr/share/man/man*/*

%endif
