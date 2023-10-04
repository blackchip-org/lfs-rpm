Name:           gcc-lfs-tools
Version:        13.2.0
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

%define         mpfr_version    4.2.0
%define         gmp_version     6.3.0
%define         mpc_version     1.3.1

Source0:        gcc-%{version}.tar.xz
Source1:        mpfr-%{mpfr_version}.tar.xz
Source2:        gmp-%{gmp_version}.tar.xz
Source3:        mpc-%{mpc_version}.tar.gz

Conflicts:      libstdc++-lfs-bootstrap

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n gcc-%{version}

tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}

mv mpfr-%{mpfr_version}  mpfr
mv gmp-%{gmp_version}    gmp
mv mpc-%{mpc_version}    mpc


%build
export PATH=%{tools}/bin:${PATH}

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

sed '/thread_header =/s/@.*@/gthr-posix.h/' \
    -i libgcc/Makefile.in libstdc++-v3/include/Makefile.in

mkdir build
cd build

../configure                                       \
    --build=$(../config.guess)                     \
    --host=%{lfs_tgt}                              \
    --target=%{lfs_tgt}                            \
    LDFLAGS_FOR_TARGET=-L$PWD/%{lfs_tgt}/libgcc    \
    --prefix=/usr                                  \
    --with-build-sysroot=%{lfs}                    \
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
make


%install
export PATH=%{tools}/bin:${PATH}
cd build
DESTDIR=%{buildroot}/%{lfs} make install
ln -sv gcc %{buildroot}/%{lfs}/usr/bin/cc
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/c++/%{version}
%{lfs}/usr/lib/gcc/%{lfs_tgt}/%{version}
%{lfs}/usr/lib/*.{so*,a,spec}
%{lfs}/usr/libexec/gcc/%{lfs_tgt}/%{version}
%{lfs}/usr/share/gcc-%{version}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 13.2.0-1
- Initial package
