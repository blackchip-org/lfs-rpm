# dnf

%global name            dnf
%global version         5.2.16.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Command-line package manager
License:        GPLv2

Source0:        https://github.com/rpm-software-management/dnf5/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

Requires:       elfutils
Requires:       file
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gettext
BuildRequires:  json-c-devel
BuildRequires:  librepo-devel
BuildRequires:  libsolv-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  perl-devel
BuildRequires:  pkgconf
BuildRequires:  python-devel
BuildRequires:  sdbus-c++-devel
BuildRequires:  swig
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  toml11-devel
BuildRequires:  zchunk-devel

%if !%{with lfs}
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%endif

%description
DNF5 is a command-line package manager that automates the process of
installing, upgrading, configuring, and removing computer programs in a
consistent manner. It supports RPM packages, modulemd modules, and comps
groups and environments.

%if !%{with lfs}
%description devel
Development files for %{name}

%description lang
Language files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n dnf5-%{version}

#---------------------------------------------------------------------------
%build
sed -i 's/ \-Werror//g' CMakeLists.txt

%if %{with lfs_stage3}

# Using systemd in the pod build image pulls in way too many packages and
# that needs to be as light as possible. While the build has a flag to turn
# off systemd support, it doesn't seem like it is always checked. Make some
# changes here to get it to compile.
sed -i '/needs_restarting_plugin/d' dnf5-plugins/CMakeLists.txt
sed -i 's/sdbus::ObjectPath/std::string/g' dnf5/commands/offline/offline.cpp

mkdir build
cd build

cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DPYTHON3=OFF \
    -DWITH_MAN=OFF \
    -DWITH_MODULEMD=0 \
    -DWITH_RUBY=0 \
    -DWITH_PERL5=0 \
    -DWITH_SYSTEMD=OFF \
    -DWITH_TESTS=OFF \
    -DWITH_DNF5DAEMON_CLIENT=OFF \
    -DWITH_DNF5DAEMON_SERVER=OFF \
    -DWITH_DNF5_PLUGINS=ON \
    -DWITH_PLUGIN_ACTIONS=ON \
    -DWITH_PLUGIN_APPSTREAM=OFF \
    ..

%else
mkdir build
cd build

cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DPYTHON3=ON \
    -DWITH_MAN=OFF \
    -DWITH_MODULEMD=0 \
    -DWITH_RUBY=0 \
    -DWITH_PERL5=1 \
    -DWITH_SYSTEMD=ON \
    -DWITH_TESTS=OFF \
    -DWITH_DNF5DAEMON_CLIENT=OFF \
    -DWITH_DNF5DAEMON_SERVER=OFF \
    -DWITH_DNF5_PLUGINS=ON \
    -DWITH_PLUGIN_ACTIONS=ON \
    -DWITH_PLUGIN_APPSTREAM=OFF \
    ..
%endif

make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install
ln -s dnf5 %{buildroot}/usr/bin/dnf

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/etc/bash_completion.d
/etc/dnf
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/lib/dnf5
/usr/lib/libdnf5
/usr/lib/python%{python_version}
/usr/lib/pkgconfig
/usr/lib/systemd
/usr/share/dnf5

%else
/etc/bash_completion.d/dnf5
%config(noreplace) /etc/dnf/dnf.conf
%config(noreplace) /etc/dnf/libdnf5-plugins/actions.conf
%config(noreplace) /etc/dnf/libdnf5-plugins/expired-pgp-keys.conf
/etc/dnf/dnf5-aliases.d/README
/usr/bin/{dnf,dnf5}
/usr/bin/dnf-automatic
/usr/lib/dnf5/plugins/README
/usr/lib/libdnf5-cli.so.*
/usr/lib/libdnf5.so.*
/usr/lib/libdnf5/plugins/python_plugins_loader.so
/usr/lib/dnf5/plugins/automatic_cmd_plugin.so
/usr/lib/dnf5/plugins/builddep_cmd_plugin.so
/usr/lib/dnf5/plugins/changelog_cmd_plugin.so
/usr/lib/dnf5/plugins/config-manager_cmd_plugin.so
/usr/lib/dnf5/plugins/copr_cmd_plugin.so
/usr/lib/libdnf5/plugins/expired-pgp-keys.so
/usr/lib/dnf5/plugins/repoclosure_cmd_plugin.so
/usr/lib/dnf5/plugins/reposync_cmd_plugin.so
/usr/lib/libdnf5/plugins/actions.so
/usr/lib/python%{python_version}/site-packages/libdnf5-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/libdnf5_cli-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/libdnf5{,_cli}
/usr/lib/python%{python_version}/site-packages/libdnf_plugins
/usr/lib/systemd/system/dnf-automatic.service
/usr/lib/systemd/system/dnf-automatic.timer
/usr/lib/systemd/system/dnf5-automatic.service
/usr/lib/systemd/system/dnf5-automatic.timer
/usr/lib/systemd/system/dnf5-makecache.service
/usr/lib/systemd/system/dnf5-makecache.timer
/usr/share/dnf5/aliases.d/compatibility.conf
/usr/share/dnf5/aliases.d/compatibility-plugins.conf
/usr/share/dnf5/aliases.d/compatibility-reposync.conf
/usr/share/dnf5/dnf5-plugins/automatic.conf

%if !%{with lfs_stage3}
%shlib /usr/lib/dnf5/plugins/needs_restarting_cmd_plugin.so
/usr/lib/perl5/%{perl_version}/site_perl/auto/libdnf5*
/usr/lib/perl5/%{perl_version}/site_perl/libdnf5*
/usr/lib/systemd/system/dnf5-offline-transaction-cleanup.service
/usr/lib/systemd/system/dnf5-offline-transaction.service

%endif

%files devel
/usr/include/dnf5
/usr/include/libdnf5-cli
/usr/include/libdnf5
/usr/lib/libdnf5.so
/usr/lib/libdnf5-cli.so
/usr/lib/pkgconfig/libdnf5-cli.pc
/usr/lib/pkgconfig/libdnf5.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%endif

