%define version     2.38
%define lfs_version 12.0

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

%files
/etc/ld.so.cache
/etc/ld.so.conf
/etc/ld.so.conf.d
/etc/nscd.conf
/etc/nsswitch.conf
/etc/rpc
/usr/bin/*
/usr/include/*
%attr(755,root,root) /usr/lib/*.so.*
/usr/lib/*.{a,o,so}
/usr/lib/{audit,gconv}
/usr/lib/systemd/system/nscd.service
/usr/lib/tmpfiles.d/nscd.conf
/usr/libexec/getconf
/usr/sbin/*
/usr/share/i18n/charmaps/*
/usr/share/i18n/locales/*
/usr/share/info/dir
/usr/share/info/libc*
/usr/share/locale/*/LC_MESSAGES/libc.mo
/usr/share/locale/locale.alias
/var/lib/nss_db/Makefile


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package