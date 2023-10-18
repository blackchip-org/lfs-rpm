%global version         2.4
%global _build_id_links none

Name:           inetutils
Version:        %{version}
Release:        1%{?dist}
Summary:        A collection of common network programs
License:        GPLv2+

Source0:        https://ftp.gnu.org/gnu/inetutils/inetutils-%{version}.tar.xz

%description
Inetutils is a collection of common network programs. It includes:

- An inetd meta-server.
- An ftp client and server.
- A telnet client and server.
- An rsh client and server.
- An rlogin client and server.
- A tftp client and server.
- A talk client and server.
- A syslogd daemon.
- Network tools: ping, ping6, traceroute, whois.
- Admin tools: hostname, dnsdomainname, ifconfig, logger
- And more...

Most of them are improved versions of programs originally from BSD. Some others
are original versions, written from scratch.


%prep
%setup -q


%build
./configure --prefix=/usr        \
            --bindir=/usr/bin    \
            --localstatedir=/var \
            --disable-logger     \
            --disable-whois      \
            --disable-rcp        \
            --disable-rexec      \
            --disable-rlogin     \
            --disable-rsh        \
            --disable-servers
make


%check
make check


%install
make DESTDIR=%{buildroot} install
mkdir %{buildroot}/usr/sbin
mv -v %{buildroot}/usr/{,s}bin/ifconfig
rm -f %{buildroot}/usr/share/info/dir


%files
/usr/bin/dnsdomainname
/usr/bin/ftp
/usr/bin/hostname
/usr/bin/ping
/usr/bin/ping6
/usr/bin/talk
/usr/bin/telnet
/usr/bin/tftp
/usr/bin/traceroute
/usr/sbin/ifconfig
/usr/share/info/*
/usr/share/man/man1/*
