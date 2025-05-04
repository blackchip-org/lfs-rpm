# lfs

%global name            procps-ng
%global version         4.0.5
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        System and process monitoring utilities
License:        GPL+ and GPLv2 and GPLv2+ and GPLv3+ and LGPLv2+

Source0:        https://sourceforge.net/projects/%{name}/files/Production/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  pkgconf
BuildRequires:  systemd-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The procps package contains a set of system utilities that provide system
information. Procps includes ps, free, skill, pkill, pgrep, snice, tload, top,
uptime, vmstat, pidof, pmap, slabtop, w, watch, pwdx and pidwait.

The ps command displays a snapshot of running processes. The top command
provides a repetitive update of the statuses of running processes. The free
command displays the amounts of free and used memory on your system. The skill
command sends a terminate command (or another specified signal) to a specified
set of processes. The snice command is used to change the scheduling priority
of specified processes. The tload command prints a graph of the current system
load average to a specified tty. The uptime command displays the current time,
how long the system has been running, how many users are logged on, and system
load averages for the past one, five, and fifteen minutes. The w command
displays a list of the users who are currently logged on and what they are
running. The watch program watches a running program. The vmstat command
displays virtual memory statistics about processes, memory, paging, block I/O,
traps, and CPU activity. The pwdx command reports the current working directory
of a process or processes. The pidwait command waits for processes of specified
names.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description lang
Language files for %{name}

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
%if %{with lfs}
./configure --prefix=/usr                           \
            --docdir=/usr/share/doc/procps-ng-%{version} \
            --disable-static                        \
            --disable-kill                          \
            --with-systemd

%else
./configure --prefix=/usr                           \
            --docdir=/usr/share/doc/procps-ng-%{version} \
            --disable-kill                          \
            --with-systemd

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include/libproc2
/usr/lib/lib*.so*
/usr/lib/pkgconfig
/usr/sbin

%else
/usr/bin/free
/usr/bin/hugetop
/usr/bin/pgrep
/usr/bin/pidof
/usr/bin/pidwait
/usr/bin/pkill
/usr/bin/pmap
/usr/bin/ps
/usr/bin/pwdx
/usr/bin/slabtop
/usr/bin/tload
/usr/bin/top
/usr/bin/uptime
/usr/bin/vmstat
/usr/bin/w
/usr/bin/watch
/usr/lib/libproc2.so.*
/usr/sbin/sysctl

%files devel
/usr/include/libproc2
/usr/lib/libproc2.so
/usr/lib/pkgconfig/libproc2.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/procps-ng-%{version}

%files man
/usr/share/man/{??,pt_BR,zh_CN}/man*/*
/usr/share/man/man*/*

%files static
/usr/lib/libproc2.a

%endif