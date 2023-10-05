#!/bin/bash

case $1 in
    init)
        podman rm lfs-stage1
        podman build -t lfs-stage1 container/lfs-stage1
        podman create \
            --name lfs-stage1 \
            --hostname lfs-stage1 \
            --userns keep-id \
            --volume $HOME/.local/cache/lfs/rpmbuild:/home/lfs/rpmbuild:z \
            --volume .:/home/lfs/lfs-rpm:z \
            lfs-stage1
        ;;
    start)
        podman start lfs-stage1
        ;;
    stop)
        podman stop -t 0 lfs-stage1
        ;;
    build)
        exec podman exec -t lfs-stage1 bash -i /home/lfs/lfs-rpm/container/lfs-stage1/build-stage1.sh
        ;;
    shell)
        exec podman exec -it lfs-stage1 bash
        ;;
    *)
        echo "invalid command"
        exit 1
esac
