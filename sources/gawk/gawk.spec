# lfs

%global name            gawk
%global version         5.3.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU version of the AWK text processing utility
License:        GPLv3+ and GPLv2+ and LGPLv2+ and BSD

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

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
The gawk package contains the GNU version of AWK text processing utility. AWK
is a programming language designed for text processing and typically used as a
data extraction and reporting tool.

The gawk utility can be used to do quick and easy text pattern matching,
extracting or reformatting. It is considered to be a standard Linux tool for
text processing.

%if !%{with lfs}
%description devel
Development files for %{name}

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
sed -i 's/extras//' Makefile.in

%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

%if !%{with lfs}
ln -sv gawk.1 %{buildroot}/usr/share/man/man1/awk.1
%endif

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/gawk
%{?lfs_dir}/usr/libexec/awk
%{?lfs_dir}/usr/share/awk

%else
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-%{version}
/usr/bin/gawkbug
/usr/lib/gawk/filefuncs.so
/usr/lib/gawk/fnmatch.so
/usr/lib/gawk/fork.so
/usr/lib/gawk/inplace.so
/usr/lib/gawk/intdiv.so
/usr/lib/gawk/ordchr.so
/usr/lib/gawk/readdir.so
/usr/lib/gawk/readfile.so
/usr/lib/gawk/revoutput.so
/usr/lib/gawk/revtwoway.so
/usr/lib/gawk/rwarray.so
/usr/lib/gawk/time.so
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat
/usr/share/awk

%files devel
/usr/include/*.h

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%endif




