# lfs

%global name            util-linux
%global version_2       2.41
%global version         %{version_2}.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Collection of basic system utilities
License:        GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain

Source0:        https://www.kernel.org/pub/linux/utils/%{name}/v%{version_2}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, util-linux contains the fdisk configuration tool and the login
program.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
mkdir -pv %{buildroot}/var/lib/hwclock
./configure ADJTIME_PATH=/var/lib/hwclock/adjtime    \
            --bindir=/usr/bin     \
            --sbindir=/usr/sbin   \
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

%else
sed -i '/test_mkfds/s/^/#/' tests/helpers/Makemodule.am
autoreconf -f
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
            --without-python     \
            --disable-makeinstall-chown \
            --disable-makeinstall-setuid \
            --docdir=/usr/share/doc/util-linux-%{version}

%endif

make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/{blkid,libfdisk,libmount,libsmartcols,uuid}
/usr/lib/lib*.{so*,a}
/usr/lib/{pkgconfig,tmpfiles.d,sysusers.d}/*
/usr/sbin/*
/usr/share/bash-completion/completions/*
%if %{with lfs_stage2}
/usr/lib/systemd/system/*
%endif

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
/usr/lib/libblkid.so.*
/usr/lib/libfdisk.so.*
/usr/lib/libmount.so.*
/usr/lib/libsmartcols.so.*
/usr/lib/libuuid.so.*
/usr/lib/systemd/system/fstrim.service
/usr/lib/systemd/system/fstrim.timer
/usr/lib/systemd/system/uuidd.service
/usr/lib/systemd/system/uuidd.socket
/usr/lib/sysusers.d/uuidd-sysusers.conf
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
/usr/sbin/swaplabel
/usr/sbin/swapoff
/usr/sbin/swapon
/usr/sbin/switch_root
/usr/sbin/uuidd
/usr/sbin/wipefs
/usr/sbin/zramctl
/usr/share/bash-completion/completions/*

%if !%{with lfs}
/usr/sbin/sulogin
%endif

%files devel
/usr/include/blkid/blkid.h
/usr/include/libfdisk/libfdisk.h
/usr/include/libmount/libmount.h
/usr/include/libsmartcols/libsmartcols.h
/usr/include/uuid/uuid.h
/usr/lib/libblkid.so
/usr/lib/libfdisk.so
/usr/lib/libmount.so
/usr/lib/libsmartcols.so
/usr/lib/libuuid.so
/usr/lib/pkgconfig/blkid.pc
/usr/lib/pkgconfig/fdisk.pc
/usr/lib/pkgconfig/mount.pc
/usr/lib/pkgconfig/smartcols.pc
/usr/lib/pkgconfig/uuid.pc

%files doc
/usr/share/doc/%{name}-%{version}

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man{1,3,5,8}/*

%files static
/usr/lib/libblkid.a
/usr/lib/libfdisk.a
/usr/lib/libmount.a
/usr/lib/libsmartcols.a
/usr/lib/libuuid.a

%endif
