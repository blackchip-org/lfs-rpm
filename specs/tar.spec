Name:           tar
Version:        1.35
Release:        1%{?dist}
Summary:        A GNU file archiving program
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/tar/tar-%{version}.tar.xz

%description
The GNU tar program saves many files together in one archive and can restore
individual files (or all of the files) from that archive. Tar can also be used
to add supplemental files to an archive and to update or list files in the
archive. Tar includes multivolume support, automatic archive
compression/decompression, the ability to perform remote archives, and the
ability to perform incremental and full backups.

If you want to use tar for remote backups, you also need to install the rmt
package on the remote box.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else 
FORCE_UNSAFE_CONFIGURE=1  \
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
%make DESTDIR=%{buildroot} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/libexec/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/tar.mo

%else 
/usr/bin/tar
/usr/libexec/rmt
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man{1,8}/*

%endif

