Name:           openssl
Version:        3.1.2
Release:        1%{?dist}
Summary:        Utilities from the general purpose cryptography library with TLS implementation
License:        OpenSSL and ASL 2.0

Source0:        https://www.openssl.org/source/openssl-%{version}.tar.gz

%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared libraries
which provide various cryptographic algorithms and protocols.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

./config --prefix=/usr         \
         --openssldir=/etc/ssl \
         --libdir=lib          \
         shared                \
         zlib-dynamic
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

sed -i '/INSTALL_LIBS/s/libcrypto.a libssl.a//' Makefile
%make DESTDIR=%{buildroot} MANSUFFIX=ssl install
mv -v %{buildroot}/usr/share/doc/openssl \
      %{buildroot}/usr/share/doc/openssl-%{version}
cp -vfr doc/* %{buildroot}/usr/share/doc/openssl-%{version}
%lfs_install_end

#---------------------------------------------------------------------------
%check
%make test

#---------------------------------------------------------------------------
%files
%config(noreplace) /etc/ssl/ct_log_list.cnf
/etc/ssl/ct_log_list.cnf.dist
/etc/ssl/misc/CA.pl
/etc/ssl/misc/tsget
/etc/ssl/misc/tsget.pl
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
/usr/lib/libssl.so
/usr/lib/ossl-modules/legacy.so
/usr/lib/pkgconfig/libcrypto.pc
/usr/lib/pkgconfig/libssl.pc
/usr/lib/pkgconfig/openssl.pc
/usr/share/doc/openssl-%{version}
/usr/share/man/man{1,3,5,7}/*

%defattr(755,root,root,755)
/usr/lib/libcrypto.so.3
/usr/lib/libssl.so.3
