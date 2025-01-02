Name:           iana-etc
Version:        20240806
Release:        1%{?dist}
Summary:        Data for network services and protocols
License:        MIT

Source0:        https://github.com/Mic92/iana-etc/releases/download/%{version}/iana-etc-%{version}.tar.gz

%description
The Iana-Etc package provides data for network services and protocols.

#---------------------------------------------------------------------------
%prep
%setup -q -n iana-etc-%{version}

#---------------------------------------------------------------------------
%install
install services    -D %{buildroot}/etc/services
install protocols   -D %{buildroot}/etc/protocols

#---------------------------------------------------------------------------
%files
/etc/{services,protocols}