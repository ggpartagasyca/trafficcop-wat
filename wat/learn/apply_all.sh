#!/bin/sh

# INPUT='Welcome to Paradise Spa'
# echo healthspa-default
# python postclassifier.py -v -n healthspa -i default --load --test 0 --apply "$INPUT"


# INPUT='<html><body>No black men please</body></html>'
# echo race-default
# python postclassifier.py -v -n race -i ci --load --test 0 --type html --apply "$INPUT"

# exit

indicators=( ci cs default )

for fullfile in data/test/*; do
    filename=$(basename "$fullfile")
    extension="${filename##*.}"
    filename="${filename%.*}"
    if [ "$extension" = "html" ] ;
    then
	type='html'
    else
	type='text'
    fi
    INPUT=`cat $fullfile`
    for indicator in "${indicators[@]}"
    do
	python postclassifier.py -v -n age -i $indicator --load --test 0 --type $type --apply "$INPUT"
	python postclassifier.py -v -n race -i $indicator --load --test 0 --type $type --apply "$INPUT"
	python postclassifier.py -v -n multi -i $indicator --load --test 0 --type $type --apply "$INPUT"
	python postclassifier.py -v -n agency -i $indicator --load --test 0 --type $type --apply "$INPUT"
	python postclassifier.py -v -n healthspa -i $indicator --load --test 0 --type $type --apply "$INPUT"
	python postclassifier.py -v -n offtopic -i $indicator --load --test 0 --type $type --apply "$INPUT"
	python postclassifier.py -v -n typical -i $indicator --load --test 0 --type $type --apply "$INPUT"
    done
done
