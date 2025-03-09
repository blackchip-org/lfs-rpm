Name:           python
Version:        3.13.2
%global         python_version 3.13
Release:        1%{?dist}
Summary:        Interpreter of the Python programming language
License:        Python

Source:         https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

BuildRequires:  expat
BuildRequires:  openssl
Suggests:       %{name}-doc = %{version}

%description
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readibility. It includes an
extensive standard library, and has a vast ecosystem of third-party libraries.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

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

# Some files get installed that trigger a dependency for /usr/local/bin/python
# and need to be fixed.
find %{buildroot} -type f -exec sed -i 's_/usr/local/bin/python_/usr/bin/python_g' {} \;

%endif

# Add symlinks from unverisoned binaries to versioned (python -> python3)
ln -s python3       %{buildroot}/usr/bin/python
ln -s pyton3-config %{buildroot}/usr/bin/python-config
ln -s pydoc3        %{buildroot}/usr/bin/pydoc
ln -s pip3          %{buildroot}/usr/bin/pip
ln -s idle3         %{buildroot}/usr/bin/idle

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
/usr/bin/{idle,idle3,idle%{python_version}}
/usr/bin/{pip,pip3,pip%{python_version}}
/usr/bin/{pydoc,pydoc3,pydoc%{python_version}}
/usr/bin/{python,python3,python%{python_version}}
/usr/bin/{python-config,python3-config,python%{python_version}-config}
/usr/include/python%{python_version}
/usr/lib/libpython%{python_version}.so
/usr/lib/libpython3.so
%shlib /usr/lib/libpython%{python_version}.so.1.0
/usr/lib/pkgconfig/python-%{python_version}-embed.pc
/usr/lib/pkgconfig/python-%{python_version}.pc
/usr/lib/pkgconfig/python3-embed.pc
/usr/lib/pkgconfig/python3.pc
/usr/lib/python%{python_version}
/usr/lib/rpm/macros.d/macros.python

%files doc
/usr/share/man/man*/*

%endif

