#!/bin/sh

FILES=`cat wat_annot_escort_01.files`

for FILE in ${FILES[@]};
do 
    python bp-extract.py -t -b $FILE
done
