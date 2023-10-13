%global version         2.1.3
%global py_version      3.11
%global _build_id_links none

Name:           python-MarkupSafe
Version:        %{version}
Release:        1%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string
License:        BSD

Source0:        https://pypi.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz

%description
A library for safe markup escaping.


%prep
%setup -q -n MarkupSafe-%{version}


%build
pip3 wheel -w dist --no-build-isolation --no-deps $PWD


%install
pip3 install --root=%{buildroot} --no-index --no-user --find-links dist Markupsafe


%files
/usr/lib/python%{py_version}/site-packages/MarkupSafe-2.1.3.dist-info
/usr/lib/python%{py_version}/site-packages/markupsafe
