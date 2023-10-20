Name:           lua
Version:        5.4.6
Release:        1%{?dist}
Summary:        Powerful light-weight programming language
License:        MIT

Source0:        http://www.lua.org/ftp/lua-%{version}.tar.gz

%description
Lua is a powerful light-weight programming language designed for extending
applications. Lua is also frequently used as a general-purpose, stand-alone
language. Lua is free software. Lua combines simple procedural syntax with
powerful data description constructs based on associative arrays and extensible
semantics. Lua is dynamically typed, interpreted from bytecodes, and has
automatic memory management with garbage collection, making it ideal for
configuration, scripting, and rapid prototyping.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_bootstrap}
%make INSTALL_TOP=/usr \
     CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar rcu" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -fPIC"

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_bootstrap}
%make INSTALL_BIN=%{buildroot}/%{lfs_dir}/usr/bin \
     INSTALL_LIB=%{buildroot}/%{lfs_dir}/usr/lib \
     INSTALL_INC=%{buildroot}/%{lfs_dir}/usr/include \
     INSTALL_MAN=%{buildroot}/%{lfs_dir}/usr/share/man \
     INSTALL_LMOD=%{buildroot}/%{lfs_dir}/usr/share/lua/5.4 \
     INSTALL_CMOD=%{buildroot}/%{lfs_dir}/usr/lib/lua/5.4 \
     install
rm %{buildroot}/%{lfs_dir}/usr/bin/*

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files

%if %{with lfs_bootstrap}
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*

%endif

