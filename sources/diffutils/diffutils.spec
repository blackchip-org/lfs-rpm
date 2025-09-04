# lfs

%global name            diffutils
%global version         3.12
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU collection of diff utilities
License:        GPLv3+

Source:         https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

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

%if !%{with lfs}
%description info
Info documentation for %{name}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            gl_cv_func_strcasecmp_works=y \
            --build=$(./build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*

%else
/usr/bin/cmp
/usr/bin/diff
/usr/bin/diff3
/usr/bin/sdiff

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%endif



