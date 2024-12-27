Name:           libstdc++
Version:        14.2.0
Release:        1%{?dist}
Summary:        C++ standard library
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz

%global         glibc_version   2.40

%description
C++ standard library

#---------------------------------------------------------------------------
%prep
%setup -q -n gcc-%{version}

#---------------------------------------------------------------------------
%build

case $(uname -m) in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

mkdir build
cd build

%if %{with lfs_stage1a}
%use_lfs_tools
../libstdc++-v3/configure           \
    --host=%{lfs_tgt}               \
    --build=$(../config.guess)      \
    --prefix=/usr                   \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/%{lfs_tgt}/include/c++/%{version}
%endif
%make

#---------------------------------------------------------------------------
%install

cd build

%if %{with lfs_stage1a}
%use_lfs_tools
DESTDIR=%{buildroot}/%{lfs_dir} %make install
rm -v %{buildroot}/%{lfs_dir}/usr/lib/lib{stdc++,stdc++fs,supc++}.la
%discard_docs

%endif

#---------------------------------------------------------------------------
%check
cd build
ulimit -s 32768
%make -k check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1a}
%{lfs_tools_dir}/%{lfs_tgt}/include/c++/%{version}
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/share/gcc-%{version}/python

%endif
