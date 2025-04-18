Name:           less
Version:        668
Release:        1%{?dist}
Summary:        A text file browser similar to more, but better
License:        GPLv3+ or BSD

Source:         https://www.greenwoodsoftware.com/less/less-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
The less utility is a text file browser that resembles more, but has more
capabilities. Less allows you to move backwards in the file as well as
forwards. Since less doesn't have to read the entire input file before it
starts, less starts up more quickly than text editors (for example, vi).

You should install less because it is a basic utility for viewing text files,
and you'll use it frequently.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr --sysconfdir=/etc
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey

%files doc
/usr/share/man/man1/*