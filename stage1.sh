#!/bin/bash

. ./env 

case $1 in
    init)
        podman stop -t 0 lfs-stage1
        podman rm -f lfs-stage1
        podman build -t lfs-stage1 containers/lfs-stage1
        mkdir -p "$builddir"
        podman create \
            --name lfs-stage1 \
            --hostname lfs-stage1 \
            --userns keep-id \
            --volume "$builddir:/home/lfs/rpmbuild:z" \
            --volume .:/home/lfs/lfs-rpm:z \
            lfs-stage1
        podman start lfs-stage1
        ;;
    start)
        ;;
    stop)
        podman stop -t 0 lfs-stage1
        ;;
    build)
        exec podman exec -t lfs-stage1 bash -i /home/lfs/lfs-rpm/containers/lfs-stage1/build-stage1.sh
        ;;
    shell)
        exec podman exec -it lfs-stage1 bash
        ;;
    export)
        rm -f containers/lfs-stage2/lfs-stage2.tar.gz
        podman exec -t lfs-stage1 bash -i /home/lfs/lfs-rpm/containers/lfs-stage1/export-stage2.sh 
        podman cp lfs-stage1:/tmp/lfs-stage2.tar.gz containers/lfs-stage2
        ;; 
    *)
        echo "invalid command"
        exit 1
esac
