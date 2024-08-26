
# manual-vm 

Instructions for creating a virtual machine manually using the virt-manager
GUI:

- Start virt-manager
- Select File -> New Virtual Machine
- Select "Import existing disk image"
- For "Provide the existing storage path" and select "lfs-12.2-root.img"
- For "Choose the operating system your are installing", select "Generic Linux 2022"
- Click on "Forward"
- Adjust memory and CPUs as needed and click on "Forward"
- For "Name", put in "LFS" or any name that you like
- Click on "Customize configuration before install"
- Click on "Finish"
- On the left sidebar, select "Boot Options" and then open "Direct kernel boot"
- Click on "Enable direct kernel boot"
- For "Kernel path" select "lfs-12.2-vmlinuz"
- Leave "Initrd path" blank
- For "Kernel args" enter in "root=/dev/vda rw"
- Click on "Apply"
- On the left sidebar, select "Video Virtio"
- Change Model from "Virtio" to "VGA"
- Click on "Apply"
- In the top left-hand corner, select "Begin Installation"
