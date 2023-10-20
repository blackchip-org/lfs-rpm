Name:           linux
Version:        6.4.12
Release:        1%{?dist}
Summary:        The Linux kernel
License:        GPLv2 and Redistributable, no modification permitted

Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

%description
The kernel package contains the Linux kernel (vmlinuz), the core of any Linux
operating system. The kernel handles the basic functions of the operating
system: memory allocation, process allocation, device input and output, etc.

#---------------------------------------------------------------------------
%prep
%setup -q 

#---------------------------------------------------------------------------
%build
%lfs_build_begin 

%make mrproper

%if %{with lfs_stage1b}
%make headers
find usr/include -type f ! -name '*.h' -delete

%endif
%lfs_build_end 

#---------------------------------------------------------------------------
%install
%lfs_build_begin 

%if %{with lfs_stage1b}
mkdir -p %{buildroot}/%{lfs_dir}/usr
cp -rv usr/include %{buildroot}/%{lfs_dir}/usr

%endif 
%lfs_build_end 

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1b}
%{lfs_dir}/usr/include/*

%endif 
