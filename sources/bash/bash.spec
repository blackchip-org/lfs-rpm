# lfs

%global name        bash
%global version     5.2.37
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU Bourne Again shell
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

Provides:       /bin/sh
Provides:       /bin/bash

BuildRequires:  readline

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The GNU Bourne Again shell (Bash) is a shell or command language interpreter
that is compatible with the Bourne shell (sh). Bash incorporates useful
features from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr                      \
            --build=$(sh support/config.guess) \
            --host=%{lfs_tgt}                  \
            --without-bash-malloc              \
            bash_cv_strtold_broken=no

%else
./configure --prefix=/usr             \
            --without-bash-malloc     \
            --with-installed-readline \
            bash_cv_strtold_broken=no \
            --docdir=/usr/share/doc/bash-%{version}

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make    DESTDIR=%{buildroot}/%{?lfs_dir} install
ln -s   bash %{buildroot}/%{?lfs_dir}/usr/bin/sh

#---------------------------------------------------------------------------
%check
make tests

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/%{name}
%{?lfs_dir}/usr/lib/%{name}
%{?lfs_dir}/usr/lib/pkgconfig/*

%else
/usr/bin/bash
/usr/bin/bashbug
/usr/bin/sh
/usr/lib/bash

%files devel
/usr/include/%{name}
/usr/lib/pkgconfig/bash.pc

%files doc
/usr/share/doc/%{name}-%{version}

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif
