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
Suggests:       %{name}-doc = %{version}

%description
The GNU Bourne Again shell (Bash) is a shell or command language interpreter
that is compatible with the Bourne shell (sh). Bash incorporates useful
features from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
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
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
mkdir -p %{buildroot}/%{lfs_dir}/bin
ln -s bash %{buildroot}/%{lfs_dir}/usr/bin/sh
%discard_docs
%discard_locales

%else
%make DESTDIR=%{buildroot} install
ln -s bash %{buildroot}/usr/bin/sh
%remove_info_dir

%endif

#---------------------------------------------------------------------------
%check
make tests

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/bash
%{lfs_dir}/usr/lib/bash
%{lfs_dir}/usr/lib/pkgconfig/bash.pc

%else
/usr/bin/bash
/usr/bin/bashbug
/usr/bin/sh
/usr/include/bash/*
/usr/lib/bash
/usr/lib/pkgconfig/bash.pc

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
