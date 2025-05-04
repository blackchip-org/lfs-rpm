# lfs

%global name            tar
%global version         1.35
%global release         1

#---------------------------------------------------------------------------
Name:           tar
Version:        1.35
Release:        1%{?dist}
Summary:        A GNU file archiving program
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/tar/tar-%{version}.tar.xz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

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
The GNU tar program saves many files together in one archive and can restore
individual files (or all of the files) from that archive. Tar can also be used
to add supplemental files to an archive and to update or list files in the
archive. Tar includes multivolume support, automatic archive
compression/decompression, the ability to perform remote archives, and the
ability to perform incremental and full backups.

If you want to use tar for remote backups, you also need to install the rmt
package on the remote box.

%if !%{with lfs}
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
%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else
FORCE_UNSAFE_CONFIGURE=1  \
./configure --prefix=/usr

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/libexec/*

%else
/usr/bin/tar
/usr/libexec/rmt

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%endif

