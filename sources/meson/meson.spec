# lfs

%global name            meson
%global version         1.7.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Meson is an open source build system designed to be both extremely fast and as user friendly as possible.
License:        ASL

Source0:        https://github.com/mesonbuild/meson/releases/download/%{version}/meson-%{version}.tar.gz
Source1:        %{name}.sha256

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
Meson is an open source build system meant to be both extremely fast, and, even
more importantly, as user friendly as possible.

The main design point of Meson is that every moment a developer spends writing
or debugging build definitions is a second wasted. So is every second spent
waiting for the build system to actually start compiling code.

%if !%{with lfs}
%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n meson-%{version}

#---------------------------------------------------------------------------
%build
pip3 wheel -w dist --no-build-isolation --no-deps $PWD

#---------------------------------------------------------------------------
%install
pip3 install --root %{buildroot} --no-index --find-links dist meson

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/lib/python%{python_version}/site-packages/*
/usr/share/polkit-1/actions/*

%else
/usr/bin/meson
/usr/lib/python%{python_version}/site-packages/meson-%{version}.dist-info
/usr/lib/python%{python_version}/site-packages/mesonbuild
/usr/share/polkit-1/actions/com.mesonbuild.install.policy

%files man
/usr/share/man/man*/*

%endif