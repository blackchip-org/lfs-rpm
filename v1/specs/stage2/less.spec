%global version         643
%global _build_id_links none

Name:           less
Version:        %{version}
Release:        1%{?dist}
Summary:        A text file browser similar to more, but better
License:        GPLv3+ or BSD

Source0:        https://www.greenwoodsoftware.com/less/less-%{version}.tar.gz

%description
The less utility is a text file browser that resembles more, but has more
capabilities. Less allows you to move backwards in the file as well as
forwards. Since less doesn't have to read the entire input file before it
starts, less starts up more quickly than text editors (for example, vi).

You should install less because it is a basic utility for viewing text files,
and you'll use it frequently.


%prep
%setup -q


%build
./configure --prefix=/usr --sysconfdir=/etc
make


%check
make check


%install
make DESTDIR=%{buildroot} install


%files
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey
/usr/share/man/man1/*
