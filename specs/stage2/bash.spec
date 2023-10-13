%global version     5.2.15

Name:           bash
Version:        %{version}
Release:        1%{?dist}
Summary:        The GNU Bourne Again shell
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/bash/bash-%{version}.tar.gz

%global _build_id_links none

%description
The GNU Bourne Again shell (Bash) is a shell or command language interpreter
that is compatible with the Bourne shell (sh). Bash incorporates useful
features from the Korn shell (ksh) and the C shell (csh). Most sh scripts can
be run by bash without modifica


%prep 
%setup -q 


%build 
./configure --prefix=/usr             \
            --without-bash-malloc     \
            --with-installed-readline \
            --docdir=/usr/share/doc/bash-%{version}
make 


%check 
make tests 


%install 
make DESTDIR=%{buildroot} install 
rm -rf %{buildroot}/usr/share/info/dir 


%files 
/usr/bin/bash
/usr/bin/bashbug
/usr/include/bash/*
/usr/lib/bash 
/usr/lib/pkgconfig/bash.pc
/usr/share/doc/%{name}-%{version}
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/*
/usr/share/man/man1/*


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
