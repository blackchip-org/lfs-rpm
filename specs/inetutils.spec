Name:           inetutils
Version:        2.6
Release:        1%{?dist}
Summary:        A collection of common network programs
License:        GPLv2+

Source:         https://ftp.gnu.org/gnu/inetutils/inetutils-%{version}.tar.xz
Suggests:       %{name}-doc = %{version}

%description
Inetutils is a collection of common network programs. It includes:

* An inetd meta-server.
* An ftp client and server.
* A telnet client and server.
* An rsh client and server.
* An rlogin client and server.
* A tftp client and server.
* A talk client and server.
* A syslogd daemon.
* Network tools: ping, ping6, traceroute, whois.
* Admin tools: hostname, dnsdomainname, ifconfig, logger
* And more...

Most of them are improved versions of programs originally from BSD. Some others
are original versions, written from scratch.

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
sed -i 's/def HAVE_TERMCAP_TGETENT/ 1/' telnet/telnet.c

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
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
mkdir %{buildroot}/usr/sbin
mv -v %{buildroot}/usr/{,s}bin/ifconfig
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%post
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/dnsdomainname
/usr/bin/ftp
/usr/bin/hostname
%attr(4755,root,root) /usr/bin/ping
%attr(4755,root,root) /usr/bin/ping6
/usr/bin/talk
/usr/bin/telnet
/usr/bin/tftp
%attr(4755,root,root) /usr/bin/traceroute
/usr/sbin/ifconfig

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*
