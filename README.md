# lfs-rpm

A [Linux from Scratch](https://www.linuxfromscratch.org/) (LFS) build using
[podman](https://podman.io/) and the [RPM](https://rpm.org/) package
manager.

Before you read any further, have you built [Linux from
Scratch](https://www.linuxfromscratch.org/) yourself? If not, I highly
recommend doing it. The book is very well written and it is a fun exercise in
which you learn the intimate details of what it takes to build an operating
system.

I built LFS about five years ago and I decided now was a good time to give it
another try. This time, though, I wanted to mix it up a bit. Instead of using
the host system and a chroot to build the system, I wanted to use podman
instead. And I wanted to use RPM infrastructure for building and installing the
packages too. This repository holds to result of this work.

This build creates a bootable system, using QEMU, where you can get to a login
prompt, login, and type in `echo "hello world!"`. Not much else has been tested
beyond that. Additional testing and hacking is left to me as a fun exercise for
a future rainy day activity. There is a chance that there are major errors with
the system that have yet to be discovered. I am not an expert in building
operating systems nor am I an expert in RPM packaging. This repository should
really only be used as a guide of one way this could be done but it is nowhere
near an optimal or proper way. Others may have done this already but that was
done for their fun, not mine. 

## Build Requirements

This has only been tested on a Fedora operating system. Install `podman` for
use as the build environment and `rpmdevtools` to use `spectool` to
download the necessary source packages:

```
sudo dnf install podman rpmdevtools
```

## tl;dr

If you are lucky, cross your fingers, and enter in the following command, the
entire operating system should be built automatically:

```
./lfs build-all
```

TODO: artifacts and starting VM


## License

MIT 

## Feedback

Contact me at lfs@blackchip.org

