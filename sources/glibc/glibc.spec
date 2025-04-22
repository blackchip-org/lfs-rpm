# lfs

%global name    glibc
%global version 2.41
%global release 1

%global enable_kernel   5.4

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU libc libraries
License:        LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL

Source0:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256
Source2:        ld.so.conf
Source3:        nsswitch.conf

%if !%{with %lfs_stage1}
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/%{name}-%{version}-fhs-1.patch
%endif

BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  texinfo
BuildRequires:  python
Provides:       rtld(GNU_HASH)
Suggests:       %{name}-doc = %{version}

%description
The glibc package contains standard libraries which are used by multiple
programs on the system. In order to save disk space and memory, as well as to
make upgrading easier, common system code is kept in one place and shared
between programs. This particular package contains the most important sets of
shared libraries: the standard C library and the standard math library. Without
these two libraries, a Linux system will not function.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q
cp ${SOURCE2} %{SOURCE3} .

%if !%{with %lfs_stage1}
%patch 0 -p1
%endif

#---------------------------------------------------------------------------
%build
mkdir    build
cd       build

echo "rootsbindir=/usr/sbin" > configparms

%if %{with lfs_stage1}
../configure --prefix=/usr                         \
             --host=%{lfs_tgt}                     \
             --build=$(../scripts/config.guess)    \
             --enable-kernel=%{enable_kernel}      \
             --with-headers=%{lfs_dir}/usr/include \
             --disable-nscd                        \
             libc_cv_slibdir=/usr/lib

%else
../configure --prefix=/usr                            \
             --disable-werror                         \
             --enable-kernel=%{enable_kernel}         \
             --enable-stack-protector=strong          \
             libc_cv_slibdir=/usr/lib

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build

DESTDIR=%{buildroot}/%{?lfs_dir} make install

%if %{with lfs_stage1}
sed '/RTLDLIST=/s@/usr@@g' -i %{buildroot}/%{lfs_dir}/usr/bin/ldd
%endif

case %{_arch} in
    i?86)   mkdir -p              %{buildroot}/%{?lfs_dir}/lib
            ln -sfv ld-linux.so.2 %{buildroot}/%{?lfs_dir}/lib/ld-lsb.so.3
    ;;
    x86_64) mkdir -p %{buildroot}/%{lfs_dir}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{?lfs_dir}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{?lfs_dir}/lib64/ld-lsb-x86-64.so.3
    ;;
esac

%if %{with lfs}
rm -rf  %{buildroot}/%{?lfs_dir}/var
rm -rf  %{buildroot}/%{?lfs_dir}/usr/lib/{locale,systemd,tmpfiles.d}
%endif

%if !%{with lfs_stage1}
sed '/test-installation/s@$(PERL)@echo not running@' -i ../Makefile
make DESTDIR=%{buildroot} install

sed         '/RTLDLIST=/s@/usr@@g' -i %{buildroot}/usr/bin/ldd
cp -v       ../nscd/nscd.conf %{buildroot}/etc/nscd.conf
mkdir -pv   %{buildroot}/var/cache/nscd

install -v -Dm644 ../nscd/nscd.tmpfiles %{buildroot}/usr/lib/tmpfiles.d/nscd.conf
install -v -Dm644 ../nscd/nscd.service %{buildroot}/usr/lib/systemd/system/nscd.service

install -D -m 644 nsswitch.conf %{buildroot}/etc/nsswitch.conf
install -D -m 644 ld.so.conf    %{buildroot}/etc/ld.so.conf
%endif

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%if !%{with lfs_stage1}
%transfiletriggerin -P 2000000 -- /lib /usr/lib
/sbin/ldconfig

%transfiletriggerpostun -P 2000000 -- /lib /usr/lib
/sbin/ldconfig

%endif

#---------------------------------------------------------------------------
%files

%if %{with lfs}
%{?lfs_dir}/lib64/*
%{?lfs_dir}/etc/*
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*.{a,o,so*}
%{?lfs_dir}/usr/lib/{audit,gconv}
%{?lfs_dir}/usr/libexec/*
%{?lfs_dir}/usr/sbin/*
%{?lfs_dir}/usr/share/i18n/charmaps
%{?lfs_dir}/usr/share/i18n/locales

%else
/etc/ld.so.cache
/etc/ld.so.conf
/etc/ld.so.conf.d
/etc/nscd.conf
/etc/nsswitch.conf
/etc/rpc
/lib64/ld-linux-x86-64.so.2
/lib64/ld-lsb-x86-64.so.3
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
%shlib /usr/lib/ld-linux-x86-64.so.2
/usr/lib/libBrokenLocale.a
/usr/lib/libBrokenLocale.so
%shlib /usr/lib/libBrokenLocale.so.1
/usr/lib/libanl.a
/usr/lib/libanl.so
%shlib /usr/lib/libanl.so.1
/usr/lib/libc.a
/usr/lib/libc.so
%shlib /usr/lib/libc.so.6
/usr/lib/libc_malloc_debug.so
%shlib /usr/lib/libc_malloc_debug.so.0
/usr/lib/libc_nonshared.a
/usr/lib/libdl.a
%shlib /usr/lib/libdl.so.2
/usr/lib/libg.a
/usr/lib/libm-%{version}.a
/usr/lib/libm.a
/usr/lib/libm.so
%shlib /usr/lib/libm.so.6
/usr/lib/libmcheck.a
/usr/lib/libmemusage.so
/usr/lib/libmvec.a
/usr/lib/libmvec.so
%shlib /usr/lib/libmvec.so.1
%shlib /usr/lib/libnsl.so.1
/usr/lib/libnss_compat.so
%shlib /usr/lib/libnss_compat.so.2
/usr/lib/libnss_db.so
%shlib /usr/lib/libnss_db.so.2
%shlib /usr/lib/libnss_dns.so.2
%shlib /usr/lib/libnss_files.so.2
/usr/lib/libnss_hesiod.so
%shlib /usr/lib/libnss_hesiod.so.2
/usr/lib/libpcprofile.so
/usr/lib/libpthread.a
%shlib /usr/lib/libpthread.so.0
/usr/lib/libresolv.a
/usr/lib/libresolv.so
%shlib /usr/lib/libresolv.so.2
/usr/lib/librt.a
%shlib /usr/lib/librt.so.1
/usr/lib/libthread_db.so
%shlib /usr/lib/libthread_db.so.1
/usr/lib/libutil.a
%shlib /usr/lib/libutil.so.1
/usr/lib/locale/locale-archive
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
/var/lib/nss_db/Makefile

%files lang
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/locale/locale.alias

%files doc
/usr/share/info/*

%endif

