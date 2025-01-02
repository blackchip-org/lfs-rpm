Name:           cpio
Version:        2.15
Release:        1%{?dist}
Summary:        Copies files into or out of a cpio or tar archive
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/cpio/cpio-%{version}.tar.gz

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
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
# Both the tar package and this package have a rmt command. For now, take
# the one found in tar
rm %{buildroot}/usr/libexec/rmt
%remove_info_dir

#---------------------------------------------------------------------------
%post
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/bin/cpio

%files lang
/usr/share/locale/*/LC_MESSAGES/%{name}.mo

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*
