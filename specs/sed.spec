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
rm -rf      %{name}-%{version}
tar xf      %{_sourcedir}/%{name}/%{name}-%{version}.tar.xz
cd          %{name}-%{version}

#---------------------------------------------------------------------------
%build
cd %{name}-%{version}

%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)
%make

%else
./configure --prefix=/usr
%make
make html

%endif

#---------------------------------------------------------------------------
%install
cd %{name}-%{version}

%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install
install -d -m755           %{buildroot}/usr/share/doc/sed-4.9
install -m644 doc/sed.html %{buildroot}/usr/share/doc/sed-4.9

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/sed.mo

%else
/usr/bin/sed
/usr/share/doc/%{name}-%{version}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man1/*

%endif

