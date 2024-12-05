Name:           dnf
Version:        4.22.0
Release:        1%{?dist}
Summary:        Dandified YUM (DNF) is the next upcoming major version of YUM.
License:        GPLv2

Source0:        https://github.com/rpm-software-management/dnf/archive/refs/tags/%{version}.tar.gz

%description
Dandified YUM (DNF) is the next upcoming major version of YUM. It does package
management using RPM, libsolv and hawkey libraries. For metadata handling and
package downloads it utilizes librepo. To process and effectively handle the
comps data it uses libcomps.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DPYTHON_DESIRED="3" \
    -DWITH_MAN=0 \
    ..
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd build
make DESTDIR=%{buildroot} install

%lfs_install_end

#---------------------------------------------------------------------------
%files
/etc/bash_completion.d/dnf-3
/etc/dnf/aliases.d/zypper.conf
/etc/dnf/automatic.conf
/etc/dnf/dnf-strict.conf
/etc/dnf/dnf.conf
/etc/dnf/protected.d/yum.conf
/etc/logrotate.d/dnf
/usr/bin/dnf-3
/usr/bin/dnf-automatic-3
/usr/lib/python%{python_version}/site-packages/dnf-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/dnf
/usr/lib/systemd/system/dnf-automatic-download.service
/usr/lib/systemd/system/dnf-automatic-download.timer
/usr/lib/systemd/system/dnf-automatic-install.service
/usr/lib/systemd/system/dnf-automatic-install.timer
/usr/lib/systemd/system/dnf-automatic-notifyonly.service
/usr/lib/systemd/system/dnf-automatic-notifyonly.timer
/usr/lib/systemd/system/dnf-automatic.service
/usr/lib/systemd/system/dnf-automatic.timer
/usr/lib/systemd/system/dnf-makecache.service
/usr/lib/systemd/system/dnf-makecache.timer
/usr/lib/tmpfiles.d/dnf.conf
/usr/share/locale/*/LC_MESSAGES/dnf.mo
