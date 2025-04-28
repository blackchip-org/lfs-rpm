# lfs

%global name            bzip2
%global version         1.0.8
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A file compression utility
License:        BSD

Source0:        https://www.sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/bzip2-%{version}-install_docs-1.patch

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

%description
Bzip2 is a freely available, patent-free, high quality data compressor. Bzip2
compresses files to within 10 to 15 percent of the capabilities of the best
techniques available. However, bzip2 has the added benefit of being
approximately two times faster at compression and six times faster at
decompression than those techniques. Bzip2 is not the fastest compression
utility, but it does strike a balance between speed and compression capability.

Install bzip2 if you need a compression utility.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

%if !%{with lfs_stage1}
%patch 0 -p1
%endif

#---------------------------------------------------------------------------
%build
sed     -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile

%if %{with lfs_stage1}
make %{?_smp_mflags} -f Makefile-libbz2_so
make clean
make %{?_smp_mflags} \
    CC=%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc \
    AR=%{lfs_tools_dir}/bin/%{lfs_tgt}-ar \
    RANLIB=%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib

%else
sed     -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
make    %{?_smp_mflags} -f Makefile-libbz2_so
make    clean
make    %{?_smp_mflags}

%endif

#---------------------------------------------------------------------------
%install
mkdir   -p %{buildroot}/%{?lfs_dir}/usr/{bin,lib,share}
make    PREFIX=%{buildroot}/%{?lfs_dir}/usr install

cp -av libbz2.so.*      %{buildroot}/%{?lfs_dir}/usr/lib
ln -sv libbz2.so.1.0.8  %{buildroot}/%{?lfs_dir}/usr/lib/libbz2.so
cp -v bzip2-shared      %{buildroot}/%{?lfs_dir}/usr/bin/bzip2

for i in /usr/bin/{bzcat,bunzip2,bzcmp,bzegrep,bzfgrep,bzless}; do
    ln -sfv bzip2 %{buildroot}/%{?lfs_dir}/$i
done

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*

%else
/usr/bin/bunzip2
/usr/bin/bzcat
/usr/bin/bzcmp
/usr/bin/bzdiff
/usr/bin/bzegrep
/usr/bin/bzfgrep
/usr/bin/bzgrep
/usr/bin/bzip2
/usr/bin/bzip2recover
/usr/bin/bzless
/usr/bin/bzmore
/usr/lib/libbz2.so.*

%files devel
/usr/include/bzlib.h
/usr/lib/libbz2.so

%files doc
/usr/share/doc/%{name}-%{version}

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libbz2.a

%endif


