Name:           openssl
Version:        3.2.1
Release:        1%{?dist}
Summary:        Utilities from the general purpose cryptography library with TLS implementation
License:        OpenSSL and ASL 2.0

Source:         https://www.openssl.org/source/openssl-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared libraries
which provide various cryptographic algorithms and protocols.

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./config --prefix=/usr         \
         --openssldir=/etc/ssl \
         --libdir=lib          \
         shared                \
         zlib-dynamic
%make

#---------------------------------------------------------------------------
%install
sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile
%make DESTDIR=%{buildroot} MANSUFFIX=ssl install
mv -v %{buildroot}/usr/share/doc/openssl \
      %{buildroot}/usr/share/doc/openssl-%{version}
cp -vfr doc/* %{buildroot}/usr/share/doc/openssl-%{version}

# FIXME: For now, we are going to remove tsget as this adds a dependency to
# perl(WWW::Curl::Easy)
rm %{buildroot}/etc/ssl/misc/tsget*

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
%files
%config(noreplace) /etc/ssl/ct_log_list.cnf
/etc/ssl/ct_log_list.cnf.dist
/etc/ssl/misc/CA.pl
#/etc/ssl/misc/tsget
#/etc/ssl/misc/tsget.pl
%config(noreplace)/etc/ssl/openssl.cnf
/etc/ssl/openssl.cnf.dist
/usr/bin/c_rehash
/usr/bin/openssl
/usr/include/openssl
/usr/lib/engines-3/afalg.so
/usr/lib/engines-3/capi.so
/usr/lib/engines-3/loader_attic.so
/usr/lib/engines-3/padlock.so
/usr/lib/libcrypto.so
%shlib /usr/lib/libcrypto.so.3
/usr/lib/libssl.so
%shlib /usr/lib/libssl.so.3
%shlib /usr/lib/ossl-modules/legacy.so
/usr/lib/pkgconfig/libcrypto.pc
/usr/lib/pkgconfig/libssl.pc
/usr/lib/pkgconfig/openssl.pc

%files doc
/usr/share/doc/openssl-%{version}

%files man
/usr/share/man/man*/*
