Name:           sed
Version:        4.9
Release:        1%{?dist}
Summary:        A GNU stream text editor
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/sed/sed-%{version}.tar.xz

BuildRequires:  texinfo
Suggests:       %{name}-doc = %{version}

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive) editor.
Sed takes text as input, performs an operation or set of operations on the text
and outputs the modified text. The operations that sed performs (substitutions,
deletions, insertions, etc.) can be specified in a script file or from the
command line.

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
            --build=$(build-aux/config.guess)
%make

%else
./configure --prefix=/usr
%make
make html

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs
%discard_locales

%else
%make DESTDIR=%{buildroot} install
install -d -m755           %{buildroot}/usr/share/doc/sed-4.9
install -m644 doc/sed.html %{buildroot}/usr/share/doc/sed-4.9
%remove_info_dir

%endif

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*

%else
/usr/bin/sed

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif

