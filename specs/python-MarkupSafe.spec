Name:           python-MarkupSafe
Version:        2.1.3
Release:        1%{?dist}
Summary:        Implements a XML/HTML/XHTML Markup safe string
License:        BSD

Source0:        https://pypi.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz

%description
A library for safe markup escaping.

#---------------------------------------------------------------------------
%prep
%setup -q -n MarkupSafe-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

pip3 wheel -w dist --no-build-isolation --no-deps $PWD
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

pip3 install --root=%{buildroot} --no-index --no-user --find-links dist Markupsafe
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/lib/python%{python_version}/site-packages/MarkupSafe-2.1.3.dist-info
/usr/lib/python%{python_version}/site-packages/markupsafe
