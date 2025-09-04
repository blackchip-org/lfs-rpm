# lfs

%global name            dejagnu
%global version         1.6.3
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A front end for testing other programs
License:        GPLv3+

Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  texinfo

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
DejaGnu is an Expect/Tcl based framework for testing other programs. DejaGnu
has several purposes: to make it easy to write tests for any program; to allow
you to write tests which will be portable to any host or target where a program
must be tested; and to standardize the output format of all tests (making it
easier to integrate the testing into software development).

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description info
Info documentation for %{name}

%description man
Manual pages for %{name}

%endif

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
/usr/share/%{name}

%files devel
/usr/include/*.h

%files doc
/usr/share/doc/%{name}-%{version}

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif
