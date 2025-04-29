# lfs

%global name            python
%global source_name     Python
%global python_version  3.13
%global version         %{python_version}.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Interpreter of the Python programming language
License:        Python

Source0:        https://www.python.org/ftp/%{name}/%{version}/%{source_name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  expat-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
# Python test fails with 3.49
BuildRequires:  sqlite-devel = 3.48.0

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
Python is an accessible, high-level, dynamically typed, interpreted programming
language, designed with an emphasis on code readibility. It includes an
extensive standard library, and has a vast ecosystem of third-party libraries.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr   \
            --enable-shared \
            --without-ensurepip

%else
./configure --prefix=/usr        \
            --enable-shared      \
            --with-system-expat  \
            --enable-optimizations

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

# Some files get installed that trigger a dependency for /usr/local/bin/python
# and need to be fixed.
find %{buildroot} -type f -exec sed -i 's_/usr/local/bin/python_/usr/bin/python_g' {} \;

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
%if %{with lfs}
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
/usr/lib/libpython%{python_version}.so.*
/usr/lib/python%{python_version}

%files devel
/usr/include/python%{python_version}
/usr/lib/libpython3.so
/usr/lib/libpython%{python_version}.so
/usr/lib/pkgconfig/python-%{python_version}-embed.pc
/usr/lib/pkgconfig/python-%{python_version}.pc
/usr/lib/pkgconfig/python3-embed.pc
/usr/lib/pkgconfig/python3.pc
/usr/lib/rpm/macros.d/macros.python

%files man
/usr/share/man/man*/*

%endif

