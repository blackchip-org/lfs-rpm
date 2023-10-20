Name:           util-linux
Version:        2.39.1
Release:        1%{?dist}
Summary:        Collection of basic system utilities
License:        GPLv2 and GPLv2+ and LGPLv2+ and BSD with advertising and Public Domain

Source0:        https://www.kernel.org/pub/linux/utils/util-linux/v2.39/util-linux-%{version}.tar.xz

%description 
The util-linux package contains a large variety of low-level system
utilities that are necessary for a Linux system to function. Among
others, util-linux contains the fdisk configuration tool and the login
program.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
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

%endif 
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
/bin/*
/sbin/*
/usr/bin/*
/usr/include/*
/usr/lib/*
/usr/sbin/*
/usr/share/bash-completion/completions/*
/usr/share/locale/*/LC_MESSAGES/*.mo

%endif 
