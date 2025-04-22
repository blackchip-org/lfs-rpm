# lfs

%global name        dejagnu
%global version     1.6.3
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A front end for testing other programs
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  texinfo

%description
DejaGnu is an Expect/Tcl based framework for testing other programs. DejaGnu
has several purposes: to make it easy to write tests for any program; to allow
you to write tests which will be portable to any host or target where a program
must be tested; and to standardize the output format of all tests (making it
easier to integrate the testing into software development).

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
mkdir -v build
cd       build

../configure --prefix=/usr
make %{?_smp_mflags}
makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi
makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install
install -v -dm755  %{buildroot}/usr/share/doc/dejagnu-%{version}
install -v -m644   doc/dejagnu.{html,txt} %{buildroot}/usr/share/doc/dejagnu-%{version}

#---------------------------------------------------------------------------
%check
cd build
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/share/%{name}

%else
/usr/bin/dejagnu
/usr/bin/runtest
/usr/include/*
/usr/share/%{name}

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
