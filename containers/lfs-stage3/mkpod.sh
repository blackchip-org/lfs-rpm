#!/bin/bash -ex

rm -rf /rpmbuild/pod
mkdir -p /rpmbuild/pod

rpm -qa $(grep -v '^#' /host/containers/lfs-pod/mkpod.pkg.txt) \
    > /tmp/pod.pkg.txt

mkdir -p /rpmbuild/mkpod
cp /host/build/rpms/stage{2,3}/x86_64/*.rpm /rpmbuild/mkpod

mkdir -p /rpmbuild/pod/root
for pkg in $(cat /tmp/pod.pkg.txt); do
    ( cd /rpmbuild/pod &&
      rpm2cpio /rpmbuild/mkpod/${pkg}.rpm | cpio -idmv && \
      install -m 644 -t /rpmbuild/pod/root \
        /rpmbuild/mkpod/${pkg}.rpm
    )
done

( cd /rpmbuild/pod &&
  tar zcf /host/containers/lfs-pod/lfs-mkpod.tar.gz . )

rm -rf /rpmbuild/{pod,mkpod}
