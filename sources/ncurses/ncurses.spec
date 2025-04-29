# lfs

%global name            ncurses
%global version         6.5
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Ncurses support utilities
License:        MIT

Source0:        https://invisible-mirror.net/archives/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization. The ncurses (new curses)
library is a freely distributable replacement for the discontinued 4.4 BSD
classic curses library.

This package contains support utilities, including a terminfo compiler tic, a
decompiler infocmp, clear, tput, tset, and a termcap conversion tool captoinfo.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
sed -i s/mawk// configure

mkdir build
pushd build
  ../configure
  make -C include
  make -C progs tic
popd

./configure --prefix=/usr                \
            --host=%{lfs_tgt}            \
            --build=$(./config.guess)    \
            --mandir=/usr/share/man      \
            --with-manpage-format=normal \
            --with-shared                \
            --without-normal             \
            --with-cxx-shared            \
            --without-debug              \
            --without-ada                \
            --disable-stripping

%else
./configure --prefix=/usr           \
            --mandir=/usr/share/man \
            --with-shared           \
            --without-debug         \
            --without-normal        \
            --with-cxx-shared       \
            --enable-pc-files       \
            --with-pkg-config-libdir=/usr/lib/pkgconfig

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
make DESTDIR=%{buildroot}/%{lfs_dir} TIC_PATH=$(pwd)/build/progs/tic install
echo "INPUT(-lncursesw)" > %{buildroot}/%{lfs_dir}/usr/lib/libncurses.so

%else
make DESTDIR=%{buildroot} install

for lib in ncurses form panel menu ; do
    rm -vf                    %{buildroot}/usr/lib/lib${lib}.so
    echo "INPUT(-l${lib}w)" > %{buildroot}/usr/lib/lib${lib}.so
    ln -sfv ${lib}w.pc        %{buildroot}/usr/lib/pkgconfig/${lib}.pc
done

rm -vf                     %{buildroot}/usr/lib/libcursesw.so
echo "INPUT(-lncursesw)" > %{buildroot}/usr/lib/libcursesw.so
ln -sfv libncurses.so      %{buildroot}/usr/lib/libcurses.so

mkdir -p        %{buildroot}/usr/share/doc
cp -v -R doc -T %{buildroot}/usr/share/doc/ncurses-6.4

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/lib*.so*
%{?lfs_dir}/usr/lib/{pkgconfig,terminfo}/*
%{?lfs_dir}/usr/share/tabset/*
%{?lfs_dir}/usr/share/terminfo/*

%else
/usr/bin/captoinfo
/usr/bin/clear
/usr/bin/infocmp
/usr/bin/infotocap
/usr/bin/ncursesw6-config
/usr/bin/reset
/usr/bin/tabs
/usr/bin/tic
/usr/bin/toe
/usr/bin/tput
/usr/bin/tset
/usr/lib/libcurses.so
/usr/lib/libcursesw.so
/usr/lib/libform.so
/usr/lib/libformw.so.*
/usr/lib/libmenu.so
/usr/lib/libmenuw.so.*
/usr/lib/libncurses++w.so.*
/usr/lib/libncurses.so
/usr/lib/libncursesw.so.*
/usr/lib/libpanel.so
/usr/lib/libpanelw.so.*
/usr/lib/terminfo
/usr/share/tabset/*
/usr/share/terminfo/*

%files devel
/usr/include/*.h
/usr/lib/libformw.so
/usr/lib/libmenuw.so
/usr/lib/libncurses++w.so
/usr/lib/libncursesw.so
/usr/lib/libpanelw.so
/usr/lib/pkgconfig/form.pc
/usr/lib/pkgconfig/formw.pc
/usr/lib/pkgconfig/menu.pc
/usr/lib/pkgconfig/menuw.pc
/usr/lib/pkgconfig/ncurses++w.pc
/usr/lib/pkgconfig/ncurses.pc
/usr/lib/pkgconfig/ncursesw.pc
/usr/lib/pkgconfig/panel.pc
/usr/lib/pkgconfig/panelw.pc

%files doc
/usr/share/doc/%{name}-*

%files man
/usr/share/man/man*/*.gz

%endif




