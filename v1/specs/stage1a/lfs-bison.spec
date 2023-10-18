%define version     3.8.2

Name:           lfs-bison
Version:        %{version}
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://ftp.gnu.org/gnu/bison/bison-%{version}.tar.xz


%description
Toolchain for building LFS


%prep
%setup -q -n bison-%{version}


%build
./configure --prefix=/usr \
            --docdir=/usr/share/doc/bison-3.8.2
make


%install
make DESTDIR=%{buildroot} install
%remove_docs


%files
/usr/bin/*
/usr/lib/*
/usr/share/aclocal/*
/usr/share/bison
/usr/share/locale/*/LC_MESSAGES/*.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package


