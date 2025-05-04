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

%if !%{with lfs}
Recommends:     %{name}-man  = %{version}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
libpipeline is a C library for setting up and running pipelines of processes,
without needing to involve shell command-line parsing which is often
error-prone and insecure. This alleviates programmers of the need to
laboriously construct pipelines using lower-level primitives such as fork(2)
and execve(2).

%if !%{with lfs}
%description man
Manual pages for %{name}

%endif

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
/usr/lib/libpipeline.so*
/usr/lib/pkgconfig/%{name}.pc

%files man
/usr/share/man/man*/*.gz

%endif
