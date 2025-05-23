# lfs

%global name        libxcrypt
%global version     4.4.36
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Extended crypt library for DES, MD5, Blowfish and others
License:        LGPLv2+ and BSD and Public Domain

Source0:        https://github.com/besser82/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}.sha256

BuildRequires:  pkg-config

%if !%{with lfs}
Recommends:     %{name}-man = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%endif

%description
libxcrypt is a modern library for one-way hashing of passwords. It supports
DES, MD5, SHA-2-256, SHA-2-512, and bcrypt-based password hashes, and provides
the traditional Unix 'crypt' and 'crypt_r' interfaces, as well as a set of
extended interfaces pioneered by Openwall Linux, 'crypt_rn', 'crypt_ra',
'crypt_gensalt', 'crypt_gensalt_rn', and 'crypt_gensalt_ra'.

libxcrypt is intended to be used by login(1), passwd(1), and other similar
programs; that is, to hash a small number of passwords during an interactive
authentication dialogue with a human. It is not suitable for use in bulk
password-cracking applications, or in any other situation where speed is more
important than careful handling of sensitive data. However, it *is* intended to
be fast and lightweight enough for use in servers that must field thousands of
login attempts per minute.

On Linux-based systems, by default libxcrypt will be binary backward compatible
with the libcrypt.so.1 shipped as part of the GNU C Library. This means that
all existing binary executables linked against glibc's libcrypt should work
unmodified with this library's libcrypt.so.1. We have taken pains to provide
exactly the same "symbol versions" as were used by glibc on various CPU
architectures, and to account for the variety of ways in which the Openwall
extensions were patched into glibc's libcrypt by some Linux distributions. (For
instance, compatibility symlinks for SuSE's "libowcrypt" are provided.)

However, the converse is not true: programs linked against libxcrypt will not
work with glibc's libcrypt. Also, programs that use certain legacy APIs
supplied by glibc's libcrypt ('encrypt', 'encrypt_r', 'setkey', 'setkey_r', and
'fcrypt') cannot be compiled against libxcrypt.

%if !%{with lfs}
%description devel
Development files for %{name}

%description man
Manual pages for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr                \
            --enable-hashes=strong,glibc \
            --enable-obsolete-api=no     \
            --disable-static             \
            --disable-failure-tokens
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make prefix=%{buildroot}/usr install

#---------------------------------------------------------------------------
%check
make test

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/*
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/lib/libcrypt.so.*

%files devel
/usr/include/*.h
/usr/lib/libcrypt.so
/usr/lib/pkgconfig/libcrypt.pc
/usr/lib/pkgconfig/libxcrypt.pc

%files man
/usr/share/man/man*/*.gz

%endif

