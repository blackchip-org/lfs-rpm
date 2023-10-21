Name:           python-flit-core
Version:        3.9.0
Release:        1%{?dist}
Summary:        Simplified packaging of Python modules
License:        BSD-3-Clause

Source0:        https://pypi.org/packages/source/f/flit-core/flit_core-%{version}.tar.gz

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
%setup -q -n flit_core-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

pip3 install --root=%{buildroot} --no-index --no-user --find-links dist flit_core
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/flit_core
/usr/lib/python%{python_version}/site-packages/flit_core-%{version}.dist-info
