#!/bin/bash -e

sourcedir="$HOME/.local/cache/lfs/rpmbuild/SOURCES"

mkdir -p $sourcedir
wget --input-file=wget-list-systemd --continue --directory-prefix=$sourcedir

thisdir=$(pwd)
pushd $sourcedir
  md5sum -c "$thisdir/md5sums"
popd
