# lfs-rpm

%global name        rpm-config
%global version     1
%global release     2

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        RPM vendor configurations
License:        MIT

Source0:        brp-remove-info-index
Source1:        macros

BuildArch:      noarch

%description
RPM vendor configurations.

#---------------------------------------------------------------------------
%prep
cp %{SOURCE0} %{SOURCE1} .

#---------------------------------------------------------------------------
%install
install -D -m 644 macros \
        %{buildroot}/usr/lib/rpm/%{_vendor}/macros

install -D -m 755 brp-remove-info-index \
        %{buildroot}/usr/lib/rpm/%{_vendor}/brp-remove-info-index

#---------------------------------------------------------------------------
%files
/usr/lib/rpm/%{_vendor}/brp-remove-info-index
/usr/lib/rpm/%{_vendor}/macros



