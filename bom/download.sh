#!/bin/bash -e

sourcedir="$HOME/.local/cache/lfs/rpmbuild/SOURCES"
mkdir -p $sourcedir

groups="lfs-systemd lfs-extra"

for group in $groups; do
  wget --input-file=${group}.wget --continue --directory-prefix=$sourcedir

  thisdir=$(pwd)
  pushd $sourcedir
    md5sum -c "$thisdir/${group}.md5sums"
  popd
done
