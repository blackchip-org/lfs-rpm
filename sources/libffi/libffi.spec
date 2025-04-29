# lfs

%global name            libffi
%global version         3.4.7
%global release         1

#---------------------------------------------------------------------------
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A portable foreign function interface library
License:        MIT

Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.sha256

%if !%{with lfs}
Recommends:     %{name}-info = %{version}
Recommends:     %{name}-man  = %{version}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%package info
Summary:        Info documentation for %{name}
BuildArch:      noarch

%package man
Summary:        Manual pages for %{name}
BuildArch:      noarch

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}%{?_isa}-devel

%endif

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

%if !%{with lfs}
%description devel
Development files for %{name}

%description info
Info documentation for %{name}

%description man
Manual pages for %{name}

%description static
Static libraries for %{name}

%endif

#---------------------------------------------------------------------------
%prep
%verify_sha256 -f %{SOURCE1}
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs}
./configure --prefix=/usr          \
            --disable-static       \
            --with-gcc-arch=native

%else
./configure --prefix=/usr          \
            --with-gcc-arch=native

%endif
make %{?_smp_mflags}

#---------------------------------------------------------------------------
%install
make DESTDIR=%{buildroot} install

#---------------------------------------------------------------------------
%check
%make check

#---------------------------------------------------------------------------
%files
%if %{with lfs}
/usr/include/*.h
/usr/lib/lib*.so*
/usr/lib/pkgconfig/*

%else
/usr/lib/libffi.so.*

%files devel
/usr/include/*.h
/usr/lib/libffi.so
/usr/lib/pkgconfig/libffi.pc

%files info
/usr/share/info/*.gz

%files man
/usr/share/man/man*/*.gz

%files static
/usr/lib/libffi.a

%endif
