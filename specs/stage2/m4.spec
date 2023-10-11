%global version     1.4.19

Name:           m4
Version:        %{version}
Release:        1%{?dist}
Summary:        GNU macro processor
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz

%description
A GNU implementation of the traditional UNIX macro processor. M4 is useful for
writing text files which can be logically parsed, and is used by many programs
as part of their build process. M4 has built-in functions for including files,
running shell commands, doing arithmetic, etc. The autoconf program needs m4
for generating configure scripts, but not for running configure scripts.

Install m4 if you need a macro processor.


%global _build_id_links none


%prep
%setup -q


%build
./configure --prefix=/usr


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/m4 
/usr/share/info/* 
/usr/share/locale/*/LC_MESSAGES/m4.mo 
/usr/share/man/man1/m4.1.gz 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
