Name:           shadow
Version:        4.14.5
Release:        1%{?dist}
Summary:        Utilities for managing accounts and shadow password files
License:        BSD and GPLv2+

Source0:        https://github.com/shadow-maint/shadow/releases/download/%{version}/shadow-%{version}.tar.xz

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

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

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
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} exec_prefix=/usr install
%make -C man DESTDIR=%{buildroot} install-man
%lfs_install_end

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
/usr/lib/libsubid.so.4
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
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man{1,3,5,8}/*

%defattr(755,root,root,755)
/usr/lib/libsubid.so.4.0.0
