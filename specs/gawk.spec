Name:           gawk
Version:        5.2.2
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

%if %{with lfs_bootstrap}
sed -i 's/extras//' Makefile.in
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/gawk
%{lfs_dir}/usr/libexec/awk
%{lfs_dir}/usr/share/awk
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/gawk.mo
%endif




