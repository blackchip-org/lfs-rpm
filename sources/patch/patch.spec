# lfs

%global name        patch
%global version     2.7.6
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utility for modifying/upgrading files
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
The patch program applies diff files to originals. The diff command is used to
compare an original to a changed file. Diff lists the changes made to the file.
A person who has the original file can then use the patch command with the diff
file to add the changes to their original file (patching the file).

Patch should be installed because it is a common way of upgrading applications.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

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
./configure --prefix=/usr

%endif
make -j %{nproc}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{lfs_dir}/usr/bin/*

%else
/usr/bin/patch

%files doc
/usr/share/man/man*/*

%endif

