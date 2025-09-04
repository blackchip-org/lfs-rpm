# lfs

%global name            dbus
%global major_name      dbus-1
%global major_name_2    %{major_name}.0
%global version         1.16.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        D-BUS message bus
License:        (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later

Source0:        https://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Requires:       shadow

BuildRequires:  expat-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconf
BuildRequires:  systemd-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%endif

%description
D-BUS is a system for sending messages between applications. It is used both
for the system-wide message bus service, and as a per-user-login-session
messaging facility.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%endif

# TODO: Build doxygen/xml docs

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build

meson setup --prefix=/usr \
            --buildtype=release \
            --wrap-mode=nofallback \
            ..
ninja

#---------------------------------------------------------------------------
%install
cd build
DESTDIR=%{buildroot} ninja install

mkdir -p                %{buildroot}/var/lib
ln -sfv /etc/machine-id %{buildroot}/var/lib/dbus

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/etc/%{major_name}/*
/usr/bin/*
/usr/include/%{major_name_2}
/usr/lib/lib*.so*
/usr/lib/{cmake,pkgconfig,systemd,sysusers.d,tmpfiles.d}/*
/usr/lib/%{major_name_2}
/usr/libexec/dbus-daemon-launch-helper
/usr/share/%{major_name}
/usr/share/xml/%{major_name}
/var/lib/dbus/machine-id

%else
%config(noreplace) /etc/%{major_name}/session.conf
%config(noreplace) /etc/%{major_name}/system.conf
/usr/bin/dbus-cleanup-sockets
/usr/bin/dbus-daemon
/usr/bin/dbus-launch
/usr/bin/dbus-monitor
/usr/bin/dbus-run-session
/usr/bin/dbus-send
/usr/bin/dbus-test-tool
/usr/bin/dbus-update-activation-environment
/usr/bin/dbus-uuidgen
/usr/lib/%{major_name_2}
/usr/lib/lib%{major_name}.so.*
/usr/lib/systemd/system/dbus.service
/usr/lib/systemd/system/dbus.socket
/usr/lib/systemd/system/multi-user.target.wants/dbus.service
/usr/lib/systemd/system/sockets.target.wants/dbus.socket
/usr/lib/systemd/user/dbus.service
/usr/lib/systemd/user/dbus.socket
/usr/lib/systemd/user/sockets.target.wants/dbus.socket
/usr/libexec/dbus-daemon-launch-helper
/usr/lib/sysusers.d/dbus.conf
/usr/lib/tmpfiles.d/dbus.conf
/usr/share/%{major_name}
/usr/share/xml/%{major_name}
/var/lib/dbus/machine-id

%files devel
/usr/include/%{major_name_2}
/usr/lib/cmake/DBus1
/usr/lib/lib%{major_name}.so
/usr/lib/pkgconfig/%{major_name}.pc

%files doc
/usr/share/doc/%{name}

%endif
