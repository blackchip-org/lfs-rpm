Name:           psmisc
Version:        23.7
Release:        1%{?dist}
Summary:        Utilities for managing processes on your system
License:        GPLv2+

Source0:        https://sourceforge.net/projects/psmisc/files/psmisc/psmisc-%{version}.tar.xz

%description
The psmisc package contains utilities for managing processes on your system:
pstree, killall, fuser and pslog. The pstree command displays a tree structure
of all of the running processes on your system. The killall command sends a
specified signal (SIGTERM if nothing is specified) to processes identified by
name. The fuser command identifies the PIDs of processes that are using
specified files or filesystems. The pslog command shows the path of log files
owned by a given process.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr
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
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/{da,de,fr,hr,ko,pt_BR,ro,ru,sr,sv,uk}/man1/*
/usr/share/man/man1/*
