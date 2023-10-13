%define version   3.11

Name:           grep
Version:        %{version}
Release:        1%{?dist}
Summary:        Pattern matching utilities
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

%global _build_id_links none

%description

The GNU versions of commonly used grep utilities. Grep searches
through textual input for lines which contain a match to a specified
pattern and then prints the matching lines. GNU's grep utilities
include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be installed on every
system.


%prep
%setup -q


%build
sed -i "s/echo/#echo/" src/egrep.sh
./configure --prefix=/usr
make


%check
make check


%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/usr/share/info/dir


%files
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man1/*
   
   
%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4-1
- Initial package


