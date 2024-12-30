Name:           util-linux
Version:        2.40.2
Release:        1%{?dist}
Summary:        Collection of basic system utilities
License:        GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain

%global         version2    2.40

Source:         https://www.kernel.org/pub/linux/utils/util-linux/v%{version2}/util-linux-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd
Suggests:       %{name}-doc = %{version}

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, util-linux contains the fdisk configuration tool and the login
program.

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
%if %{with lfs_stage1}
%use_lfs_tools
mkdir -pv %{buildroot}/var/lib/hwclock
./configure ADJTIME_PATH=/var/lib/hwclock/adjtime    \
            --libdir=/usr/lib     \
            --runstatedir=/run    \
            --disable-chfn-chsh   \
            --disable-login       \
            --disable-nologin     \
            --disable-su          \
            --disable-setpriv     \
            --disable-runuser     \
            --disable-pylibmount  \
            --disable-static      \
            --disable-liblastlog2 \
            --without-python      \
            --disable-makeinstall-chown \
            --disable-makeinstall-setuid \
            --docdir=/usr/share/doc/util-linux-%{version}
%make

%else
sed -i '/test_mkfds/s/^/#/' tests/helpers/Makemodule.am

./configure ADJTIME_PATH=/var/lib/hwclock/adjtime \
            --bindir=/usr/bin    \
            --libdir=/usr/lib    \
            --runstatedir=/run   \
            --sbindir=/usr/sbin  \
            --disable-chfn-chsh  \
            --disable-login      \
            --disable-nologin    \
            --disable-su         \
            --disable-setpriv    \
            --disable-runuser    \
            --disable-pylibmount \
            --disable-liblastlog2 \
            --disable-static     \
            --without-python     \
            --disable-makeinstall-chown \
            --disable-makeinstall-setuid \
            --docdir=/usr/share/doc/util-linux-%{version}
%make

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
/bin/*
/sbin/*
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/sbin/*
/usr/share/bash-completion/completions/*
/usr/share/locale/*/LC_MESSAGES/*.mo

%else
/usr/bin/cal
/usr/bin/chmem
/usr/bin/choom
/usr/bin/chrt
/usr/bin/col
/usr/bin/colcrt
/usr/bin/colrm
/usr/bin/column
/usr/bin/dmesg
/usr/bin/eject
/usr/bin/enosys
/usr/bin/exch
/usr/bin/fadvise
/usr/bin/fallocate
/usr/bin/fincore
/usr/bin/findmnt
/usr/bin/flock
/usr/bin/getopt
/usr/bin/hardlink
/usr/bin/hexdump
/usr/bin/i386
/usr/bin/ionice
/usr/bin/ipcmk
/usr/bin/ipcrm
/usr/bin/ipcs
/usr/bin/irqtop
/usr/bin/isosize
/usr/bin/kill
/usr/bin/last
/usr/bin/lastb
/usr/bin/linux32
/usr/bin/linux64
/usr/bin/logger
/usr/bin/look
/usr/bin/lsblk
/usr/bin/lsclocks
/usr/bin/lscpu
/usr/bin/lsfd
/usr/bin/lsipc
/usr/bin/lsirq
/usr/bin/lslocks
/usr/bin/lslogins
/usr/bin/lsmem
/usr/bin/lsns
/usr/bin/mcookie
/usr/bin/mesg
/usr/bin/more
/usr/bin/mount
/usr/bin/mountpoint
/usr/bin/namei
/usr/bin/nsenter
/usr/bin/pipesz
/usr/bin/prlimit
/usr/bin/rename
/usr/bin/renice
/usr/bin/rev
/usr/bin/script
/usr/bin/scriptlive
/usr/bin/scriptreplay
/usr/bin/setarch
/usr/bin/setpgid
/usr/bin/setsid
/usr/bin/setterm
/usr/bin/taskset
/usr/bin/uclampset
/usr/bin/ul
/usr/bin/umount
/usr/bin/uname26
/usr/bin/unshare
/usr/bin/utmpdump
/usr/bin/uuidgen
/usr/bin/uuidparse
/usr/bin/waitpid
/usr/bin/wall
/usr/bin/wdctl
/usr/bin/whereis
/usr/bin/x86_64
/usr/include/blkid/blkid.h
/usr/include/libfdisk/libfdisk.h
/usr/include/libmount/libmount.h
/usr/include/libsmartcols/libsmartcols.h
/usr/include/uuid/uuid.h
/usr/lib/libblkid.so
/usr/lib/libblkid.so.1
%shlib /usr/lib/libblkid.so.1.1.0
/usr/lib/libfdisk.so
/usr/lib/libfdisk.so.1
%shlib /usr/lib/libfdisk.so.1.1.0
/usr/lib/libmount.so
/usr/lib/libmount.so.1
%shlib /usr/lib/libmount.so.1.1.0
/usr/lib/libsmartcols.so
/usr/lib/libsmartcols.so.1
%shlib /usr/lib/libsmartcols.so.1.1.0
/usr/lib/libuuid.so
/usr/lib/libuuid.so.1
%shlib /usr/lib/libuuid.so.1.3.0
/usr/lib/pkgconfig/blkid.pc
/usr/lib/pkgconfig/fdisk.pc
/usr/lib/pkgconfig/mount.pc
/usr/lib/pkgconfig/smartcols.pc
/usr/lib/pkgconfig/uuid.pc
/usr/lib/systemd/system/fstrim.service
/usr/lib/systemd/system/fstrim.timer
/usr/lib/systemd/system/uuidd.service
/usr/lib/systemd/system/uuidd.socket
/usr/lib/tmpfiles.d/uuidd-tmpfiles.conf
/usr/sbin/addpart
/usr/sbin/agetty
/usr/sbin/blkdiscard
/usr/sbin/blkid
/usr/sbin/blkpr
/usr/sbin/blkzone
/usr/sbin/blockdev
/usr/sbin/cfdisk
/usr/sbin/chcpu
/usr/sbin/ctrlaltdel
/usr/sbin/delpart
/usr/sbin/fdisk
/usr/sbin/findfs
/usr/sbin/fsck
/usr/sbin/fsck.cramfs
/usr/sbin/fsck.minix
/usr/sbin/fsfreeze
/usr/sbin/fstrim
/usr/sbin/hwclock
/usr/sbin/ldattach
/usr/sbin/losetup
/usr/sbin/mkfs
/usr/sbin/mkfs.bfs
/usr/sbin/mkfs.cramfs
/usr/sbin/mkfs.minix
/usr/sbin/mkswap
/usr/sbin/partx
/usr/sbin/pivot_root
/usr/sbin/readprofile
/usr/sbin/resizepart
/usr/sbin/rfkill
/usr/sbin/rtcwake
/usr/sbin/sfdisk
/usr/sbin/sulogin
/usr/sbin/swaplabel
/usr/sbin/swapoff
/usr/sbin/swapon
/usr/sbin/switch_root
/usr/sbin/uuidd
/usr/sbin/wipefs
/usr/sbin/zramctl
/usr/share/bash-completion/completions/*

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/util-linux-%{version}

%files man
/usr/share/man/man{1,3,5,8}

%endif
