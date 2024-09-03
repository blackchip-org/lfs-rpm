Name:           readline
Version:        8.2.13
%global         version2    8.2
Release:        1%{?dist}
Summary:        A library for editing typed command lines
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz

%description
The Readline library provides a set of functions that allow users to edit
command lines. Both Emacs and vi editing modes are available. The Readline
library includes additional functions for maintaining a list of
previously-entered command lines for recalling or editing those lines, and for
performing csh-like history expansion on previous commands

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

sed -i '/MV.*old/d' Makefile.in
sed -i '/{OLDSUFF}/c:' support/shlib-install

sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf

./configure --prefix=/usr    \
            --disable-static \
            --with-curses    \
            --docdir=/usr/share/doc/readline-%{version}
%make SHLIB_LIBS="-lncursesw"
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} SHLIB_LIBS="-lncursesw" install
install -m 644 doc/*.{ps,pdf,html,dvi} -Dt %{buildroot}/usr/share/doc/readline-%{version}
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/share/doc/readline-%{version}
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
/usr/lib/libhistory.so.%{version2}
/usr/lib/libreadline.so.%{version2}
