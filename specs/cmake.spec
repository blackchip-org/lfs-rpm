Name:           cmake
Version:        3.30.2
Release:        1%{?dist}
Summary:        Cross-platform make system
License:        BSD and MIT and zlib

Source:         https://github.com/Kitware/CMake/releases/download/v%{version}/cmake-%{version}.tar.gz

%global         version2    3.30
BuildRequires:  openssl

%description
CMake is used to control the software compilation process using simple platform
and compiler independent configuration files. CMake generates native makefiles
and workspaces that can be used in the compiler environment of your choice.
CMake is quite sophisticated: it is possible to support complex environments
requiring system configuration, preprocessor generation, code generation, and
template instantiation.

%package doc
Summary:        Documentation for %{name}

# TODO: Build documentation with Sphinx
# -DSPHINX_HTML=ON
# -DSPHINX_MAN=ON
# -DSPHINX_EXECUTABLE=/path/to/sphinx-build
# https://sphinx-doc.org

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./bootstrap \
    --verbose \
    --parallel=$(nproc) \
    -- \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_DOC_PREFIX=/usr/share/doc
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/usr/share
mv %{buildroot}/usr/doc %{buildroot}/usr/share

#---------------------------------------------------------------------------
%files
/usr/bin/{cmake,ccmake,ctest,cpack}
/usr/share/aclocal/cmake.m4
/usr/share/bash-completion/completions/{cmake,cpack,ctest}
/usr/share/cmake-%{version2}
/usr/share/emacs/site-lisp/cmake-mode.el
/usr/share/vim/vimfiles/{indent,syntax}/cmake.vim

%files doc
/usr/share/doc/cmake-%{version2}
