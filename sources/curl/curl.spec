# dnf

%global name            curl
%global version         8.15.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tool for transferring data from or to a server using URLs
License:        curl

Source0:        https://curl.se/download/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  libpsl-devel
BuildRequires:  openssl-devel

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
curl is a tool for transferring data from or to a server using URLs. It
supports these protocols: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS,
IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP,
SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

curl is powered by libcurl for all transfer-related features.

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
./configure \
    --prefix=/usr \
    --with-openssl
make

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

%if %{with lfs}
rm %{buildroot}/usr/lib/libcurl.a

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/%{name}
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*
/usr/share/aclocal/*

%else
/usr/bin/curl
/usr/bin/curl-config
/usr/lib/libcurl.so.*

%files devel
/usr/include/%{name}
/usr/lib/libcurl.so
/usr/lib/pkgconfig/libcurl.pc
/usr/share/aclocal/libcurl.m4

%files man
/usr/share/man/man{1,3}/*

%files static
/usr/lib/libcurl.a

%endif
