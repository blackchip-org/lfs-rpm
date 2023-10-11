#!/bin/bash -e

msg() {
    echo -e "\n===== $@"
}

msg "downloading sources for stage1"
./lfs.sh 1 download
msg "creating podman image for stage1"
./lfs.sh 1 init
msg "building stage1"
./lfs.sh 1 build
msg "exporting stage1"
./lfs.sh 1 export

msg "downloading sources for stage1a"
./lfs.sh 1a download
msg "creating podman image for stage1a"
./lfs.sh 1a init
msg "bootstrapping rpm"
./lfs.sh 1a bootstrap
msg "building stage1a"
./lfs.sh 1a build 
msg "exporting stage1a"
./lfs.sh 1a export

msg "downloading sources for stage2"
./lfs.sh 2 download
msg "creating podman image for stage2"
./lfs.sh 2 init 
msg "building stage2"
./lfs.sh 2 build 
