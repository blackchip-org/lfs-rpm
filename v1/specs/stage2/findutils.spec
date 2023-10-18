%global version         4.9.0
%global _build_id_links none

Name:           findutils
Version:        %{version}
Release:        1%{?dist}
Summary:        The GNU versions of find utilities (find and xargs)
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/findutils/findutils-%{version}.tar.xz

%description
The findutils package contains programs which will help you locate files on
your system. The find utility searches through a hierarchy of directories
looking for files which match a certain set of criteria (such as a file name
pattern). The xargs utility builds and executes command lines from standard
input arguments (usually lists of file names generated by the find command).

You should install findutils because it includes tools that are very useful for
finding things on your system.


%prep
%setup -q


%build
./configure --prefix=/usr --localstatedir=/var/lib/locate
make


%check
make check


%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/share/info/dir


%files
/usr/bin/find
/usr/bin/locate
/usr/bin/updatedb
/usr/bin/xargs
/usr/libexec/frcode
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/findutils.mo
/usr/share/man/man{1,5}/*