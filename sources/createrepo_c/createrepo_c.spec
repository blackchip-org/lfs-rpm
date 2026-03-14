# dnf

%global name            createrepo_c
%global version         1.2.2
%global release         1

# https://github.com/rpm-software-management/createrepo_c

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        C implementation of the createrepo
License:        GPLv2+

Source0:        https://github.com/rpm-software-management/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  glib-devel
BuildRequires:  curl-devel
BuildRequires:  libxml2-devel
BuildRequires:  python-devel
BuildRequires:  rpm-devel
BuildRequires:  openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  xz-devel
BuildRequires:  zchunk-devel
BuildRequires:  zlib-devel
BuildRequires:  libzstd-devel

%if !%{with lfs}
%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package python
Summary:        Python files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%endif

%description
C implementation of createrepo

%if !%{with lfs}
%description devel
Development files for %{name}

%description python
Python files for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DBUILD_DOC_C=OFF \
    -DENABLE_DRPM=OFF \
    -DWITH_LIBMODULEMD=OFF \
    ..
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/%{name}
/usr/lib/lib%{name}.*
/usr/lib/pkgconfig/*
/usr/lib/python%{python_version}/site-packages/%{name}
/usr/lib/python%{python_version}/site-packages/%{name}*.egg-info

%else
/usr/bin/createrepo_c
/usr/bin/mergerepo_c
/usr/bin/modifyrepo_c
/usr/bin/sqliterepo_c
/usr/lib/%{name}.so*

%files devel
/usr/include/%{name}
/usr/lib/lib%{name}.so
/usr/lib/pkgconfig/*

%files python
/usr/lib/python%{python_version}/site-packages/%{name}
/usr/lib/python%{python_version}/site-packages/%{name}*.egg-info

%endif