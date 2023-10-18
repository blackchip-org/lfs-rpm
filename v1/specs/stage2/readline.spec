%global version     8.2
%global lfs_version 12.0 

Name:           readline
Version:        %{version}
Release:        1%{?dist}
Summary:        A library for editing typed command lines
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/readline-%{version}-upstream_fix-1.patch

%description
The Readline library provides a set of functions that allow users to edit
command lines. Both Emacs and vi editing modes are available. The Readline
library includes additional functions for maintaining a list of
previously-entered command lines for recalling or editing those lines, and for
performing csh-like history expansion on previous commands


%global _build_id_links none


%prep
%setup -q
%patch 0 -p1 


%build
sed -i '/MV.*old/d' Makefile.in
sed -i '/{OLDSUFF}/c:' support/shlib-install

./configure --prefix=/usr    \
            --disable-static \
            --with-curses    \
            --docdir=/usr/share/doc/readline-%{version}
make SHLIB_LIBS="-lncursesw"


%install
make DESTDIR=%{buildroot} SHLIB_LIBS="-lncursesw" install
install -m 644 doc/*.{ps,pdf,html,dvi} -Dt %{buildroot}/usr/share/doc/readline-%{version}
rm %{buildroot}/usr/share/info/dir


%files
%doc /usr/share/doc/readline-%{version}
/usr/include/readline 
/usr/lib/libhistory.so
/usr/lib/libhistory.so.8
/usr/lib/libreadline.so
/usr/lib/libreadline.so.8
/usr/lib/pkgconfig/history.pc 
/usr/lib/pkgconfig/readline.pc 
/usr/share/info/* 
/usr/share/man/man3/*

%defattr(755,root,root,755)
/usr/lib/libhistory.so.%{version}
/usr/lib/libreadline.so.%{version}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial pack/etc/ld.so.cache
