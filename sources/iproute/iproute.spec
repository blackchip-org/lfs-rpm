# lfs

%global name        iproute
%global version     6.13.0
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Advanced IP routing and network device configuration tools
License:        GPLv2+ and Public Domain

Source0:        https://www.kernel.org/pub/linux/utils/net/%{name}2/%{name}2-%{version}.tar.xz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q -n iproute2-%{version}

#---------------------------------------------------------------------------
%build
sed -i /ARPD/d Makefile
rm -fv man/man8/arpd.8

make %{?_smp_mflags} NETNS_RUN_DIR=/run/netns

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} SBINDIR=/usr/sbin install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include
/usr/lib/tc
/usr/sbin
/usr/share/{bash-completion,%{name}2}

%else
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

%endif
