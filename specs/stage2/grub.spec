%global version         2.06
%global lfs_version     12.0
%global _build_id_links none

Name:           grub
Version:        %{version}
Release:        1%{?dist}
Summary:        The GRand Unified Bootloader
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/grub/grub-%{version}.tar.xz
Patch0:         https://www.linuxfromscratch.org/patches/lfs/%{lfs_version}/grub-%{version}-upstream_fixes-1.patch


%description
Briefly, a boot loader is the first software program that runs when a computer
starts. It is responsible for loading and transferring control to the
operating system kernel software (such as the Hurd or Linux). The kernel, in
turn, initializes the rest of the operating system (e.g. GNU).


%prep
%setup -q
%patch 0 -p 1


%build
unset {C,CPP,CXX,LD}FLAGS
./configure --prefix=/usr          \
            --sysconfdir=/etc      \
            --disable-efiemu       \
            --disable-werror
make


%install
unset {C,CPP,CXX,LD}FLAGS
make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/share/bash-completion/completions
mv -v    %{buildroot}/etc/bash_completion.d/grub \
         %{buildroot}/usr/share/bash-completion/completions
rm       %{buildroot}/usr/share/info/dir


%files
/etc/grub.d
/usr/bin/grub-editenv
/usr/bin/grub-file
/usr/bin/grub-fstest
/usr/bin/grub-glue-efi
/usr/bin/grub-kbdcomp
/usr/bin/grub-menulst2cfg
/usr/bin/grub-mkimage
/usr/bin/grub-mklayout
/usr/bin/grub-mknetdir
/usr/bin/grub-mkpasswd-pbkdf2
/usr/bin/grub-mkrelpath
/usr/bin/grub-mkrescue
/usr/bin/grub-mkstandalone
/usr/bin/grub-render-label
/usr/bin/grub-script-check
/usr/bin/grub-syslinux2cfg
/usr/lib/grub
/usr/sbin/grub-bios-setup
/usr/sbin/grub-install
/usr/sbin/grub-macbless
/usr/sbin/grub-mkconfig
/usr/sbin/grub-ofpathname
/usr/sbin/grub-probe
/usr/sbin/grub-reboot
/usr/sbin/grub-set-default
/usr/sbin/grub-sparc64-setup
/usr/share/bash-completion/completions/grub
/usr/share/grub/grub-mkconfig_lib
/usr/share/info/*
/usr/share/locale/*/LC_MESSAGES/grub.mo



