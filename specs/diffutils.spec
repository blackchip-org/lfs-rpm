Name:           diffutils
Version:        3.10
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

#---------------------------------------------------------------------------
%prep
%setup -q


#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(./build-aux/config.guess)

%else 
./configure --prefix=/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%else 
make DESTDIR=%{buildroot} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/diffutils.mo

%else
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff
/usr/share/info/diffutils.info.gz
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man1/*

%endif



