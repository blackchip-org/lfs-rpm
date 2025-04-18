#!/bin/bash

specs=$(ls specs)
for spec in $specs; do
    pkg_name=$(basename $spec | sed 's/\.spec$//' )
    cp specs/$spec sources/$pkg_name
done
