#lfs

%global source_name markupsafe
%global camel_name  MarkupSafe
%global name        python-%{camel_name}
%global version     3.0.2
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string
License:        BSD

Source0:        https://pypi.org/packages/source/M/${camel_name}/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  python
BuildRequires:  python-setuptools

%description
A library for safe markup escaping.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

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
