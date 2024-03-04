Name:           python-setuptools
Version:        69.1.0
Release:        1%{?dist}
Summary:        Easily build and distribute Python 3 packages
License:        MIT

Source0:        https://pypi.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.

#---------------------------------------------------------------------------
%prep
%setup -q -n setuptools-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

pip3 install --ignore-installed --root %{buildroot} --no-index --find-links=dist setuptools
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/setuptools-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/setuptools
/usr/lib/python%{python_version}/site-packages/_distutils_hack
/usr/lib/python%{python_version}/site-packages/distutils-precedence.pth
/usr/lib/python%{python_version}/site-packages/pkg_resources