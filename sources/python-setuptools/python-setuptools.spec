# lfs

%global source_name setuptools
%global name        python-%{source_name}
%global version     75.8.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Easily build and distribute Python 3 packages
License:        MIT

Source0:        https://pypi.org/packages/source/s/%{source_name}/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

Requires:       python-wheel

BuildRequires:  python
BuildRequires:  python-wheel

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package also contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n setuptools-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --ignore-installed --root %{buildroot} --no-index --find-links=dist setuptools

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/setuptools-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/setuptools
/usr/lib/python%{python_version}/site-packages/_distutils_hack
/usr/lib/python%{python_version}/site-packages/distutils-precedence.pth
/usr/lib/python%{python_version}/site-packages/pkg_resources