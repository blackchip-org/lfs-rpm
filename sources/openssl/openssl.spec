# lfs

%global name            openssl
%global version         3.5.2
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Utilities from the general purpose cryptography library with TLS implementation
License:        OpenSSL and ASL 2.0

Source0:        https://www.openssl.org/source/openssl-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-doc  = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared libraries
which provide various cryptographic algorithms and protocols.

%if !%{with lfs}
%description devel
Development files for %{name}

%description doc
Documentation for %{name}

%description man
Manual pages for %{name}

%endif
#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./config --prefix=/usr         \
         --openssldir=/etc/ssl \
         --libdir=lib          \
         shared                \
         zlib-dynamic
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile
make %{?_smp_mflags} DESTDIR=%{buildroot} MANSUFFIX=ssl install

mv -v %{buildroot}/usr/share/doc/openssl \
      %{buildroot}/usr/share/doc/openssl-%{version}
cp -vfr doc/* %{buildroot}/usr/share/doc/openssl-%{version}
# FIXME: For now, we are going to remove tsget as this adds a dependency to
# perl(WWW::Curl::Easy)
rm %{buildroot}/etc/ssl/misc/tsget*

#---------------------------------------------------------------------------
%check
make test

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/etc/ssl
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/include/openssl
%{?lfs_dir}/usr/lib/engines-3
%{?lfs_dir}/usr/lib/lib*.so*
%{?lfs_dir}/usr/lib/cmake/OpenSSL
%{?lfs_dir}/usr/lib/ossl-modules
%{?lfs_dir}/usr/lib/pkgconfig/*

%else
%config(noreplace) /etc/ssl/ct_log_list.cnf
/etc/ssl/ct_log_list.cnf.dist
/etc/ssl/misc/CA.pl
#/etc/ssl/misc/tsget
#/etc/ssl/misc/tsget.pl
%config(noreplace)/etc/ssl/openssl.cnf
/etc/ssl/openssl.cnf.dist
/usr/bin/c_rehash
/usr/bin/openssl
/usr/lib/engines-3/afalg.so
/usr/lib/engines-3/capi.so
/usr/lib/engines-3/loader_attic.so
/usr/lib/engines-3/padlock.so
/usr/lib/libcrypto.so.*
/usr/lib/libssl.*
/usr/lib/ossl-modules/legacy.so

%files devel
/usr/include/openssl
/usr/lib/libcrypto.so
/usr/lib/libssl.so
/usr/lib/cmake/OpenSSL
/usr/lib/pkgconfig/libcrypto.pc
/usr/lib/pkgconfig/libssl.pc
/usr/lib/pkgconfig/openssl.pc

%files doc
/usr/share/doc/openssl-%{version}

%files man
/usr/share/man/man*/*.gz

%endif