# lfs

%global name            linux-headers
%global source_name     linux
%global version         6.16.1
%global version_1       6
%global release         1

#---------------------------------------------------------------------------
Name:       %{name}
Version:    %{version}
Release:    %{release}%{?dist}
Summary:    The Linux kernel API
License:    GPLv2 and Redistributable, no modification permitted

Source:     https://www.kernel.org/pub/linux/kernel/v%{version_1}.x/linux-%{version}.tar.xz
Source1:    %{name}.sha256

%description
The C header fils that specify the interface between the Linux kernel and
userspace libraries and programs. The header files define structures and
constants that are needed for building most standard programs and are also
needed for rebuilding the glibc package.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{source_name}-%{version}

#---------------------------------------------------------------------------
%build
make %{?_smp_mflags} mrproper
make %{?_smp_mflags} headers
find usr/include -type f ! -name '*.h' -delete

#---------------------------------------------------------------------------
%install
mkdir -p %{buildroot}/%{?lfs_dir}/usr
cp -rv usr/include %{buildroot}/%{?lfs_dir}/usr

#---------------------------------------------------------------------------
%files
%{?lfs_dir}/usr/include/*

