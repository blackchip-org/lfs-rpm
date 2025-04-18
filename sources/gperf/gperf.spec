Name:           gperf
Version:        3.1
Release:        1%{?dist}
Summary:        GNU gperf is a perfect hash function generator
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/gperf/gperf-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
GNU gperf is a perfect hash function generator. For a given list of strings, it
produces a hash function and hash table, in form of C or C++ code, for looking
up a value depending on the input string. The hash function is perfect, which
means that the hash table has no collisions, and the hash table lookup needs a
single string comparison only.

GNU gperf is highly customizable. There are options for generating C or C++
code, for emitting switch statements or nested ifs instead of a hash table, and
for tuning the algorithm employed by gperf.

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
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr --docdir=/usr/share/doc/gperf-%{version}
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

#---------------------------------------------------------------------------
%check
make -j1 check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/gperf
/usr/share/doc/gperf-%{version}

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*