# lfs

%global name            psmisc
%global version         23.7
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utilities for managing processes on your system
License:        GPLv2+

Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The psmisc package contains utilities for managing processes on your system:
pstree, killall, fuser and pslog. The pstree command displays a tree structure
of all of the running processes on your system. The killall command sends a
specified signal (SIGTERM if nothing is specified) to processes identified by
name. The fuser command identifies the PIDs of processes that are using
specified files or filesystems. The pslog command shows the path of log files
owned by a given process.

%if !%{with lfs}
%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
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
/usr/bin/*

%else
/usr/bin/fuser
/usr/bin/killall
/usr/bin/peekfd
/usr/bin/prtstat
/usr/bin/pslog
/usr/bin/pstree
/usr/bin/pstree.x11

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/{??,pt_BR}/man*/*
/usr/share/man/man*/*

%endif