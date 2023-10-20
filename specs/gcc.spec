Name:           gcc
Version:        13.2.0
Release:        1%{?dist}
Summary:        Various compilers (C, C++, Objective-C, ...)
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD

Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

%if %{with lfs_gcc_bootstrap}
%define         mpfr_version    4.2.0
%define         gmp_version     6.3.0
%define         mpc_version     1.3.1

Source1:        https://ftp.gnu.org/gnu/mpfr/mpfr-%{mpfr_version}.tar.xz
Source2:        https://ftp.gnu.org/gnu/gmp/gmp-%{gmp_version}.tar.xz
Source3:        https://ftp.gnu.org/gnu/mpc/mpc-%{mpc_version}.tar.gz
%endif

%description
The gcc package contains the GNU Compiler Collection version 8. You'll need
this package in order to compile C code.

#---------------------------------------------------------------------------
%prep
%setup -q

%if %{with lfs_gcc_bootstrap}
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

%if %{with lfs_stage1a}
../configure                    \
    --target=%{lfs_tgt}         \
    --prefix=%{lfs_tools_dir}   \
    --with-glibc-version=2.38   \
    --with-sysroot=%{lfs_dir}   \
    --with-newlib               \
    --without-headers           \
    --enable-default-pie        \
    --enable-default-ssp        \
    --disable-nls               \
    --disable-shared            \
    --disable-multilib          \
    --disable-threads           \
    --disable-libatomic         \
    --disable-libgomp           \
    --disable-libquadmath       \
    --disable-libssp            \
    --disable-libvtv            \
    --disable-libstdcxx         \
    --enable-languages=c,c++
%endif

%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd build
DESTDIR=%{buildroot} %make install

%if %{with lfs_stage1a}
cd ..
cat gcc/limitx.h gcc/glimits.h gcc/limity.h > \
  %{buildroot}/%{lfs_tools_dir}/lib/gcc/%{lfs_tgt}/%{version}/include/limits.h
%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files

%if %{with lfs_stage1a}
%{lfs_tools_dir}/bin/*
%{lfs_tools_dir}/lib/gcc/%{lfs_tgt}/%{version}
%{lfs_tools_dir}/lib64/*
%{lfs_tools_dir}/libexec/gcc/%{lfs_tgt}/%{version}
%endif
