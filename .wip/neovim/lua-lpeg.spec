Name:           lua-lpeg
Version:        1.1.0
Release:        1%{?dist}
Summary:        Pattern-matching library for Lua
License:        MIT

Source:         https://www.inf.puc-rio.br/~roberto/lpeg/lpeg-1.1.0.tar.gz

BuildRequires:  lua
Suggests:       %{name}-doc = %{version}

%description
LPeg is a pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs). This text is a reference manual for the library. For those
starting with LPeg, Mastering LPeg presents a good tutorial. For a more formal
treatment of LPeg, as well as some discussion about its implementation, see
A Text Pattern-Matching Tool based on Parsing Expression Grammars. You may
also be interested in my talk about LPeg given at the III Lua Workshop.

%package doc
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q -n lpeg-%{version}

#---------------------------------------------------------------------------
%build
%make linux

#---------------------------------------------------------------------------
%install
install -Dt %{buildroot}/usr/lib/lua/%{lua_version} \
    lpeg.so

install -Dt %{buildroot}/usr/share/lua/%{lua_version} \
    re.lua

install -Dt %{buildroot}/usr/share/doc/lua-lpeg \
    HISTORY \
    lpeg-128.gif \
    lpeg.html \
    re.html
asdfasd

#---------------------------------------------------------------------------
%files
%shlib /usr/lib/lua/%{lua_version}/lpeg.so
/usr/share/lua/%{lua_version}/re.lua

%files doc
/usr/share/doc/lua-lpeg/HISTORY
/usr/share/doc/lua-lpeg/lpeg-128.gif
/usr/share/doc/lua-lpeg/lpeg.html
/usr/share/doc/lua-lpeg/re.html