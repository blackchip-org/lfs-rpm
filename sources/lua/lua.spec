# rpm

%global name        lua
%global lua_version 5.4
%global version     %{lua_version}.7
%global release     1

#---------------------------------------------------------------------------
Name:          %{name}
Version:       %{version}
Release:       %{release}%{?dist}
Summary:       Powerful light-weight programming language
License:       MIT

Source0:       http://www.lua.org/ftp/%{name}-%{version}.tar.gz
Source1:       %{name}.sha256

BuildRequires: readline
Suggests:      %{name}-doc = %{version}

%description
Lua is a powerful light-weight programming language designed for extending
applications. Lua is also frequently used as a general-purpose, stand-alone
language. Lua is free software. Lua combines simple procedural syntax with
powerful data description constructs based on associative arrays and extensible
semantics. Lua is dynamically typed, interpreted from bytecodes, and has
automatic memory management with garbage collection, making it ideal for
configuration, scripting, and rapid prototyping.

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
make %{?_smp_mflags} \
     INSTALL_TOP=/usr \
     CC="%{lfs_tools_dir}/bin/%{lfs_tgt}-gcc" \
     AR="%{lfs_tools_dir}/bin/%{lfs_tgt}-ar rcu" \
     RANLIB="%{lfs_tools_dir}/bin/%{lfs_tgt}-ranlib" \
     "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -fPIC"

%else
sed -i 's|/usr/local|/usr|g' src/luaconf.h
make %{?_smp_mflags} \
     INSTALL_TOP=/usr \
     "CFLAGS=-O2 -Wall -Wextra -DLUA_COMPAT_5_3 -DLUA_USE_LINUX -DLUA_USE_READLINE -fPIC" \
     "LDFLAGS=-Wl,-E -ldl -lreadline"
%endif

#---------------------------------------------------------------------------
%install
make \
     INSTALL_BIN=%{buildroot}/%{?lfs_dir}/usr/bin \
     INSTALL_LIB=%{buildroot}/%{?lfs_dir}/usr/lib \
     INSTALL_INC=%{buildroot}/%{?lfs_dir}/usr/include \
     INSTALL_MAN=%{buildroot}/%{?lfs_dir}/usr/share/man/man1 \
     INSTALL_LMOD=%{buildroot}/%?{lfs_dir}/usr/share/lua/%{lua_version} \
     INSTALL_CMOD=%{buildroot}/%{?lfs_dir}/usr/lib/lua/%{lua_version} \
     install

mkdir -p %{buildroot}/%{?lfs_dir}/usr/lib/rpm/macros.d
cat <<EOF | sed 's/@/%/' > %{buildroot}/%{?lfs_dir}/usr/lib/rpm/macros.d/macros.lua
@lua_version %{lua_version}
EOF

#---------------------------------------------------------------------------
%files

%if %{with lfs}
%{?lfs_dir}/usr/bin
%{?lfs_dir}/usr/include/*
%{?lfs_dir}/usr/lib/*

%else
/usr/bin/lua
/usr/bin/luac
/usr/include/*.{h,hpp}
/usr/lib/liblua.a
/usr/lib/rpm/macros.d/macros.lua

%files doc
/usr/share/man/*

%endif

