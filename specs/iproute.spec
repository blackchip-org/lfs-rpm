Name:           iproute
Version:        6.7.0
Release:        1%{?dist}
Summary:        Advanced IP routing and network device configuration tools
License:        GPLv2+ and Public Domain

Source0: https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-%{version}.tar.xz

%description
The iproute package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
kernel.

#---------------------------------------------------------------------------
%prep
%setup -q -n iproute2-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

sed -i /ARPD/d Makefile
rm -fv man/man8/arpd.8

%make NETNS_RUN_DIR=/run/netns
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} SBINDIR=/usr/sbin install
%lfs_install_end

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
/usr/share/man/man{3,7,8}/*