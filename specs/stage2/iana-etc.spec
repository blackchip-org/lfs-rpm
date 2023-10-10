%define version     20230810

Name:           iana-etc
Version:        %{version}
Release:        1%{?dist}
Summary:        Data for network services and protocols
License:        MIT

Source0:        https://github.com/Mic92/iana-etc/releases/download/%{version}/iana-etc-%{version}.tar.gz


%description
The Iana-Etc package provides data for network services and protocols.


%global _build_id_links none


%prep
%setup -q -n iana-etc-%{version}


%build


%install
install services    -D %{buildroot}/etc/services
install protocols   -D %{buildroot}/etc/protocols


%files
/etc/{services,protocols}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
