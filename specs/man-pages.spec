Name:           man-pages
Version:        6.9.1
Release:        1%{?dist}
Summary:        Linux kernel and C library user-space interface documentation
License:        GPL+ and GPLv2+ and BSD and MIT and Copyright only

Source:         https://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz

Requires:       man-db

%description
A large collection of manual pages from the Linux Documentation Project (LDP).

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
rm -v man3/crypt*

#---------------------------------------------------------------------------
%install
%make prefix=/usr DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/share/man/man{1,2,3,4,5,6,7,8}/*
/usr/share/man/man{2,3}type/*
/usr/share/man/man{2,3}const/*
/usr/share/man/man3head/*
