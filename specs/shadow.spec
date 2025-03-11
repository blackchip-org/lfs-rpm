Name:           shadow
Version:        4.17.3
Release:        1%{?dist}
Summary:        Utilities for managing accounts and shadow password files
License:        BSD and GPLv2+

Source:         https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

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

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
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

./configure --sysconfdir=/etc   \
            --disable-static    \
            --with-{b,yes}crypt \
            --without-libbsd    \
            --with-group-name-max-length=32
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} exec_prefix=/usr install
%make -C man DESTDIR=%{buildroot} install-man

#---------------------------------------------------------------------------
%post

/usr/sbin/pwconv
/usr/sbin/grpconv
mkdir -p /etc/default
useradd -D --gid 999
sed -i '/MAIL/s/yes/no/' /etc/default/useradd

#---------------------------------------------------------------------------
%files
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
/usr/include/shadow
/usr/lib/libsubid.so
/usr/lib/libsubid.so.5
%shlib /usr/lib/libsubid.so.5.0.0
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

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/man/man*/*

