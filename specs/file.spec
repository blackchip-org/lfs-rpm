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
%if %{with lfs_stage1}
%use_lfs_tools
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

%else
./configure --prefix=/usr
%make

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
make DESTDIR=%{buildroot}/%{lfs_dir} install
rm %{buildroot}/%{lfs_dir}/usr/lib/libmagic.la
%discard_docs

%else
%make DESTDIR=%{buildroot} install

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*.so*
%{lfs_dir}/usr/lib/pkgconfig/libmagic.pc
%{lfs_dir}/usr/share/misc/magic.mgc

%else
/usr/bin/file
/usr/include/magic.h
/usr/lib/libmagic.so
/usr/lib/libmagic.so.1
/usr/lib/pkgconfig/libmagic.pc
/usr/share/man/man{1,3,4}/*
/usr/share/misc/magic.mgc

%defattr(755,root,root,755)
/usr/lib/libmagic.so.1.0.0

%endif


