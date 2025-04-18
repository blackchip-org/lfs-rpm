Name:           check
Version:        0.15.2
Release:        1%{?dist}
Summary:        A unit test framework for C
License:        LGPLv2+

Source0:        https://github.com/libcheck/check/releases/download/%{version}/check-%{version}.tar.gz

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
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr --disable-static
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} docdir=/usr/share/doc/check-0.15.2 install
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%post
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/checkmk
/usr/include/*.h
/usr/lib/libcheck.so
/usr/lib/libcheck.so.0
%shlib /usr/lib/libcheck.so.0.0.0
/usr/lib/pkgconfig/check.pc
/usr/share/aclocal/check.m4
/usr/share/doc/check-%{version}

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

