# lfs

%global name            man-pages
%global version         6.12
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Linux kernel and C library user-space interface documentation
License:        GPL+ and GPLv2+ and BSD and MIT and Copyright only

Source:         https://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz

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
%make -R GIT=false prefix=/usr DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/bin/diffman-git
/usr/bin/mansect
/usr/bin/pdfman
/usr/bin/sortman
/usr/share/man/man{1,2,3,4,5,6,7,8}/*
/usr/share/man/man{2,3}type/*
/usr/share/man/man{2,3}const/*
/usr/share/man/man3head/*
