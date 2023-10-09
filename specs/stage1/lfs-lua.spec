Name:           lfs-lua
Version:        5.4.6
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        n/a

Source0:        http://www.lua.org/ftp/lua-%{version}.tar.gz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n lua-%{version}


%build
%lfs_path 
make INSTALL_TOP=/usr \
     CC="%{lfs_tools}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools}/bin/%{lfs_tgt}-ar rcu" \
     RANLIB="%{lfs_tools}/bin/%{lfs_tgt}-ranlib" \
     "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -fPIC"


%install
%lfs_path 
make INSTALL_BIN=%{buildroot}/%{lfs}/usr/bin \
     INSTALL_LIB=%{buildroot}/%{lfs}/usr/lib \
     INSTALL_INC=%{buildroot}/%{lfs}/usr/include \
     INSTALL_MAN=%{buildroot}/%{lfs}/usr/share/man \
     INSTALL_LMOD=%{buildroot}/%{lfs}/usr/share/lua/5.4 \
     INSTALL_CMOD=%{buildroot}/%{lfs}/usr/lib/lua/5.4 \
     install
rm %{buildroot}/%{lfs}/usr/bin/* 
%lfs_remove_docs


%files
%{lfs}/usr/include/* 
%{lfs}/usr/lib/* 


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package
