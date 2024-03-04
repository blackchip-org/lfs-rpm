Name:           make
Version:        4.4.1
Release:        1%{?dist}
Summary:        A GNU tool which simplifies the build process for users
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/make/make-%{version}.tar.gz

%description
A GNU tool for controlling the generation of executables and other non-source
files of a program from the program's source files. Make allows users to build
and install packages without any significant knowledge about the details of the
build process. The details about how the program should be built are provided
for make in the program's makefile.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%if %{with lfs_stage1}
./configure --prefix=/usr   \
            --without-guile \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_install_begin

%if %{with lfs_stage1}
%make DESTDIR=%{buildroot}/%{lfs_dir} install

%endif
%lfs_install_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/make.mo
%endif
