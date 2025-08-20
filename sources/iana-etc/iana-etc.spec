# lfs

%global name            iana-etc
%global version         20250807
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Data for network services and protocols
License:        MIT

Source0:        https://github.com/Mic92/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

BuildArch:      noarch

%description
The Iana-Etc package provides data for network services and protocols.

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q -n %{name}-%{version}

#---------------------------------------------------------------------------
%install
install services    -D %{buildroot}/etc/services
install protocols   -D %{buildroot}/etc/protocols

#---------------------------------------------------------------------------
%files
/etc/{services,protocols}