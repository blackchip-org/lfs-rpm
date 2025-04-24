# lfs

%global name        less
%global version     668
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A text file browser similar to more, but better
License:        GPLv3+ or BSD

Source0:        https://www.greenwoodsoftware.com/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%endif

%description
The less utility is a text file browser that resembles more, but has more
capabilities. Less allows you to move backwards in the file as well as
forwards. Since less doesn't have to read the entire input file before it
starts, less starts up more quickly than text editors (for example, vi).

You should install less because it is a basic utility for viewing text files,
and you'll use it frequently.

%if !%{with lfs}
%description doc
Documentation for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr --sysconfdir=/etc
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/bin

%else
/usr/bin/less
/usr/bin/lessecho
/usr/bin/lesskey

%files doc
/usr/share/man/man1/*

%endif