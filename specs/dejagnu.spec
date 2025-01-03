Name:           dejagnu
Version:        1.6.3
Release:        1%{?dist}
Summary:        A front end for testing other programs
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/dejagnu/dejagnu-%{version}.tar.gz

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
%setup -q

#---------------------------------------------------------------------------
%build
mkdir -v build
cd       build

../configure --prefix=/usr
%make
makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi
makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install
install -v -dm755  %{buildroot}/usr/share/doc/dejagnu-%{version}
install -v -m644   doc/dejagnu.{html,txt} %{buildroot}/usr/share/doc/dejagnu-%{version}
%remove_info_dir

#---------------------------------------------------------------------------
%check
cd build
make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/dejagnu
/usr/bin/runtest
/usr/include/*
/usr/share/%{name}

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*
