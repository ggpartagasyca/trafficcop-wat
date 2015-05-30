#!/bin/sh

FILES=`cat raw_data_manifest.txt`

for FILE in ${FILES[@]};
do 
    python bp-extract.py -t -b $FILE
done
