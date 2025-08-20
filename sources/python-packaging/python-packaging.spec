# lfs

%global source_name     packaging
%global name            python-packaging
%global version         25.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Reusable core utilities for various Python Packaging interoperability specifications
License:        BSD-3-Clause

Source0:        https://pypi.org/packages/source/p/%{source_name}/%{source_name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildArch:      noarch

BuildRequires:  python-devel

%description
This library provides utilities that implement the interoperability
specifications which have clearly one correct behaviour (eg: PEP 440) or
benefit greatly from having a single shared implementation (eg: PEP 425).

The packaging project includes the following: version handling, specifiers,
markers, requirements, tags, utilities.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist --no-cache-dir --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --ignore-installed --root=%{buildroot} --no-index --no-user --find-links=dist %{source_name}

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/%{source_name}
/usr/lib/python%{python_version}/site-packages/%{source_name}-%{version}.dist-info
