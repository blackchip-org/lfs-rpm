# lfs

%global name            m4
%global version         1.4.20
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        GNU macro processor
License:        GPLv3+

Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
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
A GNU implementation of the traditional UNIX macro processor. M4 is useful for
writing text files which can be logically parsed, and is used by many programs
as part of their build process. M4 has built-in functions for including files,
running shell commands, doing arithmetic, etc. The autoconf program needs m4
for generating configure scripts, but not for running configure scripts.

Install m4 if you need a macro processor.

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
./configure --prefix=/usr

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/m4

%else
/usr/bin/m4

%files info
/usr/share/info/*.gz

%files lang
/usr/share/locale/*/LC_MESSAGES/%{name}.mo

%files man
/usr/share/man/man*/*.gz

%endif
