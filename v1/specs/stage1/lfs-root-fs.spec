Name:           lfs-root-fs
Version:        1.0.0
Release:        1%{?dist}
Summary:        Root filesystem 
License:        MIT

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Root filesystem.



%install
mkdir %{buildroot}/%{lfs}
ln -s /usr/bin %{buildroot}/%{lfs}/bin 
ln -s /usr/sbin %{buildroot}/%{lfs}/sbin 
ln -s /usr/lib %{buildroot}/%{lfs}/lib 

mkdir -pv %{buildroot}/%{lfs}/{boot,home,mnt,opt,srv}

mkdir -pv %{buildroot}/%{lfs}/etc/{opt,sysconfig}
mkdir -pv %{buildroot}/%{lfs}/usr/lib/firmware
mkdir -pv %{buildroot}/%{lfs}/media/{floppy,cdrom}
mkdir -pv %{buildroot}/%{lfs}/usr/{,local/}{include,src}
mkdir -pv %{buildroot}/%{lfs}/usr/local/{bin,lib,sbin}
mkdir -pv %{buildroot}/%{lfs}/usr/{,local/}share/{color,dict,doc,info,locale,man}
mkdir -pv %{buildroot}/%{lfs}/usr/{,local/}share/{misc,terminfo,zoneinfo}
mkdir -pv %{buildroot}/%{lfs}/usr/{,local/}share/man/man{1..8}
mkdir -pv %{buildroot}/%{lfs}/var/{cache,local,log,mail,opt,spool}
mkdir -pv %{buildroot}/%{lfs}/var/lib/{color,misc,locate}

ln -sfv /run %{buildroot}/%{lfs}/var/run
ln -sfv /run/lock %{buildroot}/%{lfs}/var/lock

install -dv -m 0750 %{buildroot}/%{lfs}/root
install -dv -m 1777 %{buildroot}/%{lfs}/tmp %{buildroot}/%{lfs}/var/tmp


%files
%{lfs}/{bin,lib,sbin}
%{lfs}/{boot,home,mnt,opt,srv}
%{lfs}/usr/lib/firmware
%{lfs}/media/{floppy,cdrom}
%{lfs}/usr/{include,src}
%{lfs}/usr/local/{include,src}
%{lfs}/usr/local/{bin,lib,sbin}
%{lfs}/usr/share/{color,dict,doc,info,locale,man}
%{lfs}/usr/share/{misc,terminfo,zoneinfo}
%{lfs}/usr/local/share/{color,dict,doc,info,locale,man}
%{lfs}/usr/local/share/{misc,terminfo,zoneinfo}
%{lfs}/var/{cache,local,log,mail,opt,spool}
%{lfs}/var/lib/{color,misc,locate}
%{lfs}/var/run 
%{lfs}/var/lock 
%{lfs}/root 
%{lfs}/tmp 
%{lfs}/var/tmp 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.4.4-1
- Initial package