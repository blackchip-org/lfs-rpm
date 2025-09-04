# lfs

%global name            glibc
%global version         2.42
%global release         1
%global enable_kernel   5.4

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU libc libraries
License:        LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL

Source0:         https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256
Source2:        ld.so.conf
Source3:        nsswitch.conf

%if !%{with %lfs_stage1}
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_url_version}/%{name}-%{version}-fhs-1.patch
%endif

BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  texinfo
BuildRequires:  python
Provides:       rtld(GNU_HASH)

%if !%{with lfs}
Recommends:     %{name}-info = %{version}

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

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The glibc package contains standard libraries which are used by multiple
programs on the system. In order to save disk space and memory, as well as to
make upgrading easier, common system code is kept in one place and shared
between programs. This particular package contains the most important sets of
shared libraries: the standard C library and the standard math library. Without
these two libraries, a Linux system will not function.

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q
cp %{SOURCE2} %{SOURCE3} .

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
             --disable-nscd                        \
              libc_cv_slibdir=/usr/lib             \
             --enable-kernel=%{enable_kernel}
%else
../configure --prefix=/usr                            \
             --disable-werror                         \
             --disable-nscd                           \
             libc_cv_slibdir=/usr/lib                 \
             --enable-stack-protector=strong          \
             --enable-kernel=%{enable_kernel}

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
    x86_64) mkdir -p %{buildroot}/%{?lfs_dir}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{?lfs_dir}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{?lfs_dir}/lib64/ld-lsb-x86-64.so.3
    ;;
esac

%if !%{with lfs_stage1}
sed '/test-installation/s@$(PERL)@echo not running@' -i ../Makefile
make DESTDIR=%{buildroot} install

sed         '/RTLDLIST=/s@/usr@@g' -i %{buildroot}/usr/bin/ldd

install -d -m 755 %{buildroot}/etc/ld.so.conf.d
install -d -m 755 %{buildroot}/etc/ld.so.conf.d

install -D -m 644 ../ld.so.conf    %{buildroot}/etc/ld.so.conf
install -D -m 644 ../nsswitch.conf %{buildroot}/etc/nsswitch.conf
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
%{?lfs_dir}/usr/lib/{audit,gconv,locale,systemd,tmpfiles.d}/*
%{?lfs_dir}/usr/libexec/*
%{?lfs_dir}/usr/sbin/*
%{?lfs_dir}/usr/share/i18n/charmaps
%{?lfs_dir}/usr/share/i18n/locales
%{?lfs_dir}/var/lib/nss_db

%else
/etc/ld.so.cache
/etc/ld.so.conf
%dir /etc/ld.so.conf.d
/etc/nsswitch.conf
/etc/rpc
/lib64/ld-linux-x86-64.so.*
/lib64/ld-lsb-x86-64.so.*
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
/usr/lib/Mcrt1.o
/usr/lib/Scrt1.o
/usr/lib/crt1.o
/usr/lib/crti.o
/usr/lib/crtn.o
/usr/lib/gcrt1.o
/usr/lib/grcrt1.o
/usr/lib/ld-linux-x86-64.so.*
/usr/lib/libBrokenLocale.so.*
/usr/lib/libanl.so.*
/usr/lib/libc.so.*
/usr/lib/libc_malloc_debug.so.*
/usr/lib/libdl.so.*
/usr/lib/libm.so.*
/usr/lib/libmemusage.so
/usr/lib/libmvec.so.*
/usr/lib/libnsl.so.*
/usr/lib/libnss_compat.so.*
/usr/lib/libnss_db.so.*
/usr/lib/libnss_dns.so.*
/usr/lib/libnss_files.so.*
/usr/lib/libnss_hesiod.so.*
/usr/lib/libpcprofile.so
/usr/lib/libpthread.so.*
/usr/lib/libresolv.so.*
/usr/lib/librt.so.*
/usr/lib/libthread_db.so.*
/usr/lib/libutil.so.*
%ghost /usr/lib/locale/locale-archive
/usr/lib/rcrt1.o
/usr/lib/{audit,gconv}
/usr/libexec/getconf
/usr/sbin/iconvconfig
/usr/sbin/ldconfig
/usr/sbin/sln
/usr/sbin/zic
/usr/share/i18n/charmaps
/usr/share/i18n/locales

%files devel
/usr/include/*
/usr/lib/libBrokenLocale.so
/usr/lib/libanl.so
/usr/lib/libc.so
/usr/lib/libc_malloc_debug.so
/usr/lib/libm.so
/usr/lib/libmvec.so
/usr/lib/libnss_compat.so
/usr/lib/libnss_db.so
/usr/lib/libnss_hesiod.so
/usr/lib/libresolv.so
/usr/lib/libthread_db.so
/var/lib/nss_db/Makefile

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/locale/locale.alias

%files static
/usr/lib/libBrokenLocale.a
/usr/lib/libanl.a
/usr/lib/libc.a
/usr/lib/libc_nonshared.a
/usr/lib/libdl.a
/usr/lib/libg.a
/usr/lib/libm-%{version}.a
/usr/lib/libm.a
/usr/lib/libmcheck.a
/usr/lib/libmvec.a
/usr/lib/libpthread.a
/usr/lib/libresolv.a
/usr/lib/librt.a
/usr/lib/libutil.a

%endif

