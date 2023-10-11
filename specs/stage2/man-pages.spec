%global version     6.05.01

Name:           man-pages
Version:        %{version}
Release:        1%{?dist}
Summary:        Linux kernel and C library user-space interface documentation
License:        GPL+ and GPLv2+ and BSD and MIT and Copyright only

Source0:        https://www.kernel.org/pub/linux/docs/man-pages/man-pages-%{version}.tar.xz


%description
A large collection of manual pages from the Linux Documentation Project (LDP).


%global _build_id_links none


%prep
%setup -q -n man-pages-%{version}


%build
rm -v man3/crypt*


%install
make prefix=/usr DESTDIR=%{buildroot} install


%files
/usr/share/man/man{1,2,3,4,5,6,7,8}/*
/usr/share/man/man{2,3}type/*
/usr/share/man/man3const/*
/usr/share/man/man3head/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
