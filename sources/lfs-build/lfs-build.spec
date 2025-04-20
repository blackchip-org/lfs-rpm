# lfs-rpm

%global name        lfs-build
%global version     1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Linux from Scratch build configurations
License:        MIT

Source0:        brp-lfs-build
Source1:        macros.lfs

%description
Configuration files for a LFS build.

#---------------------------------------------------------------------------
%prep
cp %{SOURCE0} %{SOURCE1} .

#---------------------------------------------------------------------------
%install
install -D -m 644 macros.lfs    %{buildroot}/etc/rpm/macros.lfs
install -D -m 755 brp-lfs-build %{buildroot}/usr/lib/rpm/brp-lfs-build

#---------------------------------------------------------------------------
%files
/etc/rpm/macros.lfs
/usr/lib/rpm/brp-lfs-build


