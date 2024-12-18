Name:           python
Version:        3.12.5
%global         python_version 3.12
Release:        1%{?dist}
Summary:        Interpreter of the Python programming language
License:        Python

Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

BuildRequires:  expat
BuildRequires:  openssl

%description
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readibility. It includes an
extensive standard library, and has a vast ecosystem of third-party libraries.

#---------------------------------------------------------------------------
%prep
%setup -q -n Python-%{version}

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr   \
            --enable-shared \
            --without-ensurepip

%else
./configure --prefix=/usr        \
            --enable-shared      \
            --with-system-expat  \
            --enable-optimizations

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
make DESTDIR=%{buildroot} install
%discard_docs

%else
make DESTDIR=%{buildroot} install

%endif
mkdir -p %{buildroot}/usr/lib/rpm/macros.d
cat <<EOF | sed 's/@/%/' > %{buildroot}/usr/lib/rpm/macros.d/macros.python
@python_version %{python_version}
EOF

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
/usr/bin/*
/usr/include/python%{python_version}
/usr/lib/*.so*
/usr/lib/pkgconfig/*
/usr/lib/python%{python_version}
/usr/lib/rpm/macros.d/macros.python

%else
/usr/bin/2to3
/usr/bin/2to3-%{python_version}
/usr/bin/idle3
/usr/bin/idle%{python_version}
/usr/bin/pip3
/usr/bin/pip%{python_version}
/usr/bin/pydoc3
/usr/bin/pydoc%{python_version}
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python%{python_version}
/usr/bin/python%{python_version}-config
/usr/include/python%{python_version}
/usr/lib/libpython%{python_version}.so
/usr/lib/libpython3.so
/usr/lib/pkgconfig/python-%{python_version}-embed.pc
/usr/lib/pkgconfig/python-%{python_version}.pc
/usr/lib/pkgconfig/python3-embed.pc
/usr/lib/pkgconfig/python3.pc
/usr/lib/python%{python_version}
/usr/lib/rpm/macros.d/macros.python
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libpython%{python_version}.so.1.0

%endif

