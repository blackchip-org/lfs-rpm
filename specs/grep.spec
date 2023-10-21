Name:           grep
Version:        3.11
Release:        1%{?dist}
Summary:        Pattern matching utilities
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz

%description
The GNU versions of commonly used grep utilities. Grep searches
through textual input for lines which contain a match to a specified
pattern and then prints the matching lines. GNU's grep utilities
include grep, egrep and fgrep.

GNU grep is needed by many scripts, so it shall be installed on every
system.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
./configure --prefix=/usr     \
            --host=%{lfs_tgt} \
            --build=$(./build-aux/config.guess)

%else 
sed -i "s/echo/#echo/" src/egrep.sh
./configure --prefix=/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
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
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/grep.mo

%else 
/usr/bin/egrep
/usr/bin/fgrep
/usr/bin/grep
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/man/man1/*

%endif
