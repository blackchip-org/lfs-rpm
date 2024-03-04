Name:           grub
Version:        2.12
Release:        1%{?dist}
Summary:        The GRand Unified Bootloader
License:        GPLv3+

Source0:        https://ftp.gnu.org/gnu/grub/grub-%{version}.tar.xz


%description
Briefly, a boot loader is the first software program that runs when a computer
starts. It is responsible for loading and transferring control to the
operating system kernel software (such as the Hurd or Linux). The kernel, in
turn, initializes the rest of the operating system (e.g. GNU).

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

unset {C,CPP,CXX,LD}FLAGS
echo depends bli part_gpt > grub-core/extra_deps.lst
./configure --prefix=/usr          \
            --sysconfdir=/etc      \
            --disable-efiemu       \
            --disable-werror
%make
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_build_begin

unset {C,CPP,CXX,LD}FLAGS
%make DESTDIR=%{buildroot} install

mkdir -p %{buildroot}/usr/share/bash-completion/completions
mv -v    %{buildroot}/etc/bash_completion.d/grub \
         %{buildroot}/usr/share/bash-completion/completions
%lfs_build_end

#---------------------------------------------------------------------------
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
