# dnf

%global name            libsolv
%global version         0.7.31
%global release         1

# TODO: Have cmake define this macro
%global cmake_version   3.30

#---------------------------------------------------------------------------
Name:		    %{name}
Version:	    %{version}
Release:	    %{release}%{?dist}
Summary:	    Dependency solver using a satisfiability algorithm
License:        BSD

Source0:	    https://github.com/openSUSE/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        %{name}.sha256

BuildRequires:  cmake
BuildRequires:  libxml2
Suggests:       %{name}-doc = %{version}

%description
This is libsolv, a free package dependency solver using a satisfiability
algorithm.

The code is based on two major, but independent, blocks:

Using a dictionary approach to store and retrieve package and dependency
information in a fast and space efficient manner.

Using satisfiability, a well known and researched topic, for resolving
package dependencies.

The sat-solver code has been written to aim for the newest packages, record the
decision tree to provide introspection, and also provides the user with
suggestions on how to deal with unsolvable problems. It also takes advantage of
repository storage to minimize memory usage.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DENABLE_COMPLEX_DEPS=ON \
    -DENABLE_RPMDB=ON \
    -DENABLE_RPMMD=ON \
    -DENABLE_RPMPKG=ON \
    -DENABLE_RPMDB_BYRPMHEADER=ON \
    -DENABLE_RPMDB_LIBRPM=ON \
    -DENABLE_COMPS=ON \
    -DWITH_LIBXML2=ON \
    -DMULTI_SEMANTICS=ON \
    ..
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
cd build
make DESTDIR=%{buildroot} install
mv %{buildroot}/usr/share/cmake \
   %{buildroot}/usr/share/cmake-%{cmake_version}

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin
/usr/include/solv
/usr/lib/lib*.so*
/usr/lib/pkgconfig
/usr/share/cmake-%{cmake_version}

%else
/usr/bin/comps2solv
/usr/bin/deltainfoxml2solv
/usr/bin/dumpsolv
/usr/bin/installcheck
/usr/bin/mergesolv
/usr/bin/repo2solv
/usr/bin/repomdxml2solv
/usr/bin/rpmdb2solv
/usr/bin/rpmmd2solv
/usr/bin/rpms2solv
/usr/bin/testsolv
/usr/bin/updateinfoxml2solv
/usr/include/solv
/usr/lib/libsolv.so
/usr/lib/libsolv.so.1
/usr/lib/libsolvext.so
/usr/lib/libsolvext.so.1
/usr/lib/pkgconfig/libsolv.pc
/usr/lib/pkgconfig/libsolvext.pc
/usr/share/cmake-%{cmake_version}/Modules/FindLibSolv.cmake

%files doc
/usr/share/man/man*/*

%endif
