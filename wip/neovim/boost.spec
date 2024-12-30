Name:           boost
Version:        1.87.0
Release:        1%{?dist}
Summary:        Free peer-reviewed portable C++ source libraries
License:        BSL

%global         u_version   1_87_0

Source:         https://boostorg.jfrog.io/artifactory/main/release/%{version}/source/boost_%{u_version}.tar.bz2

%description
Boost provides free peer-reviewed portable C++ source libraries.

We emphasize libraries that work well with the C++ Standard Library. Boost
libraries are intended to be widely useful, and usable across a broad spectrum
of applications. The Boost license encourages the use of Boost libraries for
all users with minimal restrictions.

We aim to establish "existing practice" and provide reference implementations
so that Boost libraries are suitable for eventual standardization. Beginning
with the ten Boost Libraries included in the Library Technical Report (TR1)
and continuing with every release of the ISO standard for C++ since 2011,
the C++ Standards Committee has continued to rely on Boost as a valuable
source for additions to the Standard C++ Library.

#---------------------------------------------------------------------------
%prep
%setup -q -n boost_%{u_version}

#---------------------------------------------------------------------------
%build
./bootstrap.sh --prefix=/usr

#---------------------------------------------------------------------------
%install
./b2 install --prefix=%{buildroot}/usr
rm -f %{buildroot}/usr/lib/*.a

#---------------------------------------------------------------------------
%files
/usr/include/boost
/usr/lib/cmake/*
/usr/lib/libboost_atomic.so
%shlib /usr/lib/libboost_atomic.so.%{version}
/usr/lib/libboost_charconv.so
%shlib /usr/lib/libboost_charconv.so.%{version}
/usr/lib/libboost_chrono.so
%shlib /usr/lib/libboost_chrono.so.%{version}
/usr/lib/libboost_container.so
%shlib /usr/lib/libboost_container.so.%{version}
/usr/lib/libboost_context.so
%shlib /usr/lib/libboost_context.so.%{version}
/usr/lib/libboost_contract.so
%shlib /usr/lib/libboost_contract.so.%{version}
/usr/lib/libboost_coroutine.so
%shlib /usr/lib/libboost_coroutine.so.%{version}
/usr/lib/libboost_date_time.so
%shlib /usr/lib/libboost_date_time.so.%{version}
/usr/lib/libboost_fiber.so
%shlib /usr/lib/libboost_fiber.so.%{version}
/usr/lib/libboost_filesystem.so
%shlib /usr/lib/libboost_filesystem.so.%{version}
/usr/lib/libboost_graph.so
%shlib /usr/lib/libboost_graph.so.%{version}
/usr/lib/libboost_iostreams.so
%shlib /usr/lib/libboost_iostreams.so.%{version}
/usr/lib/libboost_json.so
%shlib /usr/lib/libboost_json.so.%{version}
/usr/lib/libboost_locale.so
%shlib /usr/lib/libboost_locale.so.%{version}
/usr/lib/libboost_log.so
%shlib /usr/lib/libboost_log.so.%{version}
/usr/lib/libboost_log_setup.so
%shlib /usr/lib/libboost_log_setup.so.%{version}
/usr/lib/libboost_math_c99.so
%shlib /usr/lib/libboost_math_c99.so.%{version}
/usr/lib/libboost_math_c99f.so
%shlib /usr/lib/libboost_math_c99f.so.%{version}
/usr/lib/libboost_math_c99l.so
%shlib /usr/lib/libboost_math_c99l.so.%{version}
/usr/lib/libboost_math_tr1.so
%shlib /usr/lib/libboost_math_tr1.so.%{version}
/usr/lib/libboost_math_tr1f.so
%shlib /usr/lib/libboost_math_tr1f.so.%{version}
/usr/lib/libboost_math_tr1l.so
%shlib /usr/lib/libboost_math_tr1l.so.%{version}
/usr/lib/libboost_nowide.so
%shlib /usr/lib/libboost_nowide.so.%{version}
/usr/lib/libboost_prg_exec_monitor.so
%shlib /usr/lib/libboost_prg_exec_monitor.so.%{version}
/usr/lib/libboost_process.so
%shlib /usr/lib/libboost_process.so.%{version}
/usr/lib/libboost_program_options.so
%shlib /usr/lib/libboost_program_options.so.%{version}
/usr/lib/libboost_random.so
%shlib /usr/lib/libboost_random.so.%{version}
/usr/lib/libboost_regex.so
%shlib /usr/lib/libboost_regex.so.%{version}
/usr/lib/libboost_serialization.so
%shlib /usr/lib/libboost_serialization.so.%{version}
/usr/lib/libboost_stacktrace_addr2line.so
%shlib /usr/lib/libboost_stacktrace_addr2line.so.%{version}
/usr/lib/libboost_stacktrace_basic.so
%shlib /usr/lib/libboost_stacktrace_basic.so.%{version}
/usr/lib/libboost_stacktrace_from_exception.so
%shlib /usr/lib/libboost_stacktrace_from_exception.so.%{version}
/usr/lib/libboost_stacktrace_noop.so
%shlib /usr/lib/libboost_stacktrace_noop.so.%{version}
/usr/lib/libboost_system.so
%shlib /usr/lib/libboost_system.so.%{version}
/usr/lib/libboost_thread.so
%shlib /usr/lib/libboost_thread.so.%{version}
/usr/lib/libboost_timer.so
%shlib /usr/lib/libboost_timer.so.%{version}
/usr/lib/libboost_type_erasure.so
%shlib /usr/lib/libboost_type_erasure.so.%{version}
/usr/lib/libboost_unit_test_framework.so
%shlib /usr/lib/libboost_unit_test_framework.so.%{version}
/usr/lib/libboost_url.so
%shlib /usr/lib/libboost_url.so.%{version}
/usr/lib/libboost_wave.so
%shlib /usr/lib/libboost_wave.so.%{version}
/usr/lib/libboost_wserialization.so
%shlib /usr/lib/libboost_wserialization.so.%{version}
/usr/share/boost_predef