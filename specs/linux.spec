Name:           linux
Version:        6.7.4
Release:        1%{?dist}
Summary:        The Linux kernel
License:        GPLv2 and Redistributable, no modification permitted

Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%{version}.tar.xz

%description
The kernel package contains the Linux kernel (vmlinuz), the core of any Linux
operating system. The kernel handles the basic functions of the operating
system: memory allocation, process allocation, device input and output, etc.

#---------------------------------------------------------------------------
%prep
%setup -q

#---------------------------------------------------------------------------
%build
%lfs_build_begin

%make mrproper

%if %{with lfs_stage1}
%make headers
find usr/include -type f ! -name '*.h' -delete

%else
%make defconfig

cat <<EOF >.config.sed
# This prevents debug messages like "... used greatest stack depth"
# https://forums.gentoo.org/viewtopic-t-1024636-start-0-postdays-0-postorder-asc-highlight-.html
s/CONFIG_DEBUG_STACK_USAGE=y/CONFIG_DEBUG_STACK_USAGE=n/
EOF
sed -i .config -f .config.sed

%make

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%install
%lfs_build_begin

%if %{with lfs_stage1}
mkdir -p %{buildroot}/%{lfs_dir}/usr
cp -rv usr/include %{buildroot}/%{lfs_dir}/usr

%else
%make INSTALL_MOD_PATH=%{buildroot}/usr modules_install
install -m 755 -d %{buildroot}/boot
install -m 644 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{version}%{dist}.%{lfs_arch}
install -m 644 System.map            %{buildroot}/boot/System.map-%{version}
install -m 644 .config               %{buildroot}/boot/config-%{version}

ln -s vmlinuz-%{version}%{dist}.%{lfs_arch} %{buildroot}/boot/vmlinuz
ln -s System.map-%{version}                 %{buildroot}/boot/System.map
ln -s config-%{version}                     %{buildroot}/boot/config

install -m755 -d %{buildroot}/etc/modprobe.d
cat > %{buildroot}/etc/modprobe.d/usb.conf <<EOF
install ohci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i ohci_hcd ; true
install uhci_hcd /sbin/modprobe ehci_hcd ; /sbin/modprobe -i uhci_hcd ; true
EOF

rm %{buildroot}/usr/lib/modules/%{version}/build

%endif
%lfs_build_end

#---------------------------------------------------------------------------
%files
%if %{with lfs_stage1}
%{lfs_dir}/usr/include/*

%else
/boot/System.map-%{version}
/boot/System.map
/boot/config-%{version}
/boot/config
/boot/vmlinuz-%{version}%{dist}.%{lfs_arch}
/boot/vmlinuz
/etc/modprobe.d
/usr/lib/modules/%{version}

%endif
