Name:           psmisc
Version:        23.7
Release:        1%{?dist}
Summary:        Utilities for managing processes on your system
License:        GPLv2+

Source:         https://sourceforge.net/projects/psmisc/files/psmisc/psmisc-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

%description
The psmisc package contains utilities for managing processes on your system:
pstree, killall, fuser and pslog. The pstree command displays a tree structure
of all of the running processes on your system. The killall command sends a
specified signal (SIGTERM if nothing is specified) to processes identified by
name. The fuser command identifies the PIDs of processes that are using
specified files or filesystems. The pslog command shows the path of log files
owned by a given process.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

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

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/man/{??,pt_BR}/man*/*
/usr/share/man/man*/*
