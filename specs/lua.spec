Name:           lua
Version:        5.4.7
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
%if %{with lfs_stage1}
%use_lfs_tools
%make INSTALL_TOP=/usr \
     CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar rcu" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -fPIC"

%else
%make INSTALL_TOP=/usr "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -fPIC"

%endif

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make INSTALL_BIN=%{buildroot}/%{lfs_dir}/usr/bin \
     INSTALL_LIB=%{buildroot}/%{lfs_dir}/usr/lib \
     INSTALL_INC=%{buildroot}/%{lfs_dir}/usr/include \
     INSTALL_MAN=%{buildroot}/%{lfs_dir}/usr/share/man/man1 \
     INSTALL_LMOD=%{buildroot}/%{lfs_dir}/usr/share/lua/5.4 \
     INSTALL_CMOD=%{buildroot}/%{lfs_dir}/usr/lib/lua/5.4 \
     install
rm %{buildroot}/%{lfs_dir}/usr/bin/*
%discard_docs

%else
%make INSTALL_BIN=%{buildroot}/usr/bin \
     INSTALL_LIB=%{buildroot}/usr/lib \
     INSTALL_INC=%{buildroot}/usr/include \
     INSTALL_MAN=%{buildroot}/usr/share/man \
     INSTALL_LMOD=%{buildroot}/usr/share/lua/5.4 \
     INSTALL_CMOD=%{buildroot}/usr/lib/lua/5.4 \
     install

%endif

#---------------------------------------------------------------------------
%files

%if %{with lfs_stage1}
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/lib/*

%else
/usr/bin/lua
/usr/bin/luac
/usr/include/*.{h,hpp}
/usr/lib/liblua.a
/usr/share/man/*

%endif

