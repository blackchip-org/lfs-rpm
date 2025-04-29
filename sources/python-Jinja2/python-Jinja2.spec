# lfs

%global source_name     jinja2
%global camel_name      Jinja2
%global name            python-%{camel_name}
%global version         3.1.5
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        General purpose template engine for python
License:        BSD

Source0:        https://pypi.org/packages/source/J/%{camel_name}/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildArch:      noarch

Requires:       python-MarkupSafe

BuildRequires:  python-devel
BuildRequires:  python-flit-core

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
%verify_sha256 -f %{SOURCE1}
%setup -q -n jinja2-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist  --no-cache-dir --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --ignore-installed --no-deps --root=%{buildroot} --no-index --no-user --find-links=dist Jinja2

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/jinja2-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/jinja2
