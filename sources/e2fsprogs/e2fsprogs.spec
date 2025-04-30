# lfs

%global name            e2fsprogs
%global version         1.47.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utilities for managing ext2, ext3, and ext4 file systems
License:        GPLv2

Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  pkgconf
BuildRequires:  systemd
BuildRequires:  texinfo

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package info
Summary:        Info documentation for %{name}
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
The e2fsprogs package contains a number of utilities for creating, checking,
modifying, and correcting any inconsistencies in second, third and fourth
extended (ext2/ext3/ext4) file systems. E2fsprogs contains e2fsck (used to
repair file system inconsistencies after an unclean shutdown), mke2fs (used to
initialize a partition to contain an empty ext2 file system), debugfs (used to
examine the internal structure of a file system, to manually repair a corrupted
file system, or to create test cases for e2fsck), tune2fs (used to modify file
system parameters), and most of the other core ext2fs file system utilities.

You should install the e2fsprogs package if you need to manage the performance
of an ext2, ext3, or ext4 file system.

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

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
mkdir -v build
cd       build

../configure --prefix=/usr           \
             --sysconfdir=/etc       \
             --enable-elf-shlibs     \
             --disable-libblkid      \
             --disable-libuuid       \
             --disable-uuidd         \
             --disable-fsck
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install

cd build
make DESTDIR=%{buildroot} install

%if %{with lfs}
rm -fv %{buildroot}/usr/lib/{libcom_err,libe2p,libext2fs,libss}.a

%else
chmod 644 %{buildroot}/usr/lib/*.a

%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/etc
/usr/bin
/usr/include
/usr/lib/{e2initrd_helper,pkgconfig,systemd,udev}
/usr/lib/lib*.so*
/usr/libexec/%{name}
/usr/sbin
/usr/share/{et,ss}

%else
%config(noreplace) /etc/e2scrub.conf
%config(noreplace) /etc/mke2fs.conf
/usr/bin/chattr
/usr/bin/compile_et
/usr/bin/lsattr
/usr/bin/mk_cmds
/usr/lib/e2initrd_helper
/usr/lib/libcom_err.so.*
/usr/lib/libe2p.so.*
/usr/lib/libext2fs.so.*
/usr/lib/libss.so.*
/usr/lib/systemd/system/e2scrub@.service
/usr/lib/systemd/system/e2scrub_all.service
/usr/lib/systemd/system/e2scrub_all.timer
/usr/lib/systemd/system/e2scrub_fail@.service
/usr/lib/systemd/system/e2scrub_reap.service
/usr/lib/udev/rules.d/64-ext4.rules
/usr/lib/udev/rules.d/96-e2scrub.rules
/usr/libexec/e2fsprogs/e2scrub_fail
/usr/sbin/badblocks
/usr/sbin/debugfs
/usr/sbin/dumpe2fs
/usr/sbin/e2freefrag
/usr/sbin/e2fsck
/usr/sbin/e2image
/usr/sbin/e2label
/usr/sbin/e2mmpstatus
/usr/sbin/e2scrub
/usr/sbin/e2scrub_all
/usr/sbin/e2undo
/usr/sbin/e4crypt
/usr/sbin/e4defrag
/usr/sbin/filefrag
/usr/sbin/fsck.ext2
/usr/sbin/fsck.ext3
/usr/sbin/fsck.ext4
/usr/sbin/logsave
/usr/sbin/mke2fs
/usr/sbin/mkfs.ext2
/usr/sbin/mkfs.ext3
/usr/sbin/mkfs.ext4
/usr/sbin/mklost+found
/usr/sbin/resize2fs
/usr/sbin/tune2fs
/usr/share/et/et_c.awk
/usr/share/et/et_h.awk
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed

%files devel
/usr/include/*.h
/usr/include/{e2p,et,ext2fs,ss}
/usr/lib/libcom_err.so
/usr/lib/libe2p.so
/usr/lib/libext2fs.so
/usr/lib/libss.so
/usr/lib/pkgconfig/com_err.pc
/usr/lib/pkgconfig/e2p.pc
/usr/lib/pkgconfig/ext2fs.pc
/usr/lib/pkgconfig/ss.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libcom_err.a
/usr/lib/libe2p.a
/usr/lib/libext2fs.a
/usr/lib/libss.a

%endif
