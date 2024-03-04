Name:           python-wheel
Version:        0.42.0
Release:        1%{?dist}
Summary:        Built-package format for Python
License:        MIT

Source0:        https://pypi.org/packages/source/w/wheel/wheel-%{version}.tar.gz

%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename and the
.whl extension. It is designed to contain all the files for a PEP 376
compatible install in a way that is very close to the on-disk format.

Python 3 version.

#---------------------------------------------------------------------------
%prep
%setup -q -n wheel-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

pip3 install --ignore-installed --root %{buildroot} --no-index --find-links=dist wheel
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/wheel
/usr/lib/python%{python_version}/site-packages/wheel-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/wheel
