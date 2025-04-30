# lfs

%global name            expect
%global version         5.45.4
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A program-script interaction and testing utility
License:        Public Domain

Source0:        https://prdownloads.sourceforge.net/%{name}/%{name}%{version}.tar.gz
Source1:        %{name}.sha256
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/expect-%{version}-gcc14-1.patch

BuildRequires:  tcl-devel

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
Expect is a tcl application for automating and testing interactive applications
such as telnet, ftp, passwd, fsck, rlogin, tip, etc. Expect makes it easy for a
script to control another program and interact with it.

This package contains expect and some scripts that use it.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{name}%{version}

# patch macro has fuzz=0 which fail, manually patch
patch -Np1 -i %{PATCH0}

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr           \
            --with-tcl=/usr/lib     \
            --enable-shared         \
            --mandir=/usr/share/man \
            --with-tclinclude=/usr/include
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
ln -svf expect%{version}/libexpect%{version}.so %{buildroot}/usr/lib

#---------------------------------------------------------------------------
%check
make test

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*
/usr/include/*
/usr/lib/expect%{version}
/usr/lib/lib*.so*

%else
/usr/bin/autoexpect
/usr/bin/autopasswd
/usr/bin/cryptdir
/usr/bin/decryptdir
/usr/bin/dislocate
/usr/bin/expect
/usr/bin/ftp-rfc
/usr/bin/kibitz
/usr/bin/lpunlock
/usr/bin/mkpasswd
/usr/bin/multixterm
/usr/bin/passmass
/usr/bin/rftp
/usr/bin/rlogin-cwd
/usr/bin/timed-read
/usr/bin/timed-run
/usr/bin/tknewsbiff
/usr/bin/tkpasswd
/usr/bin/unbuffer
/usr/bin/weather
/usr/bin/xkibitz
/usr/bin/xpstat
/usr/lib/expect%{version}/pkgIndex.tcl
/usr/lib/libexpect%{version}.so
/usr/lib/expect%{version}/libexpect%{version}.so

%files devel
/usr/include/*.h

%files man
/usr/share/man/man*/*.gz

%endif