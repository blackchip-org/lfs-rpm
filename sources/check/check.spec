# lfs

%global name        check
%global version     0.15.2
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A unit test framework for C
License:        LGPLv2+

Source0:        https://github.com/lib%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer. Tests are run
in a separate address space, so Check can catch both assertion failures and
code errors that cause segmentation faults or other signals. The output from
unit tests can be used within source code editors and IDEs.

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
./configure --prefix=/usr --disable-static
make %{_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} docdir=/usr/share/doc/check-0.15.2 install

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include
/usr/lib/lib*.so*
/usr/lib/pkgconfig
/usr/share/aclocal

%else
/usr/bin/checkmk
/usr/include/*.h
/usr/lib/libcheck.so
/usr/lib/libcheck.so.0
%shlib /usr/lib/libcheck.so.0.0.0
/usr/lib/pkgconfig/check.pc
/usr/share/aclocal/check.m4

%files doc
/usr/share/info/*
/usr/share/doc/check-%{version}

%files man
/usr/share/man/man*/*

%endif
