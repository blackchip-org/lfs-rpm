Name:           dnf
Version:        5.2.8.1
Release:        1%{?dist}
Summary:        Command-line package manager
License:        GPLv2

Source0:        https://github.com/rpm-software-management/dnf5/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fmt
BuildRequires:  json-c
BuildRequires:  librepo
BuildRequires:  libsolv
BuildRequires:  libxml2
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  sdbus-c++
BuildRequires:  swig
BuildRequires:  sqlite
BuildRequires:  toml11
BuildRequires:  zchunk

%description
DNF5 is a command-line package manager that automates the process of
installing, upgrading, configuring, and removing computer programs in a
consistent manner. It supports RPM packages, modulemd modules, and comps
groups and environments.

#---------------------------------------------------------------------------
%prep
%setup -q -n dnf5-%{version}

#---------------------------------------------------------------------------
%build
sed -i 's/ \-Werror//g' CMakeLists.txt

mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DPYTHON_DESIRED="3" \
    -DWITH_MAN=OFF \
    -DWITH_MODULEMD=0 \
    -DWITH_RUBY=0 \
    -DWITH_PERL=0 \
    -DWITH_SYSTEMD=OFF \
    -DWITH_TESTS=OFF \
    -DWITH_DNF5DAEMON_CLIENT=OFF \
    -DWITH_DNF5DAEMON_SERVER=OFF \
    -DWITH_DNF5_PLUGINS=ON \
    -DWITH_PLUGIN_ACTIONS=ON \
    ..
%make

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install
ln -s %{buildroot}/usr/bin/dnf dnf5

#---------------------------------------------------------------------------
%files
/etc/bash_completion.d/dnf5
/etc/dnf/dnf.conf
/etc/dnf/dnf5-aliases.d/README
/usr/bin/{dnf,dnf5}
/usr/include/dnf5
/usr/include/libdnf5-cli
/usr/include/libdnf5
/usr/lib/dnf5/plugins/README
/usr/lib/libdnf5-cli.so
%shlib /usr/lib/libdnf5-cli.so.2
/usr/lib/libdnf5.so
%shlib /usr/lib/libdnf5.so.2
%shlib /usr/lib/libdnf5/plugins/python_plugins_loader.so
/usr/lib/perl5/%{perl_version}/site_perl/auto/libdnf5*
/usr/lib/perl5/%{perl_version}/site_perl/libdnf5*
/usr/lib/pkgconfig/libdnf5-cli.pc
/usr/lib/pkgconfig/libdnf5.pc
/usr/lib/python%{python_version}/site-packages/libdnf5-5.2.8.1.dist-info
/usr/lib/python%{python_version}/site-packages/libdnf5_cli-5.2.8.1.dist-info
/usr/lib/python%{python_version}/site-packages/libdnf5{,_cli}
/usr/lib/python%{python_version}/site-packages/libdnf_plugins
/usr/lib/systemd/system/dnf5-makecache.service
/usr/lib/systemd/system/dnf5-makecache.timer
/usr/share/dnf5/aliases.d/compatibility-plugins.conf
/usr/share/dnf5/aliases.d/compatibility.conf
/usr/share/locale/*/LC_MESSAGES/*.mo
