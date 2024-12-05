#!/bin/bash -ex

rpm -i /build/lfs-rpm/build/deps/*.rpm
rpmbuild \
    -ba \
    lfs-rpm/$1

