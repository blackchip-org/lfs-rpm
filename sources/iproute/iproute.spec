# lfs

%global name            iproute
%global major_name      %{name}2
%global version         6.16.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Advanced IP routing and network device configuration tools
License:        GPLv2+ and Public Domain

Source0:        https://www.kernel.org/pub/linux/utils/net/%{major_name}/%{major_name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  bison


%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The iproute package contains networking utilities (ip and rtmon, for example)
which are designed to use the advanced networking capabilities of the Linux
kernel.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{major_name}-%{version}

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
/usr/include/*
/usr/lib/tc
/usr/sbin/*
/usr/share/bash-completion/completions/*
/usr/share/%{major_name}

%else
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

%files devel
/usr/include/%{major_name}

%files man
/usr/share/man/man*/*.gz

%endif
