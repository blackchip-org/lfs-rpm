# rpm

%global name        cmake
%global version_2   3.31
%global version     %{version_2}.6
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Cross-platform make system
License:        BSD and MIT and zlib

Source0:        https://github.com/Kitware/CMake/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

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
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1b}
./bootstrap \
    --verbose \
    --parallel=%{?_smp_build_ncpus} \
    -- \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_DOC_PREFIX=/usr/share/doc \
    -DCMAKE_USE_OPENSSL=OFF

%else
./bootstrap \
    --verbose \
    --parallel=%{?_smp_build_ncpus} \
    -- \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_DOC_PREFIX=/usr/share/doc

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot}/%{?lfs_dir} install

%if %{with lfs}
rm -rf %{buildroot}/%{?lfs_dir}/usr/doc

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs}
%{?lfs_dir}/usr/bin/*
%{?lfs_dir}/usr/share/cmake-%{version_2}
%{?lfs_dir}/usr/share/{aclocal,bash-completion,emacs,vim}/*

%else
/usr/bin/{cmake,ccmake,ctest,cpack}
/usr/share/aclocal/cmake.m4
/usr/share/bash-completion/completions/{cmake,cpack,ctest}
/usr/share/cmake-%{version_2}
/usr/share/emacs/site-lisp/cmake-mode.el
/usr/share/vim/vimfiles/{indent,syntax}/cmake.vim

%files doc
/usr/share/doc/cmake-%{version_2}

%endif