Name:           curl
Version:        8.11.1
Release:        1%{?dist}
Summary:        Tool for transferring data from or to a server using URLs
License:        curl

Source0:        https://curl.se/download/curl-%{version}.tar.xz

BuildRequires:  libpsl
BuildRequires:  openssl
Suggests:       %{name}-man = %{version}

%package man
Summary:        Manual pages for %{name}

%description
curl is a tool for transferring data from or to a server using URLs. It
supports these protocols: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS,
IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP,
SMB, SMBS, SMTP, SMTPS, TELNET, TFTP, WS and WSS.

curl is powered by libcurl for all transfer-related features.

%description man
Manual pages for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure \
    --prefix=/usr \
    --with-openssl
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

# Remove static library
rm %{buildroot}/usr/lib/libcurl.a

#---------------------------------------------------------------------------
%files
/usr/bin/curl
/usr/bin/curl-config
/usr/include/%{name}
/usr/lib/libcurl.so
/usr/lib/libcurl.so.4
/usr/lib/pkgconfig/libcurl.pc
/usr/share/aclocal/libcurl.m4

%defattr(755,root,root,755)
/usr/lib/libcurl.so.4.8.0

%files man
/usr/share/man/man{1,3}/*
