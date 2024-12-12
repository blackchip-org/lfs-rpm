Name:           bash
Version:        5.2.32
Release:        1%{?dist}
Summary:        The GNU Bourne Again shell
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/bash/bash-%{version}.tar.gz

%description
The GNU Bourne Again shell (Bash) is a shell or command language interpreter
that is compatible with the Bourne shell (sh). Bash incorporates useful
features from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modification.

#---------------------------------------------------------------------------
%prep
rm -rf      %{name}-%{version}
tar xf      %{_sourcedir}/%{name}/%{name}-%{version}.tar.gz
cd          %{name}-%{version}

#---------------------------------------------------------------------------
%build
cd %{name}-%{version}

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
cd %{name}-%{version}

%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
mkdir -p %{buildroot}/%{lfs_dir}/bin
ln -s bash %{buildroot}/%{lfs_dir}/usr/bin/sh
%discard_docs

%else
%make DESTDIR=%{buildroot} install
ln -s bash %{buildroot}/usr/bin/sh

%endif

#---------------------------------------------------------------------------
%check
make tests

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/bash
%{lfs_dir}/usr/lib/bash
%{lfs_dir}/usr/lib/pkgconfig/bash.pc
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/bash.mo

%else
/usr/bin/bash
/usr/bin/bashbug
/usr/bin/sh
/usr/include/bash/*
/usr/lib/bash
/usr/lib/pkgconfig/bash.pc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man1/*

%endif
