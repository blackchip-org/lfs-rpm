Name:           python-Jinja2
Version:        3.1.3
Release:        1%{?dist}
Summary:        General purpose template engine for python
License:        BSD

Source0:        https://pypi.org/packages/source/J/Jinja2/Jinja2-%{version}.tar.gz

%description
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

If you have any exposure to other text-based template languages, such as Smarty
or Django, you should feel right at home with Jinja2. It's both designer and
developer friendly by sticking to Python's principles and adding functionality
useful for templating environments.

#---------------------------------------------------------------------------
%prep
%setup -q -n Jinja2-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

pip3 wheel -w dist  --no-cache-dir --no-build-isolation --no-deps $PWD
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

pip3 install --ignore-installed --no-deps --root=%{buildroot} --no-index --no-user --find-links=dist Jinja2
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/Jinja2-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/jinja2
