Name:           dejagnu
Version:        1.6.3
Release:        1%{?dist}
Summary:        A front end for testing other programs
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/dejagnu/dejagnu-%{version}.tar.gz

%description 
DejaGnu is an Expect/Tcl based framework for testing other programs. DejaGnu
has several purposes: to make it easy to write tests for any program; to allow
you to write tests which will be portable to any host or target where a program
must be tested; and to standardize the output format of all tests (making it
easier to integrate the testing into software development).

#---------------------------------------------------------------------------
%prep
%setup -q 

#---------------------------------------------------------------------------
%build
%lfs_build_begin

mkdir -v build
cd       build

../configure --prefix=/usr
%make 
makeinfo --html --no-split -o doc/dejagnu.html ../doc/dejagnu.texi
makeinfo --plaintext       -o doc/dejagnu.txt  ../doc/dejagnu.texi
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

cd build 
%make DESTDIR=%{buildroot} install
install -v -dm755  %{buildroot}/usr/share/doc/dejagnu-%{version}
install -v -m644   doc/dejagnu.{html,txt} %{buildroot}/usr/share/doc/dejagnu-%{version}
%lfs_install_end

#---------------------------------------------------------------------------
%check 
cd build 
make check

#---------------------------------------------------------------------------
%files
/usr/bin/dejagnu
/usr/bin/runtest
/usr/include/* 
/usr/share/%{name}
/usr/share/doc/%{name}-%{version}
/usr/share/info/* 
/usr/share/man/man1/* 
