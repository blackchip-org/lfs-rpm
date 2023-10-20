Name:           glibc
Version:        2.38
Release:        1%{?dist}
Summary:        The GNU libc libraries
License:        LGPLv2+ and LGPLv2+ with exceptions and GPLv2+ and GPLv2+ with exceptions and BSD and Inner-Net and ISC and Public Domain and GFDL

Source0:        https://ftp.gnu.org/gnu/glibc/glibc-%{version}.tar.xz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/glibc-%{version}-memalign_fix-1.patch

%if %{without %lfs_bootstrap}
Patch1:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/glibc-%{version}-fhs-1.patch
%endif

%description
The glibc package contains standard libraries which are used by multiple
programs on the system. In order to save disk space and memory, as well as to
make upgrading easier, common system code is kept in one place and shared
between programs. This particular package contains the most important sets of
shared libraries: the standard C library and the standard math library. Without
these two libraries, a Linux system will not function.


#---------------------------------------------------------------------------
%prep 
%setup -q 
%patch 0 -p1 

%if %{without %lfs_bootstrap}
%patch 1 -p1 
%endif 

#---------------------------------------------------------------------------
%build 
%lfs_build_begin

mkdir build
cd build

%if %{with lfs_stage1b}
echo "rootsbindir=/usr/sbin" > configparms

../configure                                \
      --prefix=/usr                         \
      --host=%{lfs_tgt}                     \
      --build=$(../scripts/config.guess)    \
      --enable-kernel=4.14                  \
      --with-headers=%{lfs_dir}/usr/include \
      libc_cv_slibdir=/usr/lib
%endif 

%make 
%lfs_build_end 

#---------------------------------------------------------------------------
%install 
%lfs_install_begin 

cd build

%if %{with lfs_stage1b}
DESTDIR=%{buildroot}/%{lfs_dir} %make install
sed '/RTLDLIST=/s@/usr@@g' -i %{buildroot}/%{lfs_dir}/usr/bin/ldd

case $(uname -m) in
    i?86)   mkdir -p              %{buildroot}/%{lfs_dir}/lib
            ln -sfv ld-linux.so.2 %{buildroot}/%{lfs_dir}/lib/ld-lsb.so.3
    ;;
    x86_64) mkdir -p %{buildroot}/%{lfs_dir}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{lfs_dir}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{lfs_dir}/lib64/ld-lsb-x86-64.so.3
    ;;
esac
rm -rf %{buildroot}/%{lfs_dir}/var

%endif 
%lfs_install_end 

#---------------------------------------------------------------------------
%files

%if %{with lfs_stage1b}
%{lfs_dir}/lib64/*
%{lfs_dir}/etc/rpc
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/libexec/*
%{lfs_dir}/usr/sbin/*
%{lfs_dir}/usr/share/i18n/charmaps/*
%{lfs_dir}/usr/share/i18n/locales/*
%{lfs_dir}/usr/share/locale/locale.alias
%endif 
