# lfs

%global name        dbus
%global version     1.16.0
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        D-BUS message bus
License:        (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later

Source0:        https://dbus.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  expat
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkg-config
BuildRequires:  systemd

%description
D-BUS is a system for sending messages between applications. It is used both
for the system-wide message bus service, and as a per-user-login-session
messaging facility.

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}

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
/etc/dbus-1
/usr/bin
/usr/include/dbus-1.0
/usr/lib/lib*.so*
/usr/lib/{cmake,dbus-1.0,pkgconfig,systemd,sysusers.d,tmpfiles.d}
/usr/libexec/dbus-daemon-launch-helper
/usr/share/dbus-1
/usr/share/xml/dbus-1
/var/lib/dbus/machine-id

%else
%config(noreplace) /etc/dbus-1/session.conf
%config(noreplace) /etc/dbus-1/system.conf
/usr/bin/dbus-cleanup-sockets
/usr/bin/dbus-daemon
/usr/bin/dbus-launch
/usr/bin/dbus-monitor
/usr/bin/dbus-run-session
/usr/bin/dbus-send
/usr/bin/dbus-test-tool
/usr/bin/dbus-update-activation-environment
/usr/bin/dbus-uuidgen
/usr/include/dbus-1.0
/usr/lib/cmake/DBus1
/usr/lib/dbus-1.0
/usr/lib/libdbus-1.so
/usr/lib/libdbus-1.so.3
%shlib /usr/lib/libdbus-1.so.3.38.3
/usr/lib/pkgconfig/dbus-1.pc
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
/usr/share/dbus-1
/usr/share/xml/dbus-1
/var/lib/dbus/machine-id

%files doc
/usr/share/doc/dbus

%endif
