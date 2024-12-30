Name:           iproute
Version:        6.7.0
Release:        1%{?dist}
Summary:        Advanced IP routing and network device configuration tools
License:        GPLv2+ and Public Domain

Source:         https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz

BuildRequires:  bison
Suggests:       %{name}-doc = %{version}

%description
The iproute package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
kernel.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n iproute2-%{version}

#---------------------------------------------------------------------------
%build
sed -i /ARPD/d Makefile
rm -fv man/man8/arpd.8

%make NETNS_RUN_DIR=/run/netns

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} SBINDIR=/usr/sbin install

#---------------------------------------------------------------------------
%files
/usr/include/iproute2
/usr/lib/tc/*
/usr/sbin/bridge
/usr/sbin/ctstat
/usr/sbin/genl
/usr/sbin/ifstat
/usr/sbin/ip
/usr/sbin/lnstat
/usr/sbin/nstat
/usr/sbin/routel
/usr/sbin/rtacct
/usr/sbin/rtmon
/usr/sbin/rtstat
/usr/sbin/ss
/usr/sbin/tc
/usr/share/bash-completion/completions/*
/usr/share/iproute2/bpf_pinning
/usr/share/iproute2/ematch_map
/usr/share/iproute2/group
/usr/share/iproute2/nl_protos
/usr/share/iproute2/rt_dsfield
/usr/share/iproute2/rt_protos
/usr/share/iproute2/rt_realms
/usr/share/iproute2/rt_scopes
/usr/share/iproute2/rt_tables

%files doc
/usr/share/man/man*/*