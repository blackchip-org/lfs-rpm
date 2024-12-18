Name:           dbus
Version:        1.14.10
Release:        1%{?dist}
Summary:        D-BUS message bus
License:        (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later

Source0:        https://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz

%description
D-BUS is a system for sending messages between applications. It is used both
for the system-wide message bus service, and as a per-user-login-session
messaging facility.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr                        \
            --sysconfdir=/etc                    \
            --localstatedir=/var                 \
            --runstatedir=/run                   \
            --enable-user-session                \
            --disable-static                     \
            --disable-doxygen-docs               \
            --disable-xml-docs                   \
            --docdir=/usr/share/doc/dbus-%{version}  \
            --with-system-socket=/run/dbus/system_bus_socket
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

mkdir -p                %{buildroot}/var/lib
ln -sfv /etc/machine-id %{buildroot}/var/lib/dbus

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
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
/usr/share/doc/dbus-%{version}
/usr/share/dbus-1
/usr/share/xml/dbus-1
/var/lib/dbus/machine-id

%defattr(755,root,root,755)
/usr/lib/libdbus-1.so.3.*
