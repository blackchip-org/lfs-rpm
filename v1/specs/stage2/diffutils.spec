%global version         3.10
%global _build_id_links none

Name:           diffutils
Version:        %{version}
Release:        1%{?dist}
Summary:        A GNU collection of diff utilities
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/diffutils/diffutils-%{version}.tar.xz

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff compares
two files and shows the differences, line by line. The cmp command shows the
offset and line numbers where two files differ, or cmp can show the characters
that differ between the two files. The diff3 command shows the differences
between three files. Diff3 can be used when two people have made independent
changes to a common original; diff3 can produce a merged file that contains
both sets of changes and warnings about conflicts. The sdiff command can be
used to merge two files interactively.

Install diffutils if you need to compare text files.


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
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff
/usr/share/info/diffutils.info.gz
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man1/*
