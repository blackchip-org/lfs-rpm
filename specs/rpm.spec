Name:           rpm
Version:        4.19.0
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

# This package is built using a bootstrap script but this spec file is
# provided so that spectool can download the source file.

