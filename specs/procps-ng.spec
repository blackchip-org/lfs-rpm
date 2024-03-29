Name:           procps-ng
Version:        4.0.3
Release:        1%{?dist}
Summary:        System and process monitoring utilities
License:        GPL+ and GPLv2 and GPLv2+ and GPLv3+ and LGPLv2+

Source0:        https://sourceforge.net/projects/procps-ng/files/Production/procps-ng-%{version}.tar.xz

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

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr                           \
            --docdir=/usr/share/doc/procps-ng-%{version} \
            --disable-static                        \
            --disable-kill                          \
            --with-systemd
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
/usr/bin/free
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
/usr/include/libproc2
/usr/lib/libproc2.so
/usr/lib/libproc2.so.0
/usr/lib/pkgconfig/libproc2.pc
/usr/sbin/sysctl
/usr/share/doc/procps-ng-%{version}
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/{??,pt_BR}/man{1,3,5,8}/*
/usr/share/man/man{1,3,5,8}/*

%defattr(755,root,root,755)
/usr/lib/libproc2.so.0.0.1
