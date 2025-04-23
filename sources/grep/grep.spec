# lfs

%global name        grep
%global version     3.11
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Pattern matching utilities
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
The GNU versions of commonly used grep utilities. Grep searches
through textual input for lines which contain a match to a specified
pattern and then prints the matching lines. GNU's grep utilities
include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be installed on every
system.

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(./build-aux/config.guess)

%else
sed -i "s/echo/#echo/" src/egrep.sh
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
%{?lfs_dir}/usr/bin

%else
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
