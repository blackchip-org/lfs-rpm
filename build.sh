#!/bin/bash -e 

echo "==== creating podman image for stage1"
./stage1.sh init 
echo "==== building stage1"
./stage1.sh build 
echo "==== exporting stage2"
./stage1.sh export 


echo "==== creating podman image for stage2"
./stage2.sh init 
echo "==== downloading rpm bootstrap files"
./stage2.sh download 
echo "==== bootstrapping rpm"
./stage2.sh bootstrap 
