Name:           lfs-bzip2
Version:        1.0.8 
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://www.sourceware.org/pub/bzip2/bzip2-%{version}.tar.gz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n bzip2-%{version}


%build
%lfs_path
make -f Makefile-libbz2_so
make clean
make CC=%{lfs_tools}/bin/%{lfs_tgt}-gcc \
     AR=%{lfs_tools}/bin/%{lfs_tgt}-ar \
     RANLIB=%{lfs_tools}/bin/%{lfs_tgt}-ranlib


%install
%lfs_path
mkdir -p %{buildroot}/%{lfs}/usr/{bin,lib}

make PREFIX=%{buildroot}/%{lfs}/usr install
mkdir -p %{buildroot}/%{lfs}/usr/{bin,lib}
cp -av libbz2.so.* %{buildroot}/%{lfs}/usr/lib
ln -sv libbz2.so.1.0.8 %{buildroot}/%{lfs}/usr/lib/libbz2.so
cp -v bzip2-shared %{buildroot}/%{lfs}/usr/bin/bzip2
for i in /usr/bin/{bzcat,bunzip2,bzcmp,bzegrep,bzfgrep,bzless}; do
    ln -sfv bzip2 %{buildroot}/%{lfs}/$i
done
rm -rf %{buildroot}/lfs/usr/man


%files
%{lfs}/usr/bin/* 
%{lfs}/usr/include/*
%{lfs}/usr/lib/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.4.4-1
- Initial package


