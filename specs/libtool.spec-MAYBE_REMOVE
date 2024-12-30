Name:           libtool
Version:        2.4.7
Release:        1%{?dist}
Summary:        The GNU Portable Library Tool
License:        GPLv2+ and LGPLv2+ and GFDL

Source0:        https://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz

%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf and
GNU Automake).

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
rm -fv %{buildroot}/usr/lib/libltdl.a
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make -k check

#---------------------------------------------------------------------------
%post
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/libtool
/usr/bin/libtoolize
/usr/include/libltdl
/usr/include/*.h
/usr/lib/libltdl.so
/usr/lib/libltdl.so.7
/usr/share/aclocal/*
/usr/share/info/*
/usr/share/libtool
/usr/share/man/man1/*

%defattr(755,root,root,755)
/usr/lib/libltdl.so.7.3.2
