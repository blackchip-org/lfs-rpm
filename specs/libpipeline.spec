Name:           libpipeline
Version:        1.5.7
Release:        1%{?dist}
Summary:        A pipeline manipulation library
License:        GPLv3+

Source:         https://download.savannah.gnu.org/releases/libpipeline/libpipeline-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
libpipeline is a C library for setting up and running pipelines of processes,
without needing to involve shell command-line parsing which is often
error-prone and insecure. This alleviates programmers of the need to
laboriously construct pipelines using lower-level primitives such as fork(2)
and execve(2).

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
/usr/include/pipeline.h
/usr/lib/libpipeline.so
/usr/lib/libpipeline.so.1
%shlib /usr/lib/libpipeline.so.1.5.7
/usr/lib/pkgconfig/libpipeline.pc

%files doc
/usr/share/man/man*/*
