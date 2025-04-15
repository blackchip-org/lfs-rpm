# lfs

%global name        gawk
%global version     5.3.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU version of the AWK text processing utility
License:        GPLv3+ and GPLv2+ and LGPLv2+ and BSD

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
The gawk package contains the GNU version of AWK text processing utility. AWK
is a programming language designed for text processing and typically used as a
data extraction and reporting tool.

The gawk utility can be used to do quick and easy text pattern matching,
extracting or reformatting. It is considered to be a standard Linux tool for
text processing.

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
%verify_sha256
%setup -q

#---------------------------------------------------------------------------
%build
sed -i 's/extras//' Makefile.in

%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

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
%discard_locales

%else
make DESTDIR=%{buildroot} LN='ln -f' install
ln -sv gawk.1 %{buildroot}/usr/share/man/man1/awk.1
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
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/gawk
%{lfs_dir}/usr/libexec/awk
%{lfs_dir}/usr/share/awk

%else
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-%{version}
/usr/bin/gawkbug
/usr/include/*.h
%shlib /usr/lib/gawk/filefuncs.so
%shlib /usr/lib/gawk/fnmatch.so
%shlib /usr/lib/gawk/fork.so
%shlib /usr/lib/gawk/inplace.so
%shlib /usr/lib/gawk/intdiv.so
%shlib /usr/lib/gawk/ordchr.so
%shlib /usr/lib/gawk/readdir.so
%shlib /usr/lib/gawk/readfile.so
%shlib /usr/lib/gawk/revoutput.so
%shlib /usr/lib/gawk/revtwoway.so
%shlib /usr/lib/gawk/rwarray.so
%shlib /usr/lib/gawk/time.so
/usr/libexec/awk/grcat
/usr/libexec/awk/pwcat
/usr/share/awk

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif




