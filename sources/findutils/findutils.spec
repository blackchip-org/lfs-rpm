# lfs

%global name            findutils
%global version         4.10.0
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        The GNU versions of find utilities (find and xargs)
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
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
The findutils package contains programs which will help you locate files on
your system. The find utility searches through a hierarchy of directories
looking for files which match a certain set of criteria (such as a file name
pattern). The xargs utility builds and executes command lines from standard
input arguments (usually lists of file names generated by the find command).

You should install findutils because it includes tools that are very useful for
finding things on your system.

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
./configure --prefix=/usr                   \
            --localstatedir=/var/lib/locate \
            --host=%{lfs_tgt}               \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr --localstatedir=/var/lib/locate

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
/usr/bin/find
/usr/bin/locate
/usr/bin/updatedb
/usr/bin/xargs
/usr/libexec/frcode

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files man
/usr/share/man/man*/*.gz

%endif


