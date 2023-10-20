Name:           gzip
Version:        1.12
Release:        1%{?dist}
Summary:        The GNU data compression program
License:        GPLv3+ and GFDL

Source0:        https://ftp.gnu.org/gnu/gzip/gzip-%{version}.tar.xz

%description
The gzip package contains the popular GNU gzip data compression program.
Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a very commonly used
data compression program.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr --host=%{lfs_tgt}

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%endif
