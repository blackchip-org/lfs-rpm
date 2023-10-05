Name:           file-lfs
Version:        5.45
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        BSD

Source0:        file-%{version}.tar.gz

Prefix:         %lfs

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n file-%{version}


%build
%lfs_path
mkdir build
pushd build
  ../configure --disable-bzlib      \
               --disable-libseccomp \
               --disable-xzlib      \
               --disable-zlib
  make
popd

./configure --prefix=/usr --host=%{lfs_tgt} --build=$(./config.guess)
make FILE_COMPILE=$(pwd)/build/src/file


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
rm %{buildroot}/%{lfs}/usr/lib/libmagic.la
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/*
%{lfs}/usr/lib/*.so*
%{lfs}/usr/lib/pkgconfig/libmagic.pc
%{lfs}/usr/share/misc/magic.mgc


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.45-1
- Initial package


