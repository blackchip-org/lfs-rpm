Name:           cmake
Version:        3.30.2
Release:        1%{?dist}
Summary:        Cross-platform make system
License:        BSD and MIT and zlib

Source0:        https://github.com/Kitware/CMake/releases/download/v%{version}/cmake-%{version}.tar.gz

%description
CMake is used to control the software compilation process using simple platform
and compiler independent configuration files. CMake generates native makefiles
and workspaces that can be used in the compiler environment of your choice.
CMake is quite sophisticated: it is possible to support complex environments
requiring system configuration, preprocessor generation, code generation, and
template instantiation.

# This package is built using a bootstrap script but this spec file is
# provided so that spectool can download the source file.
