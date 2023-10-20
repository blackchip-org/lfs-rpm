Name:           sed
Version:        4.9
Release:        1%{?dist}
Summary:        A GNU stream text editor
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/sed/sed-%{version}.tar.xz

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive) editor.
Sed takes text as input, performs an operation or set of operations on the text
and outputs the modified text. The operations that sed performs (substitutions,
deletions, insertions, etc.) can be specified in a script file or from the
command line.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
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
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/sed.mo
%endif

