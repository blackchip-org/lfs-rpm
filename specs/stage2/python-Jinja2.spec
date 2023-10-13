%global version         3.1.2
%global py_version      3.11
%global _build_id_links none

Name:           python-Jinja2
Version:        %{version}
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


%prep
%setup -q -n Jinja2-%{version}


%build
pip3 wheel -w dist --no-build-isolation --no-deps $PWD


%install
pip3 install --root=%{buildroot} --no-index --no-user --find-links dist Jinja2


%files
/usr/lib/python%{py_version}/site-packages/Jinja2-%{version}.dist-info
/usr/lib/python%{py_version}/site-packages/jinja2

