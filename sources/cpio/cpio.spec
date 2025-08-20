# dnf

%global name            cpio
%global version         2.15
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Copies files into or out of a cpio or tar archive
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256
Patch0:         0001-Fix-c23-conformity.patch

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
GNU cpio copies files into or out of a cpio or tar archive. The archive can be
another file on the disk, a magnetic tape, or a pipe.

GNU cpio supports the following archive formats: binary, old ASCII, new ASCII,
crc, HPUX binary, HPUX old ASCII, old tar, and POSIX.1 tar. The tar format is
provided for compatibility with the tar program. By default, cpio creates
binary format archives, for compatibility with older cpio programs. When
extracting from archives, cpio automatically recognizes which kind of archive
it is reading and can read archives created on machines with a different
byte-order.

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
%patch 0 -p1

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install
# Both the tar package and this package have a rmt command. For now, take
# the one found in tar
rm %{buildroot}/usr/libexec/rmt

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin/*

%else
/usr/bin/cpio

%files lang
/usr/share/locale/*/LC_MESSAGES/%{name}.mo

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%endif
