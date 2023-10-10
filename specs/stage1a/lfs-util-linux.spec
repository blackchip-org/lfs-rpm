%define version2    2.39
%define version     %{version2}.1

Name:           lfs-util-linux
Version:        %{version}
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://www.kernel.org/pub/linux/utils/util-linux/v%{version2}/util-linux-%{version}.tar.xz


%description
Toolchain for building LFS


%prep
%setup -q -n util-linux-%{version}


%build
mkdir -pv %{buildroot}/var/lib/hwclock
./configure ADJTIME_PATH=/var/lib/hwclock/adjtime    \
            --libdir=/usr/lib    \
            --runstatedir=/run   \
            --docdir=/usr/share/doc/util-linux-2.39.1 \
            --disable-chfn-chsh  \
            --disable-login      \
            --disable-nologin    \
            --disable-su         \
            --disable-setpriv    \
            --disable-runuser    \
            --disable-pylibmount \
            --disable-static     \
            --without-python     \
            --disable-makeinstall-chown \
            --disable-makeinstall-setuid
make


%install
make DESTDIR=%{buildroot} install
%remove_docs


%files
/bin/*
/sbin/*
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/sbin/*
/usr/share/bash-completion/completions/*
/usr/share/locale/*/LC_MESSAGES/*.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
