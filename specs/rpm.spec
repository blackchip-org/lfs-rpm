Name:           rpm
Version:        4.19.1.1
Release:        1%{?dist}
Summary:        The RPM package management system
License:        GPLv2+

Source0:        https://ftp.osuosl.org/pub/rpm/releases/rpm-4.19.x/rpm-%{version}.tar.bz2

%description
The RPM Package Manager (RPM) is a powerful command line driven
package management system capable of installing, uninstalling,
verifying, querying, and updating software packages. Each software
package consists of an archive of files along with information about
the package like its version, a description, etc.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir -p _build
cd _build

cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DENABLE_NLS=OFF \
    -DENABLE_OPENMP=OFF \
    -DENABLE_SQLITE=OFF \
    -DENABLE_TESTSUITE=OFF \
    -DRPM_CONFIGDIR=/usr/lib/rpm \
    -DRPM_VENDOR=lfs \
    -DWITH_ARCHIVE=OFF \
    -DWITH_AUDIT=OFF \
    -DWITH_FAPOLICYD=OFF \
    -DWITH_INTERNAL_OPENPGP=ON \
    -DWITH_SELINUX=OFF \
    -DWITH_READLINE=OFF \
    ..
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd _build
%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/gendiff
/usr/bin/rpm
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
/usr/lib/librpmbuild.so
/usr/lib/librpmbuild.so.10
/usr/lib/librpmio.so
/usr/lib/librpmio.so.10
/usr/lib/librpmsign.so
/usr/lib/librpmsign.so.10
/usr/lib/pkgconfig/rpm.pc
/usr/lib/python%{python_version}/site-packages/*
/usr/lib/rpm
/usr/lib/rpm-plugins/dbus_announce.so
/usr/lib/rpm-plugins/prioreset.so
/usr/lib/rpm-plugins/syslog.so
/usr/lib/rpm-plugins/systemd_inhibit.so
/usr/share/dbus-1/system.d/org.rpm.conf
/usr/share/doc/rpm
/usr/share/locale/*/LC_MESSAGES/rpm.mo
/usr/share/man/man{1,8}/*

%defattr(755,root,root,755)
/usr/lib/librpm.so.10.0.0
/usr/lib/librpmbuild.so.10.0.0
/usr/lib/librpmio.so.10.0.0
/usr/lib/librpmsign.so.10.0.0


