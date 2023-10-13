%global version         0.41.1
%global py_version      3.11
%global _build_id_links none

Name:           python-wheel
Version:        %{version}
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


%prep
%setup -q -n wheel-%{version}


%build
pip3 wheel -w dist --no-build-isolation --no-deps $PWD


%install
pip3 install --root %{destdir} --no-index --find-links=dist wheel


%files

