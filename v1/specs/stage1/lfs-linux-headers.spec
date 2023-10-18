Name:           lfs-linux-headers
Version:        6.4.12
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL2

Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n linux-%{version}


%build
make mrproper
make headers
find usr/include -type f ! -name '*.h' -delete


%install
mkdir -p %{buildroot}/%{lfs}/usr
cp -rv usr/include %{buildroot}/%{lfs}/usr


%files
%{lfs}/usr/include/*


%changelog
* Tue Oct 3 2023 Mike McGann <mike.mcgann@blackchip.org> - 6.4.12-1
- Initial package

