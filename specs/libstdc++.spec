# lfs

%global name          libstdc++
%global source_name   gcc
%global version       14.2.0
%global release       1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        C++ standard library
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD

Source:         https://ftp.gnu.org/gnu/%{source_name}/%{source_name}-%{version}/%{source_name}-%{version}.tar.xz
Source1:        %{name}.sha256

%description
C++ standard library for use in LFS bootstrapping only.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build

case %{lfs_arch} in
  x86_64)
    sed -e '/m64=/s/lib64/lib/' \
        -i.orig gcc/config/i386/t-linux64
 ;;
esac

mkdir build
cd build

%use_lfs_tools
../libstdc++-v3/configure           \
    --host=%{lfs_tgt}               \
    --build=$(../config.guess)      \
    --prefix=/usr                   \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/%{lfs_tgt}/include/c++/%{version}
%make

#---------------------------------------------------------------------------
%install

cd build

%use_lfs_tools
DESTDIR=%{buildroot}/%{lfs_dir} %make install
rm -v %{buildroot}/%{lfs_dir}/usr/lib/lib{stdc++,stdc++fs,supc++}.la
%discard_docs

#---------------------------------------------------------------------------
%files
%{lfs_tools_dir}/%{lfs_tgt}/include/c++/%{version}
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/share/gcc-%{version}/python
