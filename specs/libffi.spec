Name:           libffi
Version:        3.4.6
%global         so_version  8.1.4
Release:        1%{?dist}
Summary:        A portable foreign function interface library
License:        MIT

Source:         https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz

Suggests:       %{name}-doc = %{version}

%description
Compilers for high level languages generate code that follow certain
conventions. These conventions are necessary, in part, for separate compilation
to work. One such convention is the "calling convention". The calling
convention is a set of assumptions made by the compiler about where function
arguments will be found on entry to a function. A calling convention also
specifies where the return value for a function is found.

Some programs may not know at the time of compilation what arguments are to be
passed to a function. For instance, an interpreter may be told at run-time
about the number and types of arguments used to call a given function. `Libffi'
can be used in such programs to provide a bridge from the interpreter program
to compiled code.

The `libffi' library provides a portable, high level programming interface to
various calling conventions. This allows a programmer to call any function
specified by a call interface description at run time.

FFI stands for Foreign Function Interface. A foreign function interface is the
popular name for the interface that allows code written in one language to call
code written in another language. The `libffi' library really only provides the
lowest, machine dependent layer of a fully featured foreign function interface.
A layer must exist above `libffi' that handles type conversions for values
passed between the two languages.

%package man
Summary:        Manual pages for %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       texinfo
Recommends:     %{name}-man = %{version}

%description man
Manual pages for %{name}

%description doc
Documentation for %{name}

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
./configure --prefix=/usr          \
            --disable-static       \
            --with-gcc-arch=native
%make

#---------------------------------------------------------------------------
%install
%make DESTDIR=%{buildroot} install
%remove_info_dir

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%post doc
%request_info_dir

%posttrans doc
%update_info_dir

#---------------------------------------------------------------------------
%files
/usr/include/*
/usr/lib/libffi.so
/usr/lib/libffi.so.8
%shlib /usr/lib/libffi.so.%{so_version}
/usr/lib/pkgconfig/libffi.pc

%files doc
/usr/share/info/*

%files man
/usr/share/man/man*/*
