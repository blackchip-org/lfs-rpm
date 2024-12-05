Name:		libsolv
Version:	0.7.21
Release:	1%{?dist}
Summary:	Dependency solver using a satisfiability algorithm
License:    BSD

Source0:	https://github.com/openSUSE/libsolv/archive/refs/tags/%{version}.tar.gz

%global     cmake_version 3.30

%description
This is libsolv, a free package dependency solver using a satisfiability
algorithm.

The code is based on two major, but independent, blocks:

    Using a dictionary approach to store and retrieve package and dependency information in a fast and space efficient manner.

    Using satisfiability, a well known and researched topic, for resolving package dependencies.

The sat-solver code has been written to aim for the newest packages, record the
decision tree to provide introspection, and also provides the user with
suggestions on how to deal with unsolvable problems. It also takes advantage of
repository storage to minimize memory usage.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    ..
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd build
make DESTDIR=%{buildroot} install
mv %{buildroot}/usr/share/cmake \
   %{buildroot}/usr/share/cmake-%{cmake_version}

%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/bin/dumpsolv
/usr/bin/installcheck
/usr/bin/mergesolv
/usr/bin/repo2solv
/usr/bin/testsolv
/usr/include/solv
/usr/lib/libsolv.so
/usr/lib/libsolv.so.1
/usr/lib/libsolvext.so
/usr/lib/libsolvext.so.1
/usr/lib/pkgconfig/libsolv.pc
/usr/lib/pkgconfig/libsolvext.pc
/usr/share/cmake-%{cmake_version}/Modules/FindLibSolv.cmake
/usr/share/man/man{1,3}/*