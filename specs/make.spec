# lfs

%global name        make
%global version     4.4.1
%global release     1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A GNU tool which simplifies the build process for users
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

Suggests:       %{name}-doc = %{version}

%description
A GNU tool for controlling the generation of executables and other non-source
files of a program from the program's source files. Make allows users to build
and install packages without any significant knowledge about the details of the
build process. The details about how the program should be built are provided
for make in the program's makefile.

%package lang
Summary:        Language files for %{name}
Requires:       %{name} = %{version}

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description lang
Language files for %{name}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
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
%discard_locales

%else
%make DESTDIR=%{buildroot} install
%remove_info_dir

%endif

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/include/*

%else
/usr/bin/make
/usr/include/*

%files lang
/usr/share/locale/*/LC_MESSAGES/*

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*

%endif
