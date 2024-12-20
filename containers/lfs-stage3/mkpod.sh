#!/bin/bash -ex

rm -rf /build/pod
mkdir -p /build/pod

rpm -qa $(grep -v '^#' /build/lfs-rpm/containers/lfs-pod/mkpod.pkg.txt) \
    > /tmp/pod.pkg.txt

mkdir -p /build/mkpod
cp /build/lfs-rpm/build/stage{2,3}/rpms/x86_64/*.rpm /build/mkpod

mkdir -p /build/pod/root
for pkg in $(cat /tmp/pod.pkg.txt); do
    ( cd /build/pod &&
      rpm2cpio /build/mkpod/${pkg}.rpm | cpio -idmv && \
      install -m 644 -t /build/pod/root \
        /build/mkpod/${pkg}.rpm
    )
done

( cd /build/pod &&
  tar zcf /build/lfs-rpm/containers/lfs-pod/lfs-mkpod.tar.gz . )
