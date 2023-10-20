Name:           python
Version:        3.11.4
%global         python_version 3.11
Release:        1%{?dist}
Summary:        Interpreter of the Python programming language
License:        Python

Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

%description
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readibility. It includes an
extensive standard library, and has a vast ecosystem of third-party libraries.

The python36 package provides the "python3.6" executable: the reference
interpreter for the Python language, version 3. The package also installs the
"python3" executable which is user configurable using the "alternatives
--config python3" command. For the unversioned "python" command, see manual
page "unversioned-python".

The python36-devel package contains files for dovelopment of Python application
and the python36-debug is helpful for debugging.

Packages containing additional libraries for Python 3.6 are generally named
with the "python3-" prefix.

#---------------------------------------------------------------------------
%prep
%setup -q -n Python-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr   \
            --enable-shared \
            --without-ensurepip

%endif 
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/lib/rpm/macros.d
cat <<EOF | sed 's/@/%/' > %{buildroot}/usr/lib/rpm/macros.d/macros.python
@python_version %{python_version}
EOF
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
/usr/bin/*
/usr/include/python%{python_version}
/usr/lib/*.so*
/usr/lib/pkgconfig/*
/usr/lib/python%{python_version}
/usr/lib/rpm/macros.d/macros.python 

%endif 
