%define version   23.6

Name:           psmisc
Version:        %{version}
Release:        1%{?dist}
Summary:        Utilities for managing processes on your system
License:        GPLv2+

Source0:        https://sourceforge.net/projects/psmisc/files/psmisc/psmisc-%{version}.tar.xz

%global _build_id_links none

%description
The psmisc package contains utilities for managing processes on your system:
pstree, killall, fuser and pslog. The pstree command displays a tree structure
of all of the running processes on your system. The killall command sends a
specified signal (SIGTERM if nothing is specified) to processes identified by
name. The fuser command identifies the PIDs of processes that are using
specified files or filesystems. The pslog command shows the path of log files
owned by a given process.


%prep
%setup -q


%build
./configure --prefix=/usr
make


%check
make check


%install
make DESTDIR=%{buildroot} install



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


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4-1
- Initial package


