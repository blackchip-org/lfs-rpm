%global version         1.2.1
%global py_version      3.11

%global _build_id_links none

Name:           python-meson
Version:        %{version}
Release:        1%{?dist}
Summary:        Meson is an open source build system designed to be both extremely fast and as user friendly as possible.
License:        ASL

Source0:        https://github.com/mesonbuild/meson/releases/download/1.2.1/meson-1.2.1.tar.gz

%description
Meson is an open source build system meant to be both extremely fast, and, even
more importantly, as user friendly as possible.

The main design point of Meson is that every moment a developer spends writing
or debugging build definitions is a second wasted. So is every second spent
waiting for the build system to actually start compiling code.


%prep
%setup -q -n meson-%{version}


%build
pip3 wheel -w dist --no-build-isolation --no-deps $PWD


%install
pip3 install --root %{buildroot} --no-index --find-links dist meson


%files
/usr/bin/meson
/usr/lib/python%{py_version}/site-packages/meson-%{version}.dist-info
/usr/lib/python%{py_version}/site-packages/mesonbuild
/usr/share/man/man1/*
/usr/share/polkit-1/actions/com.mesonbuild.install.policy
