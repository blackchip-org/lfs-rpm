# lfs

%global name        gzip
%global version     1.13
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU data compression program
License:        GPLv3+ and GFDL

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  less
Suggests:       %{name}-doc = %{version}

%description
The gzip package contains the popular GNU gzip data compression program.
Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a very commonly used
data compression program.

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr --host=%{lfs_tgt}

%else
./configure --prefix=/usr

%endif
make -j %{nproc}

#---------------------------------------------------------------------------
%install
make -j %{nproc} DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
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

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
