# lfs

%global source_name     wheel
%global name            python-%{source_name}
%global version         0.45.1
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Built-package format for Python
License:        MIT

Source:         https://pypi.org/packages/source/w/%{source_name}/%{source_name}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-flit-core

%description
A built-package format for Python.

A wheel is a ZIP-format archive with a specially formatted filename and the
.whl extension. It is designed to contain all the files for a PEP 376
compatible install in a way that is very close to the on-disk format.

Python 3 version.

#---------------------------------------------------------------------------
%prep
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --ignore-installed --root %{buildroot} --no-index --find-links=dist wheel

#---------------------------------------------------------------------------
%files
/usr/bin/wheel
/usr/lib/python%{python_version}/site-packages/wheel-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/wheel
