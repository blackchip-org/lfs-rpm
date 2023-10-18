%global version     2.38
%global lfs_version 12.0

Name:           glibc
Version:        %{version}
Release:        1%{?dist}
Summary:        The GNU libc libraries
License:        LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL

Source0:        https://ftp.gnu.org/gnu/glibc/glibc-%{version}.tar.xz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/glibc-%{version}-fhs-1.patch
Patch1:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/glibc-%{version}-memalign_fix-1.patch


%description
The glibc package contains standard libraries which are used by multiple
programs on the system. In order to save disk space and memory, as well as to
make upgrading easier, common system code is kept in one place and shared
between programs. This particular package contains the most important sets of
shared libraries: the standard C library and the standard math library. Without
these two libraries, a Linux system will not function.


%global _build_id_links none


%prep
%setup -q
%patch 0 -p1
%patch 1 -p1


%build
mkdir -v build
cd       build

echo "rootsbindir=/usr/sbin" > configparms

../configure --prefix=/usr                            \
             --disable-werror                         \
             --enable-kernel=4.14                     \
             --enable-stack-protector=strong          \
             --with-headers=/usr/include              \
             libc_cv_slibdir=/usr/lib
make


# %check
# cd build
# make check


%install
cd build
sed '/test-installation/s@$(PERL)@echo not running@' -i ../Makefile
make DESTDIR=%{buildroot} install
sed '/RTLDLIST=/s@/usr@@g' -i %{buildroot}/usr/bin/ldd
cp -v ../nscd/nscd.conf %{buildroot}/etc/nscd.conf
mkdir -pv %{buildroot}/var/cache/nscd
install -v -Dm644 ../nscd/nscd.tmpfiles %{buildroot}/usr/lib/tmpfiles.d/nscd.conf
install -v -Dm644 ../nscd/nscd.service %{buildroot}/usr/lib/systemd/system/nscd.service
mkdir -pv %{buildroot}/usr/lib/locale

cat > %{buildroot}/etc/nsswitch.conf << "EOF"
# Begin /etc/nsswitch.conf

passwd: files
group: files
shadow: files

hosts: files dns
networks: files

protocols: files
services: files
ethers: files
rpc: files

# End /etc/nsswitch.conf
EOF

cat > %{buildroot}/etc/ld.so.conf << "EOF"
# Begin /etc/ld.so.conf
/usr/local/lib
/opt/lib

EOF

cat >> %{buildroot}/etc/ld.so.conf << "EOF"
# Add an include directory
include /etc/ld.so.conf.d/*.conf

EOF
mkdir -pv %{buildroot}/etc/ld.so.conf.d
rm %{buildroot}/usr/share/info/dir 


%files
/etc/ld.so.cache
/etc/ld.so.conf
/etc/ld.so.conf.d
/etc/nscd.conf
/etc/nsswitch.conf
/etc/rpc
/usr/bin/gencat
/usr/bin/getconf
/usr/bin/getent
/usr/bin/iconv
/usr/bin/ld.so
/usr/bin/ldd
/usr/bin/locale
/usr/bin/localedef
/usr/bin/makedb
/usr/bin/mtrace
/usr/bin/pcprofiledump
/usr/bin/pldd
/usr/bin/sotruss
/usr/bin/sprof
/usr/bin/tzselect
/usr/bin/xtrace
/usr/bin/zdump
/usr/include/* 
/usr/lib/Mcrt1.o
/usr/lib/Scrt1.o
/usr/lib/crt1.o
/usr/lib/crti.o
/usr/lib/crtn.o
/usr/lib/gcrt1.o
/usr/lib/grcrt1.o
/usr/lib/libBrokenLocale.a
/usr/lib/libBrokenLocale.so
/usr/lib/libanl.a
/usr/lib/libanl.so
/usr/lib/libc.a
/usr/lib/libc.so
/usr/lib/libc_malloc_debug.so
/usr/lib/libc_nonshared.a
/usr/lib/libdl.a
/usr/lib/libg.a
/usr/lib/libm-2.38.a
/usr/lib/libm.a
/usr/lib/libm.so
/usr/lib/libmcheck.a
/usr/lib/libmemusage.so
/usr/lib/libmvec.a
/usr/lib/libmvec.so
/usr/lib/libnss_compat.so
/usr/lib/libnss_db.so
/usr/lib/libnss_hesiod.so
/usr/lib/libpcprofile.so
/usr/lib/libpthread.a
/usr/lib/libresolv.a
/usr/lib/libresolv.so
/usr/lib/librt.a
/usr/lib/libthread_db.so
/usr/lib/libutil.a
/usr/lib/rcrt1.o
/usr/lib/{audit,gconv}
/usr/lib/systemd/system/nscd.service
/usr/lib/tmpfiles.d/nscd.conf
/usr/libexec/getconf
/usr/sbin/iconvconfig
/usr/sbin/ldconfig
/usr/sbin/nscd
/usr/sbin/sln
/usr/sbin/zic
/usr/share/i18n/charmaps/*
/usr/share/i18n/locales/*
/usr/share/info/libc*
/usr/share/locale/*/LC_MESSAGES/libc.mo
/usr/share/locale/locale.alias
/var/lib/nss_db/Makefile

%defattr(755,root,root,755) 
/usr/lib/ld-linux-x86-64.so.2
/usr/lib/libanl.so.1
/usr/lib/libBrokenLocale.so.1
/usr/lib/libc.so.6
/usr/lib/libc_malloc_debug.so.0
/usr/lib/libdl.so.2
/usr/lib/libm.so.6
/usr/lib/libmvec.so.1
/usr/lib/libnsl.so.1
/usr/lib/libnss_compat.so.2
/usr/lib/libnss_db.so.2
/usr/lib/libnss_dns.so.2
/usr/lib/libnss_files.so.2
/usr/lib/libnss_hesiod.so.2
/usr/lib/libpthread.so.0
/usr/lib/libresolv.so.2
/usr/lib/librt.so.1
/usr/lib/libthread_db.so.1
/usr/lib/libutil.so.1


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package