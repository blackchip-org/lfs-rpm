Name:           bzip2
Version:        1.0.8
Release:        1%{?dist}
Summary:        A file compression utility
License:        BSD

Source0:        https://www.sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/bzip2-%{version}-install_docs-1.patch

%description
Bzip2 is a freely available, patent-free, high quality data compressor. Bzip2
compresses files to within 10 to 15 percent of the capabilities of the best
techniques available. However, bzip2 has the added benefit of being
approximately two times faster at compression and six times faster at
decompression than those techniques. Bzip2 is not the fastest compression
utility, but it does strike a balance between speed and compression capability.

Install bzip2 if you need a compression utility.

#---------------------------------------------------------------------------
%prep
%setup -q

%if %{without lfs_stage1}
%patch 0 -p1 
%endif 

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
%make -f Makefile-libbz2_so
%make clean
%make CC=%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc \
     AR=%{lfs_tools_dir}/bin/%{lfs_tgt}-ar \
     RANLIB=%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib

%else 
sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile
sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile
%make -f Makefile-libbz2_so
%make clean
%make

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
mkdir -p %{buildroot}/%{lfs_dir}/usr/{bin,lib}
%make PREFIX=%{buildroot}/%{lfs_dir}/usr install
mkdir -p %{buildroot}/%{lfs_dir}/usr/{bin,lib}
cp -av libbz2.so.* %{buildroot}/%{lfs_dir}/usr/lib
ln -sv libbz2.so.1.0.8 %{buildroot}/%{lfs_dir}/usr/lib/libbz2.so
cp -v bzip2-shared %{buildroot}/%{lfs_dir}/usr/bin/bzip2
for i in /usr/bin/{bzcat,bunzip2,bzcmp,bzegrep,bzfgrep,bzless}; do
    ln -sfv bzip2 %{buildroot}/%{lfs_dir}/$i
done
rm -rf %{buildroot}/lfs/usr/man

%else 
make PREFIX=%{buildroot}/usr install
cp -av libbz2.so.* %{buildroot}/usr/lib
ln -sv libbz2.so.%{version} %{buildroot}/usr/lib/libbz2.so
cp -v bzip2-shared %{buildroot}/usr/bin/bzip2
for i in /usr/bin/{bzcat,bunzip2}; do
  ln -sfv bzip2 %{buildroot}/$i
done
rm -f %{buildroot}/usr/lib/libbz2.a

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*

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
/usr/include/bzlib.h
/usr/lib/libbz2.so
/usr/lib/libbz2.so.1.0
/usr/share/doc/bzip2-%{version}
/usr/share/man/man1/*

%defattr(755,root,root,755) 
/usr/lib/libbz2.so.%{version}

%endif


