%define version     7.0.3

Name:           lfs-texinfo
Version:        %{version}
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://ftp.gnu.org/gnu/texinfo/texinfo-%{version}.tar.xz


%description
Toolchain for building LFS


%prep
%setup -q -n texinfo-%{version}


%build
./configure --prefix=/usr
make


%install
make DESTDIR=%{buildroot} install
%remove_docs


%files
/usr/bin/*
/usr/lib/*
/usr/share/locale/*/LC_MESSAGES/*.mo
/usr/share/texinfo/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
