%global version     5.45.4

Name:           expect
Version:        %{version}
Release:        1%{?dist}
Summary:        A program-script interaction and testing utility
License:        Public Domain 

Source0:        https://prdownloads.sourceforge.net/expect/expect%{version}.tar.gz

%description
Expect is a tcl application for automating and testing interactive applications
such as telnet, ftp, passwd, fsck, rlogin, tip, etc. Expect makes it easy for a
script to control another program and interact with it.

This package contains expect and some scripts that use it.


%global _build_id_links none


%prep
%setup -q -n %{name}%{version}


%build
./configure --prefix=/usr           \
            --with-tcl=/usr/lib     \
            --enable-shared         \
            --mandir=/usr/share/man \
            --with-tclinclude=/usr/include
make 


%check 
make test


%install
make DESTDIR=%{buildroot} install
ln -svf expect%{version}/libexpect%{version}.so %{buildroot}/usr/lib


%files
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
/usr/include/* 
%attr(755,root,root) /usr/lib/expect5.45.4/libexpect5.45.4.so
/usr/lib/expect5.45.4/pkgIndex.tcl
/usr/lib/libexpect5.45.4.so
/usr/share/man/man{1,3}/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
