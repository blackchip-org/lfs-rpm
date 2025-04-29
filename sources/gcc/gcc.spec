# lfs

%global name            gcc
%global version         14.2.0
%global release         1

%global glibc_version   2.40
%global mpfr_version    4.2.1
%global gmp_version     6.3.0
%global mpc_version     1.3.1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Various compilers (C, C++, Objective-C, ...)
License:        GPLv3+ and GPLv3+ with ewith-glibc-verxceptions and GPLv2+ with exceptions and LGPLv2+ and BSD

Source:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if %{with lfs}
Source2:        https://ftp.gnu.org/gnu/mpfr/mpfr-%{mpfr_version}.tar.xz
Source3:        https://ftp.gnu.org/gnu/gmp/gmp-%{gmp_version}.tar.xz
Source4:        https://ftp.gnu.org/gnu/mpc/mpc-%{mpc_version}.tar.gz

%endif

BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  mpc-devel

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

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

%endif

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C,
Fortran, Ada, Go, D and Modula-2 as well as libraries for these languages
(libstdc++,...). GCC was originally written as the compiler for the GNU
operating system. The GNU system was developed to be 100% free software, free
in the sense that it respects the user's freedom.

%if !%{with lfs}
%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n gcc-%{version}

%if %{with lfs_stage1}
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}
tar -xf %{SOURCE4}

mv mpfr-%{mpfr_version}  mpfr
mv gmp-%{gmp_version}    gmp
mv mpc-%{mpc_version}    mpc
%endif

#---------------------------------------------------------------------------
%build

case %{_arch} in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

mkdir build
cd build

%if %{with lfs_stage1a}
../configure                              \
    --target=%{lfs_tgt}                   \
    --prefix=%{lfs_tools_dir}             \
    --with-glibc-version=%{glibc_version} \
    --with-sysroot=%{lfs_dir}             \
    --with-newlib                         \
    --without-headers                     \
    --enable-default-pie                  \
    --enable-default-ssp                  \
    --disable-nls                         \
    --disable-shared                      \
    --disable-multilib                    \
    --disable-threads                     \
    --disable-libatomic                   \
    --disable-libgomp                     \
    --disable-libquadmath                 \
    --disable-libssp                      \
    --disable-libvtv                      \
    --disable-libstdcxx                   \
    --enable-languages=c,c++


%elif %{with lfs_stage1b}
sed '/thread_header =/s/@.*@/gthr-posix.h/' \
    -i ../libgcc/Makefile.in ../libstdc++-v3/include/Makefile.in
../configure                                       \
    --build=$(../config.guess)                     \
    --host=%{lfs_tgt}                              \
    --target=%{lfs_tgt}                            \
    LDFLAGS_FOR_TARGET=-L$PWD/%{lfs_tgt}/libgcc    \
    --prefix=/usr                                  \
    --with-build-sysroot=%{lfs_dir}                \
    --enable-default-pie                           \
    --enable-default-ssp                           \
    --disable-nls                                  \
    --disable-multilib                             \
    --disable-libatomic                            \
    --disable-libgomp                              \
    --disable-libquadmath                          \
    --disable-libsanitizer                         \
    --disable-libssp                               \
    --disable-libvtv                               \
    --enable-languages=c,c++

%else
../configure --prefix=/usr            \
             LD=ld                    \
             --enable-languages=c,c++ \
             --enable-default-pie     \
             --enable-default-ssp     \
             --enable-host-pie        \
             --disable-multilib       \
             --disable-bootstrap      \
             --disable-fixincludes    \
             --with-system-zlib
%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install

cd build

%if %{with lfs_stage1a}
DESTDIR=%{buildroot} make install
cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
    %{buildroot}/%{lfs_tools_dir}/lib/gcc/%{lfs_tgt}/%{version}/include/limits.h

%elif %{with lfs_stage1b}
DESTDIR=%{buildroot}/%{lfs_dir} make install
ln -sv gcc %{buildroot}/%{lfs_dir}/usr/bin/cc

%else
make %{?_smp_mflags} DESTDIR=%{buildroot} install

ln -svr /usr/bin/cpp %{buildroot}/usr/lib
ln -sv  gcc %{buildroot}/usr/bin/cc
ln -sv  gcc.1 %{buildroot}/usr/share/man/man1/cc.1

mkdir   %{buildroot}/usr/lib/bfd-plugins/
ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/%{version}/liblto_plugin.so \
        %{buildroot}/usr/lib/bfd-plugins/

mkdir   -pv %{buildroot}/usr/share/gdb/auto-load/usr/lib
mv -v   %{buildroot}/usr/lib/*gdb.py %{buildroot}/usr/share/gdb/auto-load/usr/lib

%endif

#---------------------------------------------------------------------------
%check
cd build
ulimit -s 32768
make -k check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1a}
%{lfs_tools_dir}/bin/*
%{lfs_tools_dir}/lib64/*
%{lfs_tools_dir}/lib/gcc/%{lfs_tgt}/%{version}
%{lfs_tools_dir}/libexec/gcc/%{lfs_tgt}/%{version}

%elif %{with lfs_stage1b}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/c++/%{version}
%{lfs_dir}/usr/lib/*.{so*,a,spec}
%{lfs_dir}/usr/lib/gcc
%{lfs_dir}/usr/libexec/gcc
%{lfs_dir}/usr/share/gcc-%{version}

%elif %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/c++/%{version}
%{?lfs_dir}/usr/lib/*.{so*,a,spec,o}
%{?lfs_dir}/usr/lib/{bfd-plugins,cpp,gcc}
%{?lfs_dir}/usr/share/gcc-%{version}
%{?lfs_dir}/usr/share/gdb
%{?lfs_dir}/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}

%else
/usr/bin/c++
/usr/bin/cc
/usr/bin/cpp
/usr/bin/g++
/usr/bin/gcc
/usr/bin/gcc-ar
/usr/bin/gcc-nm
/usr/bin/gcc-ranlib
/usr/bin/gcov
/usr/bin/gcov-dump
/usr/bin/gcov-tool
/usr/bin/lto-dump
/usr/bin/%{_arch}-pc-linux-gnu-c++
/usr/bin/%{_arch}-pc-linux-gnu-g++
/usr/bin/%{_arch}-pc-linux-gnu-gcc
/usr/bin/%{_arch}-pc-linux-gnu-gcc-%{version}
/usr/bin/%{_arch}-pc-linux-gnu-gcc-ar
/usr/bin/%{_arch}-pc-linux-gnu-gcc-nm
/usr/bin/%{_arch}-pc-linux-gnu-gcc-ranlib
/usr/lib/bfd-plugins/liblto_plugin.so
/usr/lib/cpp
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/*.{o,a}
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/include
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/install-tools
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/plugin/gtype.state
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/plugin/include
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/plugin/libcc1plugin.so*
/usr/lib/gcc/%{_arch}-pc-linux-gnu/%{version}/plugin/libcp1plugin.so*
/usr/lib/libatomic.a
/usr/lib/libatomic.so*
/usr/lib/libcc1.so*
/usr/lib/libgcc_s.so*
/usr/lib/libgomp.a
/usr/lib/libgomp.so*
/usr/lib/libgomp.spec
/usr/lib/libquadmath.a
/usr/lib/libquadmath.so*
/usr/lib/libssp.a
/usr/lib/libssp.so*
/usr/lib/libssp_nonshared.a
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/cc1
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/cc1plus
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/collect2
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/g++-mapper-server
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/install-tools/mkinstalldirs
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/liblto_plugin.so
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/lto-wrapper
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/lto1
/usr/libexec/gcc/%{_arch}-pc-linux-gnu/%{version}/plugin/gengtype
/usr/share/gcc-%{version}

# libstdc++
/usr/include/c++/%{version}
/usr/lib/libasan.a
/usr/lib/libasan.so*
/usr/lib/libasan_preinit.o
/usr/lib/libhwasan.a
/usr/lib/libhwasan.so*
/usr/lib/libhwasan_preinit.o
/usr/lib/libitm.a
/usr/lib/libitm.so*
/usr/lib/libitm.spec
/usr/lib/liblsan.a
/usr/lib/liblsan.so*
/usr/lib/liblsan_preinit.o
/usr/lib/libsanitizer.spec
/usr/lib/libstdc++.a
/usr/lib/libstdc++.so*
/usr/lib/libstdc++exp.a
/usr/lib/libstdc++fs.a
/usr/lib/libsupc++.a
/usr/lib/libtsan.a
/usr/lib/libtsan.so*
/usr/lib/libtsan_preinit.o
/usr/lib/libubsan.a
/usr/lib/libubsan.so*
/usr/share/gdb/auto-load/usr/lib/libstdc++.so.6.0.33-gdb.py

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man{1,7}/*.gz

%endif
