Name:           e2fsprogs
Version:        1.47.0
Release:        1%{?dist}
Summary:        Utilities for managing ext2, ext3, and ext4 file systems
License:        GPLv2

Source0:        https://downloads.sourceforge.net/project/e2fsprogs/e2fsprogs/v%{version}/e2fsprogs-%{version}.tar.gz

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

#---------------------------------------------------------------------------
%prep 
%setup -q 

#---------------------------------------------------------------------------
%build 
%lfs_build_begin

mkdir -v build
cd       build

../configure --prefix=/usr           \
             --sysconfdir=/etc       \
             --enable-elf-shlibs     \
             --disable-libblkid      \
             --disable-libuuid       \
             --disable-uuidd         \
             --disable-fsck
%make 
%lfs_build_end

#---------------------------------------------------------------------------
%install 
%lfs_install_begin

cd build 
%make DESTDIR=%{buildroot} install 
rm -fv %{buildroot}/usr/lib/{libcom_err,libe2p,libext2fs,libss}.a
%lfs_install_end

#---------------------------------------------------------------------------
%check 
%make check 

#---------------------------------------------------------------------------
%files 
%config(noreplace) /etc/e2scrub.conf
%config(noreplace) /etc/mke2fs.conf
/usr/bin/chattr
/usr/bin/compile_et
/usr/bin/lsattr
/usr/bin/mk_cmds
/usr/include/*.h 
/usr/include/{e2p,et,ext2fs,ss}
/usr/lib/e2fsprogs/e2scrub_fail
/usr/lib/e2initrd_helper
/usr/lib/libcom_err.so
/usr/lib/libcom_err.so.2
/usr/lib/libe2p.so
/usr/lib/libe2p.so.2
/usr/lib/libext2fs.so
/usr/lib/libext2fs.so.2
/usr/lib/libss.so
/usr/lib/libss.so.2
/usr/lib/pkgconfig/com_err.pc
/usr/lib/pkgconfig/e2p.pc
/usr/lib/pkgconfig/ext2fs.pc
/usr/lib/pkgconfig/ss.pc
/usr/lib/systemd/system/e2scrub@.service
/usr/lib/systemd/system/e2scrub_all.service
/usr/lib/systemd/system/e2scrub_all.timer
/usr/lib/systemd/system/e2scrub_fail@.service
/usr/lib/systemd/system/e2scrub_reap.service
/usr/lib/udev/rules.d/96-e2scrub.rules
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
/usr/share/info/libext2fs.info.gz
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man{1,3,5,8}/*
/usr/share/ss/ct_c.awk
/usr/share/ss/ct_c.sed

%defattr(755,root,root,755)
/usr/lib/libcom_err.so.2.1
/usr/lib/libe2p.so.2.3
/usr/lib/libext2fs.so.2.4
/usr/lib/libss.so.2.0