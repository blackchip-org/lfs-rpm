Name:           m4
Version:        1.4.19
Release:        1%{?dist}
Summary:        GNU macro processor
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz

%description
A GNU implementation of the traditional UNIX macro processor. M4 is useful for
writing text files which can be logically parsed, and is used by many programs
as part of their build process. M4 has built-in functions for including files,
running shell commands, doing arithmetic, etc. The autoconf program needs m4
for generating configure scripts, but not for running configure scripts.

Install m4 if you need a macro processor.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%else
%make DESTDIR=%{buildroot} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/m4
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/m4.mo

%else
/usr/bin/m4
/usr/share/locale/*/LC_MESSAGES/m4.mo
/usr/share/info/*
/usr/share/man/man1/m4.1.gz
%endif
