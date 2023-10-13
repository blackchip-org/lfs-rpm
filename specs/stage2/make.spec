%global version         4.4.1
%global _build_id_links none

Name:           make
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU tool which simplifies the build process for users
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/make/make-%{version}.tar.gz

%description
A GNU tool for controlling the generation of executables and other non-source
files of a program from the program's source files. Make allows users to build
and install packages without any significant knowledge about the details of the
build process. The details about how the program should be built are provided
for make in the program's makefile.


%prep
%setup -q


%build
./configure --prefix=/usr
make


%check
make check


%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/share/info/dir


%files
/usr/bin/make
/usr/include/*.h
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/make.mo
/usr/share/man/man1/*
