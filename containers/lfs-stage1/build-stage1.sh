#!/bin/bash

set -e

thisdir="$(dirname $0)"
specdir="$HOME/lfs-rpm/specs/stage1"
rpmdir="$HOME/rpmbuild/RPMS/$(uname -m)"

packages=$(cat $HOME/lfs-rpm/containers/lfs-stage1/stage1.txt)

cd $specdir
for package in $packages; do
    if ! rpm -q ${package}; then
        rpmbuild -bb ${package}.spec
        sudo rpm -i --replacefiles "$rpmdir/${package}*.rpm"
    fi
done
