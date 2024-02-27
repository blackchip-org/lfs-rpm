Name:           gawk
Version:        5.3.0
Release:        1%{?dist}
Summary:        The GNU version of the AWK text processing utility
License:        GPLv3+ and GPLv2+ and LGPLv2+ and BSD

Source0:        https://ftp.gnu.org/gnu/gawk/gawk-%{version}.tar.xz

%description
The gawk package contains the GNU version of AWK text processing utility. AWK
is a programming language designed for text processing and typically used as a
data extraction and reporting tool.

The gawk utility can be used to do quick and easy text pattern matching,
extracting or reformatting. It is considered to be a standard Linux tool for
text processing.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

sed -i 's/extras//' Makefile.in

%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%else
make DESTDIR=%{buildroot} LN='ln -f' install
ln -sv gawk.1 %{buildroot}/usr/share/man/man1/awk.1

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/gawk
%{lfs_dir}/usr/libexec/awk
%{lfs_dir}/usr/share/awk
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/gawk.mo

%else
/usr/bin/awk
/usr/bin/gawk
/usr/bin/gawk-%{version}
/usr/bin/gawkbug
/usr/include/*.h
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
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/gawk.mo
/usr/share/man/man{1,3}/*

%endif




