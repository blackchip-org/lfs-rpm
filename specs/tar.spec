Name:           tar
Version:        1.35
Release:        1%{?dist}
Summary:        A GNU file archiving program
License:        GPLv3+

Source:         https://ftp.gnu.org/gnu/tar/tar-%{version}.tar.xz

Suggests:       %{name}-doc = %{version}

%description
The GNU tar program saves many files together in one archive and can restore
individual files (or all of the files) from that archive. Tar can also be used
to add supplemental files to an archive and to update or list files in the
archive. Tar includes multivolume support, automatic archive
compression/decompression, the ability to perform remote archives, and the
ability to perform incremental and full backups.

If you want to use tar for remote backups, you also need to install the rmt
package on the remote box.

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
FORCE_UNSAFE_CONFIGURE=1  \
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
%check
make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/libexec/*
# %%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/tar.mo

%else
/usr/bin/tar
/usr/libexec/rmt

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif

