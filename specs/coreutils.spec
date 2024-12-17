Name:           coreutils
Version:        9.5
Release:        1%{?dist}
Summary:        A set of basic GNU tools commonly used in shell scripts
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/coreutils/coreutils-%{version}.tar.xz

%description
These are the GNU core utilities. This package is the combination of the old
GNU fileutils, sh-utils, and textutils packages.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%if %{with lfs_stage1}
%use_lfs_tools
./configure --prefix=/usr                     \
            --host=%{lfs_tgt}                 \
            --build=$(build-aux/config.guess) \
            --enable-install-program=hostname \
            --enable-no-install-program=kill,uptime

%else
autoreconf -fiv
FORCE_UNSAFE_CONFIGURE=1 ./configure \
            --prefix=/usr            \
            --enable-no-install-program=kill,uptime

%endif
%make

#---------------------------------------------------------------------------
%install
%if %{with lfs_stage1}
%use_lfs_tools
make DESTDIR=%{buildroot}/%{lfs_dir} install
mkdir -p %{buildroot}/%{lfs_dir}/usr/sbin
mv -v %{buildroot}/%{lfs_dir}/usr/bin/chroot %{buildroot}/%{lfs_dir}/usr/sbin
%discard_docs

%else
make DESTDIR=%{buildroot} install

mkdir %{buildroot}/usr/sbin
mkdir %{buildroot}/usr/share/man/man8

mv -v %{buildroot}/usr/bin/chroot %{buildroot}/usr/sbin
mv -v %{buildroot}/usr/share/man/man1/chroot.1 %{buildroot}/usr/share/man/man8/chroot.8
sed -i 's/"1"/"8"/' %{buildroot}/usr/share/man/man8/chroot.8

%endif

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/bin/*
%{lfs_dir}/usr/sbin/*
%{lfs_dir}/usr/libexec/coreutils
%{lfs_dir}/usr/share/locale/*/LC_{MESSAGES,TIME}/coreutils.mo

%else
/usr/bin/[
/usr/bin/b2sum
/usr/bin/base32
/usr/bin/base64
/usr/bin/basename
/usr/bin/basenc
/usr/bin/cat
/usr/bin/chcon
/usr/bin/chgrp
/usr/bin/chmod
/usr/bin/chown
/usr/bin/cksum
/usr/bin/comm
/usr/bin/cp
/usr/bin/csplit
/usr/bin/cut
/usr/bin/date
/usr/bin/dd
/usr/bin/df
/usr/bin/dir
/usr/bin/dircolors
/usr/bin/dirname
/usr/bin/du
/usr/bin/echo
/usr/bin/env
/usr/bin/expand
/usr/bin/expr
/usr/bin/factor
/usr/bin/false
/usr/bin/fmt
/usr/bin/fold
/usr/bin/groups
/usr/bin/head
/usr/bin/hostid
/usr/bin/id
/usr/bin/install
/usr/bin/join
/usr/bin/link
/usr/bin/ln
/usr/bin/logname
/usr/bin/ls
/usr/bin/md5sum
/usr/bin/mkdir
/usr/bin/mkfifo
/usr/bin/mknod
/usr/bin/mktemp
/usr/bin/mv
/usr/bin/nice
/usr/bin/nl
/usr/bin/nohup
/usr/bin/nproc
/usr/bin/numfmt
/usr/bin/od
/usr/bin/paste
/usr/bin/pathchk
/usr/bin/pinky
/usr/bin/pr
/usr/bin/printenv
/usr/bin/printf
/usr/bin/ptx
/usr/bin/pwd
/usr/bin/readlink
/usr/bin/realpath
/usr/bin/rm
/usr/bin/rmdir
/usr/bin/runcon
/usr/bin/seq
/usr/bin/sha1sum
/usr/bin/sha224sum
/usr/bin/sha256sum
/usr/bin/sha384sum
/usr/bin/sha512sum
/usr/bin/shred
/usr/bin/shuf
/usr/bin/sleep
/usr/bin/sort
/usr/bin/split
/usr/bin/stat
/usr/bin/stdbuf
/usr/bin/stty
/usr/bin/sum
/usr/bin/sync
/usr/bin/tac
/usr/bin/tail
/usr/bin/tee
/usr/bin/test
/usr/bin/timeout
/usr/bin/touch
/usr/bin/tr
/usr/bin/true
/usr/bin/truncate
/usr/bin/tsort
/usr/bin/tty
/usr/bin/uname
/usr/bin/unexpand
/usr/bin/uniq
/usr/bin/unlink
/usr/bin/users
/usr/bin/vdir
/usr/bin/wc
/usr/bin/who
/usr/bin/whoami
/usr/bin/yes
/usr/libexec/coreutils/libstdbuf.so
/usr/sbin/chroot
/usr/share/info/coreutils.info.gz
/usr/share/locale/*/LC_{MESSAGES,TIME}/coreutils.mo
/usr/share/man/man{1,8}/*

%endif

