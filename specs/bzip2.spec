Name:           bzip2
Version:        1.0.8
Release:        1%{?dist}
Summary:        A file compression utility
License:        BSD

Source0:        https://www.sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz

%if %{without lfs_bootstrap}
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/bzip2-%{version}-install_docs-1.patch
%endif

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

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
%make -f Makefile-libbz2_so
%make clean
%make CC=%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc \
     AR=%{lfs_tools_dir}/bin/%{lfs_tgt}-ar \
     RANLIB=%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
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

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_bootstrap}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*

%endif


