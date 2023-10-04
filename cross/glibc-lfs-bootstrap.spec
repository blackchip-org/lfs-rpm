Name:           glibc-lfs-bootstrap
Version:        2.38
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        glibc-%{version}.tar.xz
Patch0:         glibc-%{version}-fhs-1.patch

%undefine       _auto_set_build_flags
%global         debug_package %{nil}

BuildRequires:  gcc-lfs-bootstrap
BuildRequires:  linux-headers-lfs-bootstrap


%description
Toolchain for building LFS


%prep
%setup -q -n glibc-%{version}
%patch 0 -p1


%build
export PATH=%{tools}/bin:${PATH}

case $(uname -m) in
    i?86)   mkdir -p %{buildroot}/%{lfs}/lib
            ln -sfv ld-linux.so.2 %{buildroot}/%{lfs}/lib/ld-lsb.so.3
    ;;
    x86_64) mkdir -p %{buildroot}/%{lfs}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{lfs}/lib64
            ln -sfv ../lib/ld-linux-x86-64.so.2 %{buildroot}/%{lfs}/lib64/ld-lsb-x86-64.so.3
    ;;
esac

mkdir build
cd build

echo "rootsbindir=/usr/sbin" > configparms

../configure                             \
      --prefix=/usr                      \
      --host=%{lfs_tgt}                  \
      --build=$(../scripts/config.guess) \
      --enable-kernel=4.14               \
      --with-headers=%{lfs}/usr/include  \
      libc_cv_slibdir=/usr/lib
make


%install
export PATH=%{tools}/bin:${PATH}
cd build
DESTDIR=%{buildroot}/%{lfs} make install

sed '/RTLDLIST=/s@/usr@@g' -i %{buildroot}/%{lfs}/usr/bin/ldd

rm -rf %{buildroot}/%{lfs}/usr/share/info

%files
%{lfs}/etc/rpc
%{lfs}/usr/bin/*
%{lfs}/usr/include/*
%{lfs}/usr/lib/*
%{lfs}/usr/libexec/*
%{lfs}/usr/sbin/*
%{lfs}/usr/share/i18n/charmaps/*
%{lfs}/usr/share/i18n/locales/*
%{lfs}/usr/share/locale/locale.alias
%{lfs}/var/lib/nss_db/Makefile


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 2.38-1
- Initial package
