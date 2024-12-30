Name:           neovim
Version:        0.10.3
Release:        1%{?dist}
Summary:        Hyperextensible Vim-based text editor
License:        ASL-2.0

Source:         https://github.com/neovim/neovim/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  libuv
BuildRequires:  libvterm
BuildRequires:  lua
BuildRequires:  lua-lpeg
BuildRequires:  luv
BuildRequires:  msgpack
Suggests:       %{name}-doc = %{version}

%description
Neovim is a project that seeks to aggressively refactor Vim in order to:

* Simplify maintenance and encourage contributions
* Split the work between multiple developers
* Enable advanced UIs without modifications to the core
* Maximize extensibility

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package doc
Summary:        Documentation for %{name}
Provides:       %{name}-man = %{version}

%description lang
Language files for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
mkdir build
cd build
cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DLPEG_LIBRARY=/usr/lib/lua/%{lua_version}/lpeg.so \
    ..

#---------------------------------------------------------------------------
%install
cd build
%make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%files
/usr/bin/nvim
#%shlib /usr/lib/nvim/parser/c.so
#%shlib /usr/lib/nvim/parser/lua.so
#%shlib /usr/lib/nvim/parser/markdown.so
#%shlib /usr/lib/nvim/parser/markdown_inline.so
#%shlib /usr/lib/nvim/parser/query.so
#%shlib /usr/lib/nvim/parser/vim.so
#%shlib /usr/lib/nvim/parser/vimdoc.so
/usr/share/applications/nvim.desktop
/usr/share/icons/hicolor/128x128/apps/nvim.png
/usr/share/nvim

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/man/man*/*
