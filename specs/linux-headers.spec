Name:       linux-headers
Version:    6.10.5
Release:    1%{?dist}
Summary:    The Linux kernel API
License:    GPLv2 and Redistributable, no modification permitted

Source:     https://www.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

%description
The C header fils that specify the interface between the Linux kernel and
userspace libraries and programs. The header files define structures and
constants that are needed for building most standard programs and are also
needed for rebuilding the glibc package.

#---------------------------------------------------------------------------
%prep
%setup -q -n linux-%{version}

#---------------------------------------------------------------------------
%build
%make mrproper
%make headers
find usr/include -type f ! -name '*.h' -delete

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
mkdir -p %{buildroot}/%{lfs_dir}/usr
cp -rv usr/include %{buildroot}/%{lfs_dir}/usr

%else
mkdir -p %{buildroot}/usr
cp -rv usr/include %{buildroot}/usr

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/include/*

%else
/usr/include/*

%endif
