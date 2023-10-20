Name:           file
Version:        5.45
Release:        1%{?dist}
Summary:        A utility for determining file types
License:        BSD

Source0:        https://astron.com/pub/file/file-%{version}.tar.gz

%description
The file command is used to identify a particular file according to the type of
data contained by the file. File can identify many different file types,
including ELF binaries, system libraries, RPM packages, and different graphics
formats.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
mkdir build
pushd build
  ../configure --disable-bzlib      \
               --disable-libseccomp \
               --disable-xzlib      \
               --disable-zlib
  %make
popd

./configure --prefix=/usr --host=%{lfs_tgt} --build=$(./config.guess)
%make FILE_COMPILE=$(pwd)/build/src/file

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
make DESTDIR=%{buildroot}/%{lfs_dir} install
rm %{buildroot}/%{lfs_dir}/usr/lib/libmagic.la

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/libmagic.pc
%{lfs_dir}/usr/share/misc/magic.mgc
%endif


