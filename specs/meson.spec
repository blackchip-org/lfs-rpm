Name:           meson
Version:        1.4.0
Release:        1%{?dist}
Summary:        Meson is an open source build system designed to be both extremely fast and as user friendly as possible.
License:        ASL

Source0:        https://github.com/mesonbuild/meson/releases/download/%{version}/meson-%{version}.tar.gz

%description
Meson is an open source build system meant to be both extremely fast, and, even
more importantly, as user friendly as possible.

The main design point of Meson is that every moment a developer spends writing
or debugging build definitions is a second wasted. So is every second spent
waiting for the build system to actually start compiling code.

#---------------------------------------------------------------------------
%prep
%setup -q -n meson-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --root %{buildroot} --no-index --find-links dist meson

#---------------------------------------------------------------------------
%files
/usr/bin/meson
/usr/lib/python%{python_version}/site-packages/meson-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/mesonbuild
/usr/share/man/man1/*
/usr/share/polkit-1/actions/com.mesonbuild.install.policy