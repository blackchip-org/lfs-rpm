# lfs

%global name        libpipeline
%global version     1.5.8
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A pipeline manipulation library
License:        GPLv3+

Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include
/usr/lib/lib*.so*
/usr/lib/pkgconfig

%else
/usr/include/pipeline.h
/usr/lib/libpipeline.so
/usr/lib/libpipeline.so.1
%shlib /usr/lib/libpipeline.so.1.5.8
/usr/lib/pkgconfig/libpipeline.pc

%files doc
/usr/share/man/man*/*

%endif
