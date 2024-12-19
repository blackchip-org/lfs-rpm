Name:           dnf
Version:        5.2.8.1
Release:        1%{?dist}
Summary:        Dandified YUM (DNF) is the next upcoming major version of YUM.
License:        GPLv2

Source0:        https://github.com/rpm-software-management/dnf5/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fmt
BuildRequires:  json-c
BuildRequires:  librepo
BuildRequires:  libsolv
BuildRequires:  libxml2
BuildRequires:  pkg-config
BuildRequires:  swig
BuildRequires:  sqlite
BuildRequires:  toml11
BuildRequires:  zchunk

%description
Dandified YUM (DNF) is the next upcoming major version of YUM. It does package
management using RPM, libsolv and hawkey libraries. For metadata handling and
package downloads it utilizes librepo. To process and effectively handle the
comps data it uses libcomps.

#---------------------------------------------------------------------------
%prep
%setup -q -n dnf5-%{version}

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DPYTHON_DESIRED="3" \
    -DWITH_MAN=1 \
    -DWITH_MODULEMD=0 \
    -DWITH_RUBY=0 \
    -DWITH_SYSTEMD=OFF \
    ..
%make

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install

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
