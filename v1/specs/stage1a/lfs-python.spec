%define version2    3.11
%define version     %{version2}.4

Name:           lfs-python
Version:        %{version}
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://www.python.org/ftp/python/3.11.4/Python-%{version}.tar.xz


%description
Toolchain for building LFS


%prep
%setup -q -n Python-%{version}


%build
./configure --prefix=/usr   \
            --enable-shared \
            --without-ensurepip
make


%install
make DESTDIR=%{buildroot} install
%remove_docs


%files
/usr/bin/*
/usr/include/python%{version2}
/usr/lib/*.so*
/usr/lib/pkgconfig/*
/usr/lib/python%{version2}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
