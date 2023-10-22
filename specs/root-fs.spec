Name:           root-fs
Version:        1.0.0
Release:        1%{?dist}
Summary:        Root filesystem
License:        MIT

%description
Directories and symbolic links for the root filesystem.

%global root %{?with_lfs_stage1:%{lfs_dir}}

#---------------------------------------------------------------------------
%install
mkdir -p %{buildroot}/%{root}
ln -s /usr/bin %{buildroot}/%{root}/bin
ln -s /usr/sbin %{buildroot}/%{root}/sbin
ln -s /usr/lib %{buildroot}/%{root}/lib

mkdir -pv %{buildroot}/%{root}/{boot,home,mnt,opt,srv}

mkdir -pv %{buildroot}/%{root}/etc/{opt,sysconfig}
mkdir -pv %{buildroot}/%{root}/usr/lib/firmware
mkdir -pv %{buildroot}/%{root}/media/{floppy,cdrom}
mkdir -pv %{buildroot}/%{root}/usr/{,local/}{include,src}
mkdir -pv %{buildroot}/%{root}/usr/local/{bin,lib,sbin}
mkdir -pv %{buildroot}/%{root}/usr/{,local/}share/{color,dict,doc,info,locale,man}
mkdir -pv %{buildroot}/%{root}/usr/{,local/}share/{misc,terminfo,zoneinfo}
mkdir -pv %{buildroot}/%{root}/usr/{,local/}share/man/man{1..8}
mkdir -pv %{buildroot}/%{root}/var/{cache,local,log,mail,opt,spool}
mkdir -pv %{buildroot}/%{root}/var/lib/{color,misc,locate}

ln -sfv /run %{buildroot}/%{root}/var/run
ln -sfv /run/lock %{buildroot}/%{root}/var/lock

install -dv -m 0750 %{buildroot}/%{root}/root
install -dv -m 1777 %{buildroot}/%{root}/tmp %{buildroot}/%{root}/var/tmp

#---------------------------------------------------------------------------
%files
%{root}/{bin,lib,sbin}
%{root}/{boot,home,mnt,opt,srv}
%{root}/usr/lib/firmware
%{root}/media/{floppy,cdrom}
%{root}/usr/{include,src}
%{root}/usr/local/{include,src}
%{root}/usr/local/{bin,lib,sbin}
%{root}/usr/share/{color,dict,doc,info,locale,man}
%{root}/usr/share/{misc,terminfo,zoneinfo}
%{root}/usr/local/share/{color,dict,doc,info,locale,man}
%{root}/usr/local/share/{misc,terminfo,zoneinfo}
%{root}/var/{cache,local,log,mail,opt,spool}
%{root}/var/lib/{color,misc,locate}
%{root}/var/run
%{root}/var/lock
%{root}/root
%{root}/tmp
%{root}/var/tmp