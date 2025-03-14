Name:           python-MarkupSafe
Version:        3.0.2
Release:        1%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string
License:        BSD

Source:         https://pypi.org/packages/source/M/MarkupSafe/markupsafe-%{version}.tar.gz

BuildRequires:  python
BuildRequires:  python-setuptools

%description
A library for safe markup escaping.

#---------------------------------------------------------------------------
%prep
%setup -q -n markupsafe-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist  --no-cache-dir --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --ignore-installed --root=%{buildroot} --no-index --no-user --find-links=dist Markupsafe

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/markupsafe-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/markupsafe
