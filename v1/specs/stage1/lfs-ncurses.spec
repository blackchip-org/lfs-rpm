Name:           lfs-ncurses
Version:        6.4
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        X11

Source0:        https://invisible-mirror.net/archives/ncurses/ncurses-%{version}.tar.gz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n ncurses-%{version}


%build
%lfs_path

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
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} TIC_PATH=$(pwd)/build/progs/tic install
echo "INPUT(-lncursesw)" > %{buildroot}/%{lfs}/usr/lib/libncurses.so
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/*
%{lfs}/usr/lib/*
%{lfs}/usr/share/tabset/*
%{lfs}/usr/share/terminfo/*/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4-1
- Initial package


