%global version         3.11.4
%global version2        3.11
%global _build_id_links none

Name:           python
Version:        %{version}
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


%prep
%setup -q -n Python-%{version}


%build
./configure --prefix=/usr        \
            --enable-shared      \
            --with-system-expat  \
            --with-system-ffi    \
            --enable-optimizations
make


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/2to3
/usr/bin/2to3-%{version2}
/usr/bin/idle3
/usr/bin/idle%{version2}
/usr/bin/pip3
/usr/bin/pip%{version2}
/usr/bin/pydoc3
/usr/bin/pydoc%{version2}
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python%{version2}
/usr/bin/python%{version2}-config
/usr/include/python%{version2}
/usr/lib/libpython%{version2}.so
/usr/lib/libpython3.so
/usr/lib/pkgconfig/python-%{version2}-embed.pc
/usr/lib/pkgconfig/python-%{version2}.pc
/usr/lib/pkgconfig/python3-embed.pc
/usr/lib/pkgconfig/python3.pc
/usr/lib/python%{version2}
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libpython%{version2}.so.1.0