# extra

%global         version_2   4.20
%global         version     %{version_2}.1
%global         so_version  10.2.1

Name:           rpm
Version:        %{version}
Release:        1%{?dist}
Summary:        The RPM package management system
License:        GPLv2+

Source:         https://ftp.osuosl.org/pub/rpm/releases/rpm-%{version_2}.x/rpm-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  dbus
BuildRequires:  gettext
BuildRequires:  pkg-config
BuildRequires:  python
BuildRequires:  lua
BuildRequires:  readline
BuildRequires:  sqlite
Suggests:       %{name}-doc = %{version}

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
mkdir -p _build
cd _build

%if %{with lfs_stage1b}
cat > x86_64-lfs-linux-gnu.cmake <<EOF
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSROOT %{lfs_dir})

set(CMAKE_C_COMPILER %{lfs_tools_dir}/bin/x86_64-lfs-linux-gnu-gcc)
set(CMAKE_CXX_COMPILER %{lfs_tools_dir}/bin/x86_64-lfs-linux-gnu-g++)

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)

set(ENV{PKG_CONFIG_PATH} %{lfs_dir}/usr/lib/pkgconfig)
EOF

cmake --toolchain x86_64-lfs-linux-gnu.cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DENABLE_NLS=OFF \
    -DENABLE_OPENMP=OFF \
    -DENABLE_SQLITE=OFF \
    -DENABLE_TESTSUITE=OFF \
    -DENABLE_PYTHON=OFF \
    -DRPM_CONFIGDIR=/usr/lib/rpm \
    -DRPM_VENDOR=lfs \
    -DWITH_ACL=OFF \
    -DWITH_AUDIT=OFF \
    -DWITH_CAP=OFF \
    -DWITH_DBUS=OFF \
    -DWITH_FAPOLICYD=OFF \
    -DWITH_LIBDW=OFF \
    -DWITH_LIBELF=OFF \
    -DWITH_READLINE=OFF \
    -DWITH_SELINUX=OFF \
    -DWITH_SEQUOIA=OFF \
    -DWITH_ZSTD=OFF \
    ..

%elif %{with lfs_stage1c}
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DENABLE_NLS=OFF \
    -DENABLE_OPENMP=OFF \
    -DENABLE_SQLITE=OFF \
    -DENABLE_TESTSUITE=OFF \
    -DENABLE_PYTHON=OFF \
    -DRPM_CONFIGDIR=/usr/lib/rpm \
    -DRPM_VENDOR=lfs \
    -DWITH_ACL=OFF \
    -DWITH_ARCHIVE=OFF \
    -DWITH_AUDIT=OFF \
    -DWITH_CAP=OFF \
    -DWITH_DBUS=OFF \
    -DWITH_FAPOLICYD=OFF \
    -DWITH_INTERNAL_OPENPGP=ON \
    -DWITH_SELINUX=OFF \
    -DWITH_SEQUOIA=OFF \
    -DWITH_READLINE=OFF \
    -DWITH_ZSTD=OFF \
    ..

%else
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DENABLE_NLS=OFF \
    -DENABLE_OPENMP=OFF \
    -DENABLE_SQLITE=ON \
    -DENABLE_TESTSUITE=OFF \
    -DRPM_CONFIGDIR=/usr/lib/rpm \
    -DRPM_VENDOR=lfs \
    -DWITH_ARCHIVE=OFF \
    -DWITH_AUDIT=OFF \
    -DWITH_FAPOLICYD=OFF \
    -DWITH_INTERNAL_OPENPGP=ON \
    -DWITH_SELINUX=OFF \
    -DWITH_READLINE=ON \
    ..

%endif
%make

#---------------------------------------------------------------------------
%install
cd _build

%if %{with lfs_stage1b}
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs
%discard_locales

%elif %{with lfs_stage1c}
%make DESTDIR=%{buildroot} install
%discard_docs
%discard_locales

%else
%make DESTDIR=%{buildroot} install

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1b}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/rpm
%{lfs_dir}/usr/lib/*

%elif %{with lfs_stage1c}
/usr/bin/*
/usr/include/rpm
/usr/lib/*

%else
/usr/bin/gendiff
/usr/bin/rpm
/usr/bin/rpm2archive
/usr/bin/rpm2cpio
/usr/bin/rpmbuild
/usr/bin/rpmdb
/usr/bin/rpmgraph
/usr/bin/rpmkeys
/usr/bin/rpmlua
/usr/bin/rpmquery
/usr/bin/rpmsign
/usr/bin/rpmsort
/usr/bin/rpmspec
/usr/bin/rpmverify
/usr/include/rpm
/usr/lib/cmake/rpm
/usr/lib/librpm.so
/usr/lib/librpm.so.10
%shlib /usr/lib/librpm.so.%{so_version}
/usr/lib/librpmbuild.so
/usr/lib/librpmbuild.so.10
%shlib /usr/lib/librpmbuild.so.%{so_version}
/usr/lib/librpmio.so
/usr/lib/librpmio.so.10
%shlib /usr/lib/librpmio.so.%{so_version}
/usr/lib/librpmsign.so
/usr/lib/librpmsign.so.10
%shlib /usr/lib/librpmsign.so.%{so_version}
/usr/lib/pkgconfig/rpm.pc
/usr/lib/python%{python_version}/site-packages/*
/usr/lib/rpm
%shlib /usr/lib/rpm-plugins/dbus_announce.so
%shlib /usr/lib/rpm-plugins/prioreset.so
%shlib /usr/lib/rpm-plugins/syslog.so
%shlib /usr/lib/rpm-plugins/systemd_inhibit.so
%shlib /usr/lib/rpm-plugins/unshare.so
/usr/share/dbus-1/system.d/org.rpm.conf

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/rpm

%files man
/usr/share/man/man*/*

%endif


