Name:           libpipeline
Version:        1.5.7
Release:        1%{?dist}
Summary:        A pipeline manipulation library
License:        GPLv3+

Source0:        https://download.savannah.gnu.org/releases/libpipeline/libpipeline-%{version}.tar.gz

%description
libpipeline is a C library for setting up and running pipelines of processes,
without needing to involve shell command-line parsing which is often
error-prone and insecure. This alleviates programmers of the need to
laboriously construct pipelines using lower-level primitives such as fork(2)
and execve(2).

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./configure --prefix=/usr
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
/usr/include/pipeline.h
/usr/lib/libpipeline.so
/usr/lib/libpipeline.so.1
/usr/lib/pkgconfig/libpipeline.pc
/usr/share/man/man3/*

%defattr(755,root,root,755)
/usr/lib/libpipeline.so.1.5.7
