# extra

Name:           libpsl
Version:        0.21.5
Release:        1%{?dist}
Summary:        A collection of Top Level Domains (TLDs) suffixes
License:        MIT

Source:         https://github.com/rockdaboot/libpsl/releases/download/%{version}/libpsl-%{version}.tar.gz

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
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

# Remove static library
rm %{buildroot}/usr/lib/libpsl.a

#---------------------------------------------------------------------------
%files
/usr/bin/psl
/usr/bin/psl-make-dafsa
/usr/include/libpsl.h
/usr/lib/libpsl.so
/usr/lib/libpsl.so.5
%shlib /usr/lib/libpsl.so.5.3.5
/usr/lib/pkgconfig/libpsl.pc

%files doc
/usr/share/man/man*/*
