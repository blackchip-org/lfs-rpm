%define version2    5.38
%define version     %{version2}.0

Name:           lfs-perl
Version:        %{version}
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        https://www.cpan.org/src/5.0/perl-%{version}.tar.xz


%description
Toolchain for building LFS


%prep
%setup -q -n perl-%{version}


%build
sh Configure -des                                               \
             -Dprefix=/usr                                      \
             -Dvendorprefix=/usr                                \
             -Duseshrplib                                       \
             -Dprivlib=/usr/lib/perl5/%{version2}/core_perl     \
             -Darchlib=/usr/lib/perl5/%{version2}/core_perl     \
             -Dsitelib=/usr/lib/perl5/%{version2}/site_perl     \
             -Dsitearch=/usr/lib/perl5/%{version2}/site_perl    \
             -Dvendorlib=/usr/lib/perl5/%{version2}/vendor_perl \
             -Dvendorarch=/usr/lib/perl5/%{version2}/vendor_perl \
             -Dman1dir=/usr/share/man/man1 \
             -Dman3dir=/usr/share/man/man3
make


%install
make DESTDIR=%{buildroot} install
%remove_docs


%files
/usr/bin/*
/usr/lib/perl5/%{version2}


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
