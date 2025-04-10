Name:           diffutils
Version:        3.11
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

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(./build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
make DESTDIR=%{buildroot} install
%remove_info_dir

%endif

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
# %%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/diffutils.mo

%else
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif



