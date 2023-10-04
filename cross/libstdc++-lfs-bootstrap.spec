Name:           libstdc++-lfs-bootstrap
Version:        13.2.0
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        gcc-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}

BuildRequires:  glibc-lfs-bootstrap
BuildRequires:  linux-headers-lfs-bootstrap


%description
Toolchain for building LFS


%prep
%setup -q -n gcc-%{version}


%build
export PATH=%{tools}/bin:${PATH}

mkdir build
cd build

../libstdc++-v3/configure           \
    --host=%{lfs_tgt}               \
    --build=$(../config.guess)      \
    --prefix=/usr                   \
    --disable-multilib              \
    --disable-nls                   \
    --disable-libstdcxx-pch         \
    --with-gxx-include-dir=/tools/%{lfs_tgt}/include/c++/%{version}
make


%install
export PATH=%{tools}/bin:${PATH}
cd build
DESTDIR=%{buildroot}/%{lfs} make install

rm -v %{buildroot}/%{lfs}/usr/lib/lib{stdc++,stdc++fs,supc++}.la


%files
%{tools}/%{lfs_tgt}/include/c++/%{version}
%{lfs}/usr/lib/*
%{lfs}/usr/share/gcc-%{version}/python


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 13.2.0-1
- Initial package
