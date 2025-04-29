# rpm

%global name            rpm
%global version_2       4.20
%global version         %{version_2}.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The RPM package management system
License:        GPLv2+

Source0:        https://ftp.osuosl.org/pub/%{name}/releases/%{name}-%{version_2}.x/%{name}-%{version}.tar.bz2
Source1:        %{name}.sha256

BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  gettext
BuildRequires:  pkgconf
BuildRequires:  python-devel
BuildRequires:  lua-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
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

%elif %{with lfs_stage2}
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
    -DWITH_READLINE=ON \
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
    -DWITH_SEQUOIA=OFF \
    -DWITH_READLINE=ON \
    ..

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd _build

make DESTDIR=%{buildroot}/%{?lfs_dir} install

# TODO: This plugin seems to be causing problems when installing d-bus inside
# the podman container. Remove it for now.
# https://github.com/rpm-software-management/rpm/issues/3187
rm %{buildroot}/%{?lfs_dir}/usr/lib/rpm-plugins/unshare.so

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/rpm
%{?lfs_dir}/usr/lib/*

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
/usr/lib/librpm.so.*
/usr/lib/librpmbuild.so.*
/usr/lib/librpmio.so.*
/usr/lib/librpmsign.so.*
/usr/lib/python%{python_version}/site-packages/*
/usr/lib/%{name}
/usr/lib/rpm-plugins/dbus_announce.so
/usr/lib/rpm-plugins/prioreset.so
/usr/lib/rpm-plugins/syslog.so
/usr/lib/rpm-plugins/systemd_inhibit.so
# %%shlib /usr/lib/rpm-plugins/unshare.so
/usr/share/dbus-1/system.d/org.rpm.conf

%files devel
/usr/include/%{name}
/usr/lib/cmake/%{name}
/usr/lib/librpm.so
/usr/lib/librpmbuild.so
/usr/lib/librpmio.so
/usr/lib/librpmsign.so
/usr/lib/pkgconfig/%{name}.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}

%files man
/usr/share/man/man*/*.gz

%endif


