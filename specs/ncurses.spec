Name:           ncurses
Version:        6.4
Release:        1%{?dist}
Summary:        Ncurses support utilities
License:        MIT

Source0:        https://invisible-mirror.net/archives/ncurses/ncurses-%{version}.tar.gz

%description
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization. The ncurses (new curses)
library is a freely distributable replacement for the discontinued 4.4 BSD
classic curses library.

This package contains support utilities, including a terminfo compiler tic, a
decompiler infocmp, clear, tput, tset, and a termcap conversion tool captoinfo.

#---------------------------------------------------------------------------
%prep
%setup -q -n ncurses-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
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
            --disable-stripping          \
            --enable-widec

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
make DESTDIR=%{buildroot}/%{lfs_dir} TIC_PATH=$(pwd)/build/progs/tic install
echo "INPUT(-lncursesw)" > %{buildroot}/%{lfs_dir}/usr/lib/libncurses.so

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*
%{lfs_dir}/usr/share/tabset/*
%{lfs_dir}/usr/share/terminfo/*/*
%endif




