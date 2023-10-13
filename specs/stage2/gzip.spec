%global version         1.12
%global _build_id_links none

Name:           gzip
Version:        %{version}
Release:        1%{?dist}
Summary:        The GNU data compression program
License:        GPLv3+ and GFDL

Source0:        https://ftp.gnu.org/gnu/gzip/gzip-%{version}.tar.xz

%description
The gzip package contains the popular GNU gzip data compression program.
Gzipped files have a .gz extension.

Gzip should be installed on your system, because it is a very commonly used
data compression program.


%prep
%setup -q


%build
./configure --prefix=/usr
make


%check
make check


%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/share/info/dir


%files
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

