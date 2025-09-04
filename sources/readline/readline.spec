# lfs

%global name            readline
%global version         8.3
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A library for editing typed command lines
License:        GPLv3+

Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
The Readline library provides a set of functions that allow users to edit
command lines. Both Emacs and vi editing modes are available. The Readline
library includes additional functions for maintaining a list of
previously-entered command lines for recalling or editing those lines, and for
performing csh-like history expansion on previous commands

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description info
Info documentation for %{name}

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
sed -i '/MV.*old/d' Makefile.in
sed -i '/{OLDSUFF}/c:' support/shlib-install

sed -i 's/-Wl,-rpath,[^ ]*//' support/shobj-conf

%if %{with lfs}
./configure --prefix=/usr    \
            --disable-static \
            --with-curses    \
            --docdir=/usr/share/doc/readline-%{version}

%else
./configure --prefix=/usr    \
            --with-curses    \
            --docdir=/usr/share/doc/readline-%{version}

%endif

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
/usr/lib/libhistory.so.*
/usr/lib/libreadline.so.*
/usr/share/%{name}

%files devel
/usr/include/%{name}
/usr/lib/libhistory.so
/usr/lib/libreadline.so
/usr/lib/pkgconfig/history.pc
/usr/lib/pkgconfig/readline.pc

%files doc
/usr/share/doc/%{name}-%{version}

%files info
/usr/share/info/*

%files man
/usr/share/man/man*/*

%files static
/usr/lib/libhistory.a
/usr/lib/libreadline.a

%endif
