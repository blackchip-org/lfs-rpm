#!/bin/bash

. ./env 

case $1 in
    init)
        podman stop -t 0 lfs-stage2
        podman rm -f lfs-stage2
        podman build -t lfs-stage2 containers/lfs-stage2
        podman create \
            --name lfs-stage2 \
            --hostname lfs-stage2 \
            --volume "$builddir:/home/lfs/rpmbuild:z" \
            --volume .:/home/lfs/lfs-rpm:z \
            lfs-stage2
        ;;
    start)
        podman start lfs-stage2 
        ;;
    shell)
        exec podman exec -it lfs-stage2 /usr/bin/bash 
        ;;
    *)
        echo "invalid command"
        exit 1
esac
