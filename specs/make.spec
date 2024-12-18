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
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr   \
            --without-guile \
            --host=%{lfs_tgt} \
            --build=$(build-aux/config.guess)

%else
./configure --prefix=/usr

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
%make DESTDIR=%{buildroot}/%{lfs_dir} install
%discard_docs

%else
%make DESTDIR=%{buildroot} install
%remove_info_dir

%endif

#---------------------------------------------------------------------------
%post
%update_info_dir

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*
%{lfs_dir}/usr/share/locale/*/LC_MESSAGES/%{name}.mo

%else
/usr/bin/make
/usr/include/*
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/%{name}.mo
/usr/share/man/man1/*

%endif
