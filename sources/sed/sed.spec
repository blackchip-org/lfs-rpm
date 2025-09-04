# lfs

%global name            sed
%global version         4.9
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU stream text editor
License:        GPLv3+

Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  texinfo

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

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
The sed (Stream EDitor) editor is a stream or batch (non-interactive) editor.
Sed takes text as input, performs an operation or set of operations on the text
and outputs the modified text. The operations that sed performs (substitutions,
deletions, insertions, etc.) can be specified in a script file or from the
command line.

%if !%{with lfs}
%description doc
Documentation for %{name}

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
make %{?_smp_mflags}

%else
./configure --prefix=/usr
make %{?_smp_mflags}
make html

%endif

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

%if !%{with lfs}
make DESTDIR=%{buildroot} install
install -d -m755           %{buildroot}/usr/share/doc/sed-4.9
install -m644 doc/sed.html %{buildroot}/usr/share/doc/sed-4.9

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*

%else
/usr/bin/sed

%files lang
/usr/share/locale/*/LC_MESSAGES/*.mo

%files doc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*

%files man
/usr/share/man/man*/*.gz

%endif

