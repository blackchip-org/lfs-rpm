#!/bin/bash -ex

rm -rf /build/pod
mkdir -p /build/pod

rpm -qa $(grep -v '^#' /build/lfs-rpm/containers/lfs-stage2/mkpod.pkg.txt) \
    > /tmp/pod.pkg.txt

mkdir -p /build/pod/root
for pkg in $(cat /tmp/pod.pkg.txt); do
    ( cd /build/pod &&
      rpm2cpio /build/rpmbuild/RPMS/x86_64/${pkg}.rpm | cpio -idmv && \
      install -m 644 -t /build/pod/root \
        /build/rpmbuild/RPMS/x86_64/${pkg}.rpm
    )
done

( cd /build/pod &&
  tar zcf /build/lfs-rpm/containers/lfs-pod/lfs-mkpod.tar.gz . )
