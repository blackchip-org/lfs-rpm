%global version     13.2.0

Name:           gcc
Version:        %{version}
Release:        1%{?dist}
Summary:        Various compilers (C, C++, Objective-C, ...)
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD

Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

%description
The gcc package contains the GNU Compiler Collection version 8. You'll need
this package in order to compile C code.

%global _build_id_links none


%prep
%setup -q


%build
case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
  ;;
esac

mkdir -v build
cd       build

../configure --prefix=/usr            \
             LD=ld                    \
             --enable-languages=c,c++ \
             --enable-default-pie     \
             --enable-default-ssp     \
             --disable-multilib       \
             --disable-bootstrap      \
             --disable-fixincludes    \
             --with-system-zlib
make


%check
cd build
ulimit -s 32768
make -k check
../contrib/test_summary
grep -A7 Summ ../contrib/test_summary


%install
cd build
make DESTDIR=%{buildroot} install
ln -svr /usr/bin/cpp %{buildroot}/usr/lib
ln -sv gcc %{buildroot}/usr/bin/cc
ln -sv gcc.1 %{buildroot}/usr/share/man/man1/cc.1
mkdir %{buildroot}/usr/lib/bfd-plugins/
ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/%{version}/liblto_plugin.so \
        %{buildroot}/usr/lib/bfd-plugins/
mkdir -pv %{buildroot}/usr/share/gdb/auto-load/usr/lib
mv -v %{buildroot}/usr/lib/*gdb.py %{buildroot}/usr/share/gdb/auto-load/usr/lib

rm -rf %{buildroot}/usr/share/info/dir


%files
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
/usr/bin/x86_64-pc-linux-gnu-gcc-13.2.0
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
/usr/share/gdb/auto-load/usr/lib/libstdc++.so.6.0.32-gdb.py
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
/usr/lib/libstdc++.so.6.0.32
/usr/lib/libtsan.so.2.0.0
/usr/lib/libubsan.so.1.0.0


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package

readelf -l a.out | grep ': /lib'