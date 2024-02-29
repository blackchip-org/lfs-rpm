Name:           man-pages
Version:        6.06
Release:        1%{?dist}
Summary:        Linux kernel and C library user-space interface documentation
License:        GPL+ and GPLv2+ and BSD and MIT and Copyright only

Source0:        https://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz

%description
A large collection of manual pages from the Linux Documentation Project (LDP).

#---------------------------------------------------------------------------
%prep
%setup -q -n man-pages-%{version}

#---------------------------------------------------------------------------
%build
%lfs_build_begin

rm -v man3/crypt*
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%make prefix=/usr DESTDIR=%{buildroot} install
%lfs_install_end

#---------------------------------------------------------------------------
%files
/usr/share/man/man{1,2,3,4,5,6,7,8}/*
/usr/share/man/man{2,3}type/*
/usr/share/man/man3const/*
/usr/share/man/man3head/*
