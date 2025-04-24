# lfs-rpm

A [Linux from Scratch](https://www.linuxfromscratch.org/) (LFS) build using
[podman](https://podman.io/) and the [RPM](https://rpm.org/) package
manager. These build steps follow LFS version 12.3-systemd.

Before you read any further, have you built [Linux from
Scratch](https://www.linuxfromscratch.org/) yourself? If not, I highly
recommend doing it. The book is very well written and it is a fun exercise in
which you learn the intimate details of what it takes to build an operating
system.

I built LFS about five years ago and I decided now was a good time to give it
another try. This time, though, I wanted to mix it up a bit. Instead of using
my Linux system and a chroot to build LFS, I wanted to use podman instead. And
I wanted to use RPM infrastructure for building and installing the packages
too. This repository holds the result of this work.

This build creates a bootable system, using a virutal machine, where you can
get to a login prompt, login, and type in `echo "hello world!"`. Not much else
has been tested beyond that. Additional testing and hacking is left to me as a
fun exercise for a future rainy day activity. There is a chance that there are
major errors with the system that have yet to be discovered. I am not an expert
in building operating systems nor am I an expert in RPM packaging. This
repository should only be used as a guide of one way this could be done but it
is nowhere near an optimal or proper way. Others may have done this already but
that was done for their fun, not mine.

## Build Requirements

### Fedora

Install *podman* for use as the build environment:

    sudo dnf install podman

To test the image in a virtual machine, install:

    sudo dnf install qemu-kvm virt-manager

To continue onward after the initial LFS build, install createrepo:

    sudo dnf install createrepo_c

### Ubuntu

Install *podman* for use as the build environment and also *rpm* and *curl*:

    sudo apt install podman rpm curl

To test the image in a virtual machine, install:

    sudo apt install qemu-kvm virt-manager

Start libvirtd and add yourself to the libvirt group:

    sudo systemctl start libvirtd
    sudo usermod -a -G libvirt $USER
    newgrp libvirt


## Automated Build

If you are lucky and cross your fingers the entire system can be built and
booted with the following three steps:

### Run `./lfs build-all`

This downloads all the necessary source files and builds them using podman. This
will take some time. Here are the timing results from my personal desktop with
an Intel i7-7700 CPU, SSD hard drive, 16 GiB of memory, default podman
configuration, and *make -j8*:

```
real	131m27.156s
```

Once done, the root filesystem can be found at `build/stage2/lfs-stage2.tar.gz`
and the kernel at `build/boot/vmlinuz`

If the build fails for some reason, you can continue the build using the
manual procedure below. Running this command will start everything from
the beginning which is usually what you don't want.

### Run `./lfs mkimage`

The tarball now has to be converted to a filesystem image. This requires root
privileges as it is necessary to temporarily mount the image to copy in the
filesystem. Run this command and enter in your password if prompted. The root
filesystem image will now be at `build/lfs-12.3-root.img`

### Run `./lfs install`

The emulator is going to need access to two files: the root filesystem image,
and the kernel. By default, it won't have access to files in your home
directory. Running install will copy those files to */var/lib/libvirt/images*
as:

- `lfs-12.3-root.img`
- `lfs-12.3-vmlinuz`

Now create a virtual machine using the following steps:

- Start virt-manager
- Select File -> New Virtual Machine
- Select "Import existing disk image"
- For "Provide the existing storage path" and select `lfs-12.3-root.img`
- For "Choose the operating system your are installing", select "Generic Linux 2022"
- Click on "Forward"
- Adjust memory and CPUs as needed and click on "Forward"
- For "Name", put in "LFS" or any name that you like
- Click on "Customize configuration before install"
- Click on "Finish"
- On the left sidebar, select "Boot Options" and then open "Direct kernel boot"
- Click on "Enable direct kernel boot"
- For "Kernel path" select `lfs-12.3-vmlinuz`
- Leave "Initrd path" blank
- For "Kernel args" enter in `root=/dev/vda rw`
- Click on "Apply"
- On the left sidebar, select "Video Virtio"
- Change Model from "Virtio" to "VGA"
- Click on "Apply"
- In the top left-hand corner, select "Begin Installation"

The operating system should now boot. Login as root and there is no password.
Verify network connectivity with `ping 8.8.8.8`.

If the boot hangs after a bunch of pci and pci_bus messages, change the video
settings under "Video Virtio" from "Virtio" to "VGA".

## Build Process

The build is split into four separate stages which correspond to chapters
in the [LFS](https://www.linuxfromscratch.org/) book. Those stages are:

- stage1a: [Chapter 5](https://linuxfromscratch.org/lfs/view/stable-systemd/chapter05/introduction.html), Compiling a Cross-Toolchain
- stage1b: [Chapter 6](https://linuxfromscratch.org/lfs/view/stable-systemd/chapter06/introduction.html), Cross Compiling Temporary Tools
- stage1c: [Chapter 7](https://linuxfromscratch.org/lfs/view/stable-systemd/chapter07/introduction.html), Entering Chroot and Building Additional Temporary Tools
- stage2: [Chapter 8](https://linuxfromscratch.org/lfs/view/stable-systemd/chapter08/introduction.html), Installing Basic System Software

The chapter breaks provide natural "save points" in the build process. Each
stage is built in a separate podman container and the results of the build are
exported for use in the next stage.

The full procedure to build LFS without `build-all` is:

    ./lfs download  # optional

    ./lfs 1a init
    ./lfs 1a build
    ./lfs 1a export

    ./lfs 1b init
    ./lfs 1b build
    ./lfs 1b export

    ./lfs 1c init
    ./lfs 1c build
    ./lfs 1c export

    ./lfs 2 init
    ./lfs 2 build
    ./lfs 2 export

    ./lfs mkimage
    ./lfs install

## The `lfs` script

The `lfs` script is used to automate portions of the build process. The
available commands are as follows:

### `./lfs <stage> init`

To create a podman image and container for use in building a stage, use this
command where `<stage>` is one of the stages listed above. The word *stage* can
be omitted for brevity so that either "stage1b" or "1b" can be used. For
example, to create a container for the first stage, use:

    ./lfs 1a init

Contexts are found in the `containers` directory. Each context has a
`<stage>.pkg.txt` file that contains a list of spec files to build relative
to the repository root.

This command always attempts to remove the existing podman container. If work
has already been done in a container, this work will be lost. It makes it easy
to start over when needed but be aware that it will do so without any
confirmation from you.

### `./lfs <stage> build`

This command builds all packages, in order, found in `<stage>.pkg.txt` and
then uses RPM to install. In the event that the build fails, this command can
be reissued and it will skip packages that have already been installed. All
RPMs during the LFS build are installed using the `--nodeps` flag. Automatic
dependency handling will be used after the base system is setup.

Temporary packages are built with the *-bb* flag to only build RPMs while the
packages in stage2 are built with *-ba* to create RPMs and SRPMs. These
can be found in the `build/<stage>/{rpms,srpms}` directories which are
bind mounted in the containers at `/build/rpmbuild/{RPMS,SRPMS}`. All
packages are built with the *x86_64* arch even if they qualify as a *noarch*
package.

### `./lfs <stage> export`

Once the build completes, issue this command to export the build results for
use in the next stage. A tarball will be created in the build directory under
`build/<stage>/lfs-<stage>.tar.gz` and in the container context for the
next stage.

### `./lfs <stage> {start,stop}`

Once the containers have been created, they can individually be started or
stopped with these commands. To get the list of containers that are currently
running use:

    podman ps

If you need to take a break during the build process, this command can be
used to easily stop the containers and then to start them up at a later time.

### `./lfs <stage> {shell,root}`

Login to the container as the unprivileged user lfs (using *shell*) or as the
root user (using *root*). In stage1a and stage1b you can *sudo* to root as the
lfs user but in stage1c and stage2 that command is not available and you must
use the `./lfs <stage> root` command. The repository root is bind mounted at
`/build/lfs-rpm` and the sources directory at `/build/rpmbuild/SOURCES`.

### `./lfs <stage> rpm [specfile...]`

Build a single RPM in *stage* using the given *specfile*. More then one
specfile can be provided if necessary. If this RPM has already been installed,
it will be rebuilt and reinstalled by replacing the older package. This command
is useful during development when iterating on a specific package without
needing to run *build*.

By default, *%check* scriptlets are skipped when building RPMs. Prefix this
command with `with_check=1` to run any provided tests. This shouldn't be
done with the general build command as quite a few packages work fine with
a few test failures.

### `./lfs download [specfile...]`

Source files are downloaded during the build process if they have not already
been downloaded. This command is useful if you want to download all the
packages upfront or if you need to download a specific package before building.
If no specfiles are provided on the command line, all source packages will be
downloaded.

### `./lfs env`

A handful of environmental variables are injected into each container. This
command shows you the current values of those variables. When debugging the
*lfs* script, it can sometimes be useful to inject these variables into your
current shell with `source ./lfs-env`. These variables can be overridden by
placing changes in a `local-lfs.env` file. Variables of note:

- `lfs_version`: Defines which version of LFS is being built. This is used in
URLs for downloading LFS specific patches and in the dist variable for
rpmbuild.
- `lfs_host_image`: The base podman image used in the *FROM* clause that is
used in the containers for stage1a and stage1b.
- `lfs_nproc`: Number of parallel make processes to use when building. This
is usually set to the number of processors on your machine.
- `lfs_root_size`: Size to use for the root partition filesystem image.

### `./lfs clean`

This resets everything to start a build from scratch again. It deletes
everything under the *build* directory except for the sources, all exports
under *containers* and removes any podman images or containers.

### `./lfs dist-clean`

The same as `./lfs clean` but also removes the sources directory.

## RPM Notes

In stage1a and stage1b, the *rpm* and *rpmbuild* commands provided by the
Fedora image are used. Some macros are installed under
`/usr/lib/rpm/macros.d/macros.lfs` to assist with the build:

- `%dist`: Fedora uses a dist tag such as *fc41* and Red Hat Enterprise
Linux uses dist tags such as *el9*. This build uses *lfs12_3*.
- `%_build_id_links`: By default, Fedora wants to generate files in
`/usr/lib/.build-id` for debugging purposes. This isn't necessary for an LFS
build and just adds clutter to the build. This setting is set to *none* to
disable this feature.
- `%debug_package`: Fedora also wants to generate debuginfo packages which
we don't need. Set to *%{nil}* to disable.
- `%make`: We use this macro in all the spec files when using the make
command. This adds the *-j* flag which controls the number of parallel
processes to use.
- `%shlib`: This sets the permissions to 755 for shared library files.
- `%use_lfs_tools`: This is used in stage1a and stage1b to add the LFS tools
directory to the front of the search path to ensure those tools are used
when available.
- `%discard_docs`: When building the temporary toolset, it isn't necessary
to keep any generated documentation. This macro removes those files and
that helps keep the build images a bit smaller.
- `%discard_locales%`: Also used when building the temporary toolset but
for discarding additional locale files.
- `%remove_info_dir`: When info documentation pages are generated, the
`/usr/share/info/dir` file usually gets updated. This cannot be done at
build or install time because multiple RPMs cannot "own" the same file.
This macro deletes this file and then the following two macros are then used:
- `%request_info_dir`: This macro should be placed in the `%post` scriptlet
to place a request to regenerate the info dir file. Then use the following
macro:
- `%update_info_dir`: This macro should be placed in the `%posttrans` scriptlet
to regenerate the info dir file. If multiple packages are installed that have
info files, the actual regeneration only occurs once.

When using Fedora in stage1a and stage1b, there are two other macros
provided in `/usr/lib/rpm/redhat/macros` that are changed. Sed scripts
in the Containerfile make these modifications:

- `%source_date_epoch_from_changelog`: The specfiles are not using changelogs
and by setting this to zero, it removes a warning about not having a changelog.
- `%_auto_set_build_flags`: This sets a whole list of additional *CFLAGS* that
Fedora wants you to use when building packages but this causes a build
failure somewhere. This is disabled to prevent this from happening.

Another macro file, `/usr/lib/rpm/macros.d/macros.lfs-stage` is added with
stage specific information. It has a `%with_<stage> 1` macro used to
identify if a specific stage is being used and `%with_stage1` to identify
when in stage1. Quite a few packages need to be built twice, once as a
temporary tool and once as the final package. The same specfile is used
but differences in the builds are separated with conditionals using the
`%with_stage1` macro. Some packages are built three or four times and use
the additional *with* macros as necessary.

The RPM database is used during the build to track which packages have been
built and installed for that stage, not for packages which already exist on the
system. When the container for stage1a is created, the contents of the existing
RPM database are deleted. Subsequent stages do not keep the database between
exports.

## Logs

Logs can be found in *build/logs*. Those files are:

- `build.log`: Timestamp and record of when each package build is started
and completed.
- `last-started`: Name of the last package that the build started
- `last-success`: Name of the last package that was built successfully
- `<stage>/<package>.log`: Standard output and standard error capture of
*rpmbuild* and *rpm* for that package.

## And beyond...

To build packages beyond the initial set required to boot the operating
system, it is helpful to start using dependency tracking and resolution provided
by `rpm` and `dnf`. Stage 3 continues onward to build the packages necessary to
get a minimal `dnf` version 5 executable:

    ./lfs 3 init
    ./lfs 3 build

The stage 3 container now has a little over 100 packages installed at this
point. Each step along the way has been adding more and more packages to
satisfy dependencies for later packages in the build. It is now time to create
a podman image dedicated to building individual packages instead of an entire
operating system.

The image is going to be pruned down to basic tools needed for building. To
create this image, first run:

### `./lfs 3 mkpod`

This creates a tarball to be used as the base filesystem for the general
build container. The list of packages included are found in
`containers/lfs-pod/mkpod.pkg.txt`. Going forward, rpm spec files must use
`BuildRequires` for packages not found in `mkpod.pkg.txt`.

### `./pod init`

The `pod` script is going to be used from now on instead of the `lfs` script.
This creates a new podman image using the tarball created above but does
not yet start a container.

Configuration for this environment can be found in `pod-env`. Right now it
only contains the build arch and the dist tag which is now `pod12_3`. If you
would like to customize the build to use your own dist tag, create a
`local-pod.env` file and add to it *pod_dist* with the name of your
choosing.

### `./pod rpm <specfile>`

Creates or recreates a new container and builds the rpm for the given spec
file. The results of the build are found in `build/pod` and this directory is
also a dnf repository available to the container. Subsequent builds can use
`BuildRequires` to automatically install packages found here.

### `./pod build <packages.spec.txt>`

This calls `./pod rpm` for each spec file found in *packages.spec.txt*. To
rebuild all spec files up to stage 3 in the proper order, use:

    ./pod build rebuild.spec.txt

### `./pod export <image.pkg.txt>`

Export a filesystem for a bootable image using the list of
packages found in *image.pkg.txt*. The build container is used as the base
for this filesystem so any additional package required to boot must be
found in the package list. An example of a working set can be found in
`pod-image.pkg.txt`. Add additional packages to this list as desired.

After the image is exported, the image can be booted using
`./lfs mkimage build/pod/lfs-pod.tar.gz` and `./lfs install`.

### `./pod {shell,root}`

In the event of a build failure, the container will still be running and
this command can be used to login and investigate.

### `./pod {create,destroy}`

Create and start or destroy a build container.

## Booting Beyond

Below is an example, and a working set, of commands to execute to boot an
image with packages built with the podman build container:

    ./lfs 3 mkpod
    ./pod init
    ./pod build rebuild.spec.txt
    ./pod export pod-image.pkg.txt
    ./lfs mkimage-pod
    ./lfs install

Now create the virtual machine as described above and login into the root
account which has no password.

## Final Notes

I have subscribed to the LFS announcement mailing list and will try to keep this
up-to-date as new versions of LFS are published. No guarantee on when that
happens or even if I follow through with it.

## License

MIT

## Feedback

Contact me at lfs@blackchip.org
