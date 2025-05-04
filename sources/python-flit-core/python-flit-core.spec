# lfs

%global source_name     flit_core
%global name            python-flit-core
%global version         3.11.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Simplified packaging of Python modules
License:        BSD-3-Clause

Source0:        https://pypi.org/packages/source/f/%{source_name}/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildArch:      noarch

BuildRequires:  python-devel

%description
Flit is a simple way to put Python packages and modules on PyPI.

Flit only creates packages in the new 'wheel' format. People using older
versions of pip (<1.5) or easy_install will not be able to install them.

Flit packages a single importable module or package at a time, using the import
name as the name on PyPI. All sub-packages and data files within a package are
included automatically.

Flit requires Python 3, but you can use it to distribute modules for Python 2,
so long as they can be imported on Python 3.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --force-reinstall --root=%{buildroot} --no-index --no-user --find-links=dist flit_core

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/flit_core
/usr/lib/python%{python_version}/site-packages/flit_core-%{version}.dist-info
