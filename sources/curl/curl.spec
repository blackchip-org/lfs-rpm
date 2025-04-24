# dnf

%global name            curl
%global version         8.12.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Tool for transferring data from or to a server using URLs
License:        curl

Source0:        https://curl.se/download/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  libpsl
BuildRequires:  openssl
Suggests:       %{name}-doc = %{version}

%description
curl is a tool for transferring data from or to a server using URLs. It
supports these protocols: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS,
IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP,
SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

curl is powered by libcurl for all transfer-related features.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

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

# Remove static library
rm %{buildroot}/usr/lib/libcurl.a

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/lib/pkgconfig
/usr/share/aclocal

%else
/usr/bin/curl
/usr/bin/curl-config
/usr/include/%{name}
/usr/lib/libcurl.so
/usr/lib/libcurl.so.4
%shlib /usr/lib/libcurl.so.4.8.0
/usr/lib/pkgconfig/libcurl.pc
/usr/share/aclocal/libcurl.m4

%files doc
/usr/share/man/man{1,3}/*

%endif
