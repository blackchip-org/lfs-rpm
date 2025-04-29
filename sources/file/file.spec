# lfs

%global name            file
%global version         5.46
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A utility for determining file types
License:        BSD

Source0:        https://astron.com/pub/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The file command is used to identify a particular file according to the type of
data contained by the file. File can identify many different file types,
including ELF binaries, system libraries, RPM packages, and different graphics
formats.

%if !%{with lfs}
%description devel
Development files for %{name}

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
mkdir build
pushd build
../configure    --disable-bzlib      \
                --disable-libseccomp \
                --disable-xzlib      \
                --disable-zlib
make %{?_smp_mflags}
popd

./configure --prefix=/usr --host=%{lfs_tgt} --build=$(./config.guess)
make %{?_smp_mflags} FILE_COMPILE=$(pwd)/build/src/file

%else
./configure --prefix=/usr
make %{?_smp_mflags}

%endif

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*.so*
%{?lfs_dir}/usr/lib/pkgconfig/libmagic.pc
%{?lfs_dir}/usr/share/misc/magic.mgc

%else
/usr/bin/file
/usr/lib/libmagic.so.*
/usr/share/misc/magic.mgc

%files devel
/usr/include/magic.h
/usr/lib/libmagic.so
/usr/lib/pkgconfig/libmagic.pc

%files man
/usr/share/man/man*/*.gz

%endif


