%global version         2.7.6
%global _build_id_links none

Name:           patch
Version:        %{version}
Release:        1%{?dist}
Summary:        Utility for modifying/upgrading files
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/patch/patch-%{version}.tar.xz

%description
The patch program applies diff files to originals. The diff command is used to
compare an original to a changed file. Diff lists the changes made to the file.
A person who has the original file can then use the patch command with the diff
file to add the changes to their original file (patching the file).

Patch should be installed because it is a common way of upgrading applications.


%prep
%setup -q


%build
./configure --prefix=/usr
make


%check
make check


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/patch
/usr/share/man/man1/*
