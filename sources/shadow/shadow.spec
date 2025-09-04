# lfs

%global name            shadow
%global version         4.18.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utilities for managing accounts and shadow password files
License:        BSD and GPLv2+

Source0:        https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  libxcrypt-devel

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The shadow-utils package includes the necessary programs for converting UNIX
password files to the shadow password format, plus programs for managing user
and group accounts. The pwconv command converts passwords to the shadow
password format. The pwunconv command unconverts shadow passwords and generates
a passwd file (a standard UNIX password file). The pwck command checks the
integrity of password and shadow files. The lastlog command prints out the last
login times for all users. The useradd, userdel, and usermod commands are used
for managing user accounts. The groupadd, groupdel, and groupmod commands are
used for managing group accounts.

%if !%{with lfs}
%description devel
Development files for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
sed -i 's/groups$(EXEEXT) //' src/Makefile.in
find man -name Makefile.in -exec sed -i 's/groups\.1 / /'   {} \;
find man -name Makefile.in -exec sed -i 's/getspnam\.3 / /' {} \;
find man -name Makefile.in -exec sed -i 's/passwd\.5 / /'   {} \;

sed -e 's:#ENCRYPT_METHOD DES:ENCRYPT_METHOD YESCRYPT:' \
    -e 's:/var/spool/mail:/var/mail:'                   \
    -e '/PATH=/{s@/sbin:@@;s@/bin:@@}'                  \
    -i etc/login.defs

%if %{with lfs}
./configure --sysconfdir=/etc   \
            --disable-static    \
            --with-{b,yes}crypt \
            --without-libbsd    \
            --with-group-name-max-length=32

%else
./configure --sysconfdir=/etc   \
            --with-{b,yes}crypt \
            --without-libbsd    \
            --with-group-name-max-length=32

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} exec_prefix=/usr install

%if !%{with lfs}
make -C man DESTDIR=%{buildroot} install-man

%endif

#---------------------------------------------------------------------------
%post
/usr/sbin/pwconv
/usr/sbin/grpconv
mkdir -p /etc/default
useradd -D --gid 999
sed -i '/MAIL/s/yes/no/' /etc/default/useradd

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/etc/*
/usr/bin/*
/usr/include/shadow
/usr/lib/lib*.so*
/usr/sbin/*

%else
%config(noreplace) /etc/limits
%config(noreplace) /etc/login.access
%config(noreplace) /etc/login.defs
/usr/bin/chage
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/expiry
/usr/bin/faillog
/usr/bin/getsubids
/usr/bin/gpasswd
/usr/bin/login
/usr/bin/newgidmap
/usr/bin/newgrp
/usr/bin/newuidmap
/usr/bin/passwd
/usr/bin/sg
/usr/bin/su
/usr/lib/libsubid.so.*
/usr/sbin/chgpasswd
/usr/sbin/chpasswd
/usr/sbin/groupadd
/usr/sbin/groupdel
/usr/sbin/groupmems
/usr/sbin/groupmod
/usr/sbin/grpck
/usr/sbin/grpconv
/usr/sbin/grpunconv
/usr/sbin/logoutd
/usr/sbin/newusers
/usr/sbin/nologin
/usr/sbin/pwck
/usr/sbin/pwconv
/usr/sbin/pwunconv
/usr/sbin/useradd
/usr/sbin/userdel
/usr/sbin/usermod
/usr/sbin/vigr
/usr/sbin/vipw

%files devel
/usr/include/shadow
/usr/lib/libsubid.so

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*

%files static
/usr/lib/libsubid.a

%endif
