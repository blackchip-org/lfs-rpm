%define version   4.9

Name:           sed
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU stream text editor
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/sed/sed-%{version}.tar.xz

%global _build_id_links none

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive) editor.
Sed takes text as input, performs an operation or set of operations on the text
and outputs the modified text. The operations that sed performs (substitutions,
deletions, insertions, etc.) can be specified in a script file or from the
command line.


%prep
%setup -q


%build
./configure --prefix=/usr
make
make html


%check
make check


%install
make DESTDIR=%{buildroot} install
install -d -m755           %{buildroot}/usr/share/doc/sed-4.9
install -m644 doc/sed.html %{buildroot}/usr/share/doc/sed-4.9

rm -rf %{buildroot}/usr/share/info/dir


%files
/usr/bin/sed
/usr/share/doc/%{name}-%{version}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man1/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4-1
- Initial package


