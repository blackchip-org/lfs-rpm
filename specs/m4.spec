Name:           m4
Version:        1.4.19
Release:        1%{?dist}
Summary:        GNU macro processor
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz
Suggests:       %{name}-doc = %{version}

%description
A GNU implementation of the traditional UNIX macro processor. M4 is useful for
writing text files which can be logically parsed, and is used by many programs
as part of their build process. M4 has built-in functions for including files,
running shell commands, doing arithmetic, etc. The autoconf program needs m4
for generating configure scripts, but not for running configure scripts.

Install m4 if you need a macro processor.

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
%make DESTDIR=%{buildroot} install
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
%{lfs_dir}/usr/bin/m4
# %%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/m4.mo

%else
/usr/bin/m4

%files lang
/usr/share/locale/*/LC_MESSAGES/m4.mo

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
