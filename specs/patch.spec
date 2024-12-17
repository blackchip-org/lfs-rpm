Name:           patch
Version:        2.7.6
Release:        1%{?dist}
Summary:        Utility for modifying/upgrading files
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/patch/patch-%{version}.tar.xz

%description
The patch program applies diff files to originals. The diff command is used to
compare an original to a changed file. Diff lists the changes made to the file.
A person who has the original file can then use the patch command with the diff
file to add the changes to their original file (patching the file).

Patch should be installed because it is a common way of upgrading applications.

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

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*

%else
/usr/bin/patch
/usr/share/man/man1/*

%endif

