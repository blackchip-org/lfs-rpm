Name:           gperf
Version:        3.1
Release:        1%{?dist}
Summary:        GNU gperf is a perfect hash function generator
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/gperf/gperf-%{version}.tar.gz

%description
GNU gperf is a perfect hash function generator. For a given list of strings, it
produces a hash function and hash table, in form of C or C++ code, for looking
up a value depending on the input string. The hash function is perfect, which
means that the hash table has no collisions, and the hash table lookup needs a
single string comparison only.

GNU gperf is highly customizable. There are options for generating C or C++
code, for emitting switch statements or nested ifs instead of a hash table, and
for tuning the algorithm employed by gperf.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr --docdir=/usr/share/doc/gperf-%{version}
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%check
make -j1 check

#---------------------------------------------------------------------------
%files
/usr/bin/gperf
/usr/share/doc/gperf-%{version}
/usr/share/info/*.info.gz
/usr/share/man/man1/*