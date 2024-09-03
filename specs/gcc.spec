%bcond_with     lfs_gcc_libstdcpp_only

Name:           %{!?with_lfs_gcc_libstdcpp_only:gcc}%{?with_lfs_gcc_libstdcpp_only:libstdc++}
Version:        14.2.0
Release:        1%{?dist}
Summary:        Various compilers (C, C++, Objective-C, ...)
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD

Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

%global         glibc_version   2.40

%if %{with lfs_stage1}
%global         mpfr_version    4.2.1
%global         gmp_version     6.3.0
%global         mpc_version     1.3.1

Source1:        https://ftp.gnu.org/gnu/mpfr/mpfr-%{mpfr_version}.tar.xz
Source2:        https://ftp.gnu.org/gnu/gmp/gmp-%{gmp_version}.tar.xz
Source3:        https://ftp.gnu.org/gnu/mpc/mpc-%{mpc_version}.tar.gz
%endif

%description
The gcc package contains the GNU Compiler Collection version 8. You'll need
this package in order to compile C code.

#---------------------------------------------------------------------------
%prep
cat <<EOF
package name:           %{name}
lfs_stage1:             %{?with_lfs_stage1}
lfs_gcc_libstdcpp_only: %{?with_lfs_gcc_libstdcpp_only}
EOF

%setup -q -n gcc-%{version}

%if %{with lfs_stage1}
tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}

mv mpfr-%{mpfr_version}  mpfr
mv gmp-%{gmp_version}    gmp
mv mpc-%{mpc_version}    mpc
%endif

#---------------------------------------------------------------------------
%build
%lfs_build_begin

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

mkdir build
cd build

%if %{with lfs_gcc_libstdcpp_only}
../libstdc++-v3/configure           \
    --host=%{lfs_tgt}               \
    --build=$(../config.guess)      \
    --prefix=/usr                   \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/%{lfs_tgt}/include/c++/%{version}

%elif %{with lfs_stage1a}
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
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd build

%if %{with lfs_gcc_libstdcpp_only}
DESTDIR=%{buildroot}/%{lfs_dir} %make install
rm -v %{buildroot}/%{lfs_dir}/usr/lib/lib{stdc++,stdc++fs,supc++}.la

%elif %{with lfs_stage1a}
DESTDIR=%{buildroot} %make install
cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
  %{buildroot}/%{lfs_tools_dir}/lib/gcc/%{lfs_tgt}/%{version}/include/limits.h

%elif %{with lfs_stage1b}
DESTDIR=%{buildroot}/%{lfs_dir} %make install
ln -sv gcc %{buildroot}/%{lfs_dir}/usr/bin/cc

%else
make DESTDIR=%{buildroot} install
ln -svr /usr/bin/cpp %{buildroot}/usr/lib
ln -sv gcc %{buildroot}/usr/bin/cc
ln -sv gcc.1 %{buildroot}/usr/share/man/man1/cc.1
mkdir %{buildroot}/usr/lib/bfd-plugins/
ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/%{version}/liblto_plugin.so \
        %{buildroot}/usr/lib/bfd-plugins/
mkdir -pv %{buildroot}/usr/share/gdb/auto-load/usr/lib
mv -v %{buildroot}/usr/lib/*gdb.py %{buildroot}/usr/share/gdb/auto-load/usr/lib

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%check
cd build
ulimit -s 32768
%make -k check

#---------------------------------------------------------------------------
%files
%if %{with lfs_gcc_libstdcpp_only}
%{lfs_tools_dir}/%{lfs_tgt}/include/c++/%{version}
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/share/gcc-%{version}/python

%elif %{with lfs_stage1a}
%{lfs_tools_dir}/bin/*
%{lfs_tools_dir}/lib/gcc/%{lfs_tgt}/%{version}
%{lfs_tools_dir}/lib64/*
%{lfs_tools_dir}/libexec/gcc/%{lfs_tgt}/%{version}

%elif %{with lfs_stage1b}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/c++/%{version}
%{lfs_dir}/usr/lib/gcc/%{lfs_tgt}/%{version}
%{lfs_dir}/usr/lib/*.{so*,a,spec}
%{lfs_dir}/usr/libexec/gcc/%{lfs_tgt}/%{version}
%{lfs_dir}/usr/share/gcc-%{version}

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
/usr/bin/x86_64-pc-linux-gnu-c++
/usr/bin/x86_64-pc-linux-gnu-g++
/usr/bin/x86_64-pc-linux-gnu-gcc
/usr/bin/x86_64-pc-linux-gnu-gcc-%{version}
/usr/bin/x86_64-pc-linux-gnu-gcc-ar
/usr/bin/x86_64-pc-linux-gnu-gcc-nm
/usr/bin/x86_64-pc-linux-gnu-gcc-ranlib
/usr/include/c++/%{version}
/usr/lib/bfd-plugins/liblto_plugin.so
/usr/lib/cpp
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/*.{o,a}
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/include
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/install-tools
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/gtype.state
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/include
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/libcc1plugin.so
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/libcc1plugin.so.0
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/libcp1plugin.so
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/libcp1plugin.so.0
/usr/lib/libasan.a
/usr/lib/libasan.so
/usr/lib/libasan.so.8
/usr/lib/libasan_preinit.o
/usr/lib/libatomic.a
/usr/lib/libatomic.so
/usr/lib/libatomic.so.1
/usr/lib/libcc1.so
/usr/lib/libcc1.so.0
/usr/lib/libgcc_s.so
/usr/lib/libgcc_s.so.1
/usr/lib/libgomp.a
/usr/lib/libgomp.so
/usr/lib/libgomp.so.1
/usr/lib/libgomp.spec
/usr/lib/libhwasan.a
/usr/lib/libhwasan.so
/usr/lib/libhwasan.so.0
/usr/lib/libhwasan_preinit.o
/usr/lib/libitm.a
/usr/lib/libitm.so
/usr/lib/libitm.so.1
/usr/lib/libitm.spec
/usr/lib/liblsan.a
/usr/lib/liblsan.so
/usr/lib/liblsan.so.0
/usr/lib/liblsan_preinit.o
/usr/lib/libquadmath.a
/usr/lib/libquadmath.so
/usr/lib/libquadmath.so.0
/usr/lib/libsanitizer.spec
/usr/lib/libssp.a
/usr/lib/libssp.so
/usr/lib/libssp.so.0
/usr/lib/libssp_nonshared.a
/usr/lib/libstdc++.a
/usr/lib/libstdc++.so
/usr/lib/libstdc++.so.6
/usr/lib/libstdc++exp.a
/usr/lib/libstdc++fs.a
/usr/lib/libsupc++.a
/usr/lib/libtsan.a
/usr/lib/libtsan.so
/usr/lib/libtsan.so.2
/usr/lib/libtsan_preinit.o
/usr/lib/libubsan.a
/usr/lib/libubsan.so
/usr/lib/libubsan.so.1
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/cc1
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/cc1plus
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/collect2
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/g++-mapper-server
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/install-tools/mkinstalldirs
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/liblto_plugin.so
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/lto-wrapper
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/lto1
/usr/libexec/gcc/x86_64-pc-linux-gnu/%{version}/plugin/gengtype
/usr/share/gcc-%{version}
/usr/share/gdb/auto-load/usr/lib/libstdc++.so.6.0.33-gdb.py
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man{1,7}/*

%defattr(755,root,root,755)
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/libcc1plugin.so.0.0.0
/usr/lib/gcc/x86_64-pc-linux-gnu/%{version}/plugin/libcp1plugin.so.0.0.0
/usr/lib/libasan.so.8.0.0
/usr/lib/libatomic.so.1.2.0
/usr/lib/libcc1.so.0.0.0
/usr/lib/libgomp.so.1.0.0
/usr/lib/libhwasan.so.0.0.0
/usr/lib/libitm.so.1.0.0
/usr/lib/liblsan.so.0.0.0
/usr/lib/libquadmath.so.0.0.0
/usr/lib/libssp.so.0.0.0
/usr/lib/libstdc++.so.6.0.33
/usr/lib/libtsan.so.2.0.0
/usr/lib/libubsan.so.1.0.0

%endif
