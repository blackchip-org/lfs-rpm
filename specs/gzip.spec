Name:           gzip
Version:        1.13
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
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr --host=%{lfs_tgt}

%else
./configure --prefix=/usr

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*

%else
/usr/bin/gunzip
/usr/bin/gzexe
/usr/bin/gzip
/usr/bin/uncompress
/usr/bin/zcat
/usr/bin/zcmp
/usr/bin/zdiff
/usr/bin/zegrep
/usr/bin/zfgrep
/usr/bin/zforce
/usr/bin/zgrep
/usr/bin/zless
/usr/bin/zmore
/usr/bin/znew
/usr/share/info/*
/usr/share/man/man1/*

%endif
