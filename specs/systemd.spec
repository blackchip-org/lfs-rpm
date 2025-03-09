Name:           systemd
Version:        257.3
Release:        1%{?dist}
Summary:        System and Service Manager
License:        LGPLv2+ and MIT and GPLv2+

Source0:        https://github.com/systemd/systemd/archive/v%{version}/systemd-%{version}.tar.gz
Source1:        https://anduin.linuxfromscratch.org/LFS/systemd-man-pages-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  python-Jinja2
BuildRequires:  ninja
Suggests:       %{name}-doc = %{version}

%description
systemd is a system and service manager that runs as PID 1 and starts the rest
of the system. It provides aggressive parallelization capabilities, uses socket
and D-Bus activation for starting services, offers on-demand starting of
daemons, keeps track of processes using Linux control groups, maintains mount
and automount points, and implements an elaborate transactional
dependency-based service control logic. systemd supports SysV and LSB init
scripts and works as a replacement for sysvinit. Other parts of this package
are a logging daemon, utilities to control basic system configuration like the
hostname, date, locale, maintain a list of logged-in users, system accounts,
runtime directories and settings, and daemons to manage simple network
configuration, network time synchronization, log forwarding, and name
resolution.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
sed -i -e 's/GROUP="render"/GROUP="video"/' \
       -e 's/GROUP="sgx", //' rules.d/50-udev-default.rules.in

mkdir -p build
cd       build

%if %{with lfs_stage2}
meson setup \
      --prefix=/usr                  \
      --buildtype=release            \
      -D default-dnssec=no           \
      -D firstboot=false             \
      -D install-tests=false         \
      -D ldconfig=false              \
      -D sysusers=false              \
      -D rpmmacrosdir=no             \
      -D homed=disabled              \
      -D userdb=false                \
      -D man=false                   \
      -D mode=release                \
      -D pamconfdir=no               \
      -D dev-kvm-mode=0660           \
      -D nobody-group=nogroup        \
      -D sysupdate=disabled          \
      -D ukify=disabled              \
      -D docdir=/usr/share/doc/systemd-%{version} \
      ..

%else
meson setup \
      --prefix=/usr                  \
      --buildtype=release            \
      -D default-dnssec=no           \
      -D firstboot=false             \
      -D install-tests=false         \
      -D ldconfig=false              \
      -D sysusers=false              \
      -D homed=disabled              \
      -D userdb=false                \
      -D mode=release                \
      -D pamconfdir=no               \
      -D dev-kvm-mode=0660           \
      -D nobody-group=nogroup        \
      -D sysupdate=disabled          \
      -D ukify=disabled              \
      -D docdir=/usr/share/doc/systemd-%{version} \
      ..
%endif

ninja

#---------------------------------------------------------------------------
%install
cd build
DESTDIR=%{buildroot} ninja install

mkdir -p %{buildroot}/usr/share/man
tar -xf %{SOURCE1} \
    --no-same-owner --strip-components=1   \
    -C %{buildroot}/usr/share/man

#---------------------------------------------------------------------------
%post
systemd-machine-id-setup
systemctl preset-all
systemctl disable systemd-sysupdate{,-reboot}

#---------------------------------------------------------------------------
%files
/etc/X11/xinit/xinitrc.d/50-systemd-user.sh
/etc/init.d/README
/etc/profile.d/70-systemd-shell-extra.sh
%config(noreplace) /etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf
%config(noreplace) /etc/systemd/coredump.conf
%config(noreplace) /etc/systemd/journald.conf
%config(noreplace) /etc/systemd/logind.conf
%config(noreplace) /etc/systemd/networkd.conf
%config(noreplace) /etc/systemd/oomd.conf
%config(noreplace) /etc/systemd/pstore.conf
%config(noreplace) /etc/systemd/resolved.conf
%config(noreplace) /etc/systemd/sleep.conf
%config(noreplace) /etc/systemd/system.conf
%config(noreplace) /etc/systemd/timesyncd.conf
%config(noreplace) /etc/systemd/user.conf
%config(noreplace) /etc/udev/iocost.conf
%config(noreplace) /etc/udev/udev.conf
%config(noreplace) /etc/xdg/systemd/user
/usr/bin/bootctl
/usr/bin/busctl
/usr/bin/coredumpctl
/usr/bin/hostnamectl
/usr/bin/journalctl
/usr/bin/kernel-install
/usr/bin/localectl
/usr/bin/loginctl
/usr/bin/machinectl
/usr/bin/networkctl
/usr/bin/oomctl
/usr/bin/portablectl
/usr/bin/resolvectl
/usr/bin/run0
/usr/bin/systemctl
/usr/bin/systemd-ac-power
/usr/bin/systemd-analyze
/usr/bin/systemd-ask-password
/usr/bin/systemd-cat
/usr/bin/systemd-cgls
/usr/bin/systemd-cgtop
/usr/bin/systemd-confext
/usr/bin/systemd-creds
/usr/bin/systemd-delta
/usr/bin/systemd-detect-virt
/usr/bin/systemd-dissect
/usr/bin/systemd-escape
/usr/bin/systemd-hwdb
/usr/bin/systemd-id128
/usr/bin/systemd-inhibit
/usr/bin/systemd-machine-id-setup
/usr/bin/systemd-mount
/usr/bin/systemd-notify
/usr/bin/systemd-nspawn
/usr/bin/systemd-path
/usr/bin/systemd-repart
/usr/bin/systemd-resolve
/usr/bin/systemd-run
/usr/bin/systemd-socket-activate
/usr/bin/systemd-stdio-bridge
/usr/bin/systemd-sysext
/usr/bin/systemd-tmpfiles
/usr/bin/systemd-tty-ask-password-agent
/usr/bin/systemd-umount
/usr/bin/systemd-vpick
/usr/bin/timedatectl
/usr/bin/udevadm
/usr/bin/varlinkctl
/usr/include/libudev.h
/usr/include/systemd
/usr/lib/environment.d/99-environment.conf
/usr/lib/kernel/install.conf
/usr/lib/kernel/install.d/50-depmod.install
/usr/lib/kernel/install.d/90-loaderentry.install
/usr/lib/kernel/install.d/90-uki-copy.install
/usr/lib/libnss_myhostname.so.2
/usr/lib/libnss_mymachines.so.2
/usr/lib/libnss_resolve.so.2
/usr/lib/libnss_systemd.so.2
/usr/lib/libsystemd.so
/usr/lib/libsystemd.so.0
%shlib /usr/lib/libsystemd.so.0.40.0
/usr/lib/libudev.so
/usr/lib/libudev.so.1
%shlib/usr/lib/libudev.so.1.7.10
/usr/lib/kernel/uki.conf
/usr/lib/modprobe.d/README
/usr/lib/modprobe.d/systemd.conf
/usr/lib/pkgconfig/libsystemd.pc
/usr/lib/pkgconfig/libudev.pc
/usr/lib/sysctl.d/50-coredump.conf
/usr/lib/sysctl.d/50-default.conf
/usr/lib/sysctl.d/50-pid-max.conf
/usr/lib/sysctl.d/README
/usr/lib/systemd
/usr/lib/tmpfiles.d
/usr/lib/udev
/usr/sbin/halt
/usr/sbin/init
/usr/sbin/mount.ddi
/usr/sbin/poweroff
/usr/sbin/reboot
/usr/sbin/resolvconf
/usr/sbin/runlevel
/usr/sbin/shutdown
/usr/sbin/telinit
/usr/share/bash-completion/completions/*
/usr/share/dbus-1
/usr/share/factory/etc/*
/usr/share/mime/packages/io.systemd.xml
/usr/share/pkgconfig/systemd.pc
/usr/share/pkgconfig/udev.pc
/usr/share/polkit-1/actions/*
/usr/share/polkit-1/rules.d/systemd-networkd.rules
/usr/share/systemd/kbd-model-map
/usr/share/systemd/language-fallback-map
/usr/share/zsh/site-functions/*

%if !%{with lfs_stage2}
%config(noreplace) /etc/systemd/journal-upload.conf
/usr/bin/importctl
/usr/lib/rpm/macros.d/macros.systemd
%endif

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/systemd-%{version}

%files man
/usr/share/man/man*/*
