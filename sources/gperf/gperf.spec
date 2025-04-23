# lfs

%global name        gperf
%global version     3.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        GNU gperf is a perfect hash function generator
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr --docdir=/usr/share/doc/gperf-%{version}
make %{_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make -j1 check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin

%else
/usr/bin/gperf
/usr/share/doc/gperf-%{version}

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif