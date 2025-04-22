# lfs

%global name        readline
%global version     8.2.13
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A library for editing typed command lines
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Recommends:     %{name}-man = %{version}

%description
The Readline library provides a set of functions that allow users to edit
command lines. Both Emacs and vi editing modes are available. The Readline
library includes additional functions for maintaining a list of
previously-entered command lines for recalling or editing those lines, and for
performing csh-like history expansion on previous commands

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
sed -i '/MV.*old/d' Makefile.in
sed -i '/{OLDSUFF}/c:' support/shlib-install

sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf

./configure --prefix=/usr    \
            --disable-static \
            --with-curses    \
            --docdir=/usr/share/doc/readline-%{version}
make %{_smp_mflags} SHLIB_LIBS="-lncursesw"

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} SHLIB_LIBS="-lncursesw" install
install -m 644 doc/*.{ps,pdf,html,dvi} -Dt %{buildroot}/usr/share/doc/readline-%{version}

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%dir /usr/include/readline
/usr/include/readline/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/share/doc/readline-%{version}
/usr/include/readline
/usr/lib/libhistory.so
/usr/lib/libhistory.so.8
%shlib /usr/lib/libhistory.so.%{version2}
/usr/lib/libreadline.so
/usr/lib/libreadline.so.8
%shlib /usr/lib/libreadline.so.%{version2}
/usr/lib/pkgconfig/history.pc
/usr/lib/pkgconfig/readline.pc

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
