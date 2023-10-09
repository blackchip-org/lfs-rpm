%define version     3.8.2

Name:           lfs-bison
Version:        %{version}
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n bash-%{version}


%build


%install


%files


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package


