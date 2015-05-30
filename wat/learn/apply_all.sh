#!/bin/sh

# INPUT='Welcome to Paradise Spa'
# echo healthspa-default
# python postclassifier.py -v -n healthspa -i default --load --test 0 --apply "$INPUT"


# INPUT='<html><body>No black men please</body></html>'
# echo race-default
# python postclassifier.py -v -n race -i ci --load --test 0 --type html --apply "$INPUT"

# exit

for fullfile in data/test/*; do
    filename=$(basename "$fullfile")
    extension="${filename##*.}"
    filename="${filename%.*}"
    if [ "$extension" = "html" ] ;
    then
	python postclassifier.py -v -n age -i ci --load --test 0 --type html --apply "`cat $fullfile`"
    else
	python postclassifier.py -v -n age -i ci --load --test 0 --type text --apply "`cat $fullfile`"
    fi
done
exit

echo age-ci
python postclassifier.py -v -n age -i ci --load --test 0 --apply "$INPUT"
echo race-ci
python postclassifier.py -v -n race -i ci --load --test 0 --apply "$INPUT"
echo multi-ci
python postclassifier.py -v -n multi -i ci --load --test 0 --apply "$INPUT"
echo agency-ci
python postclassifier.py -v -n agency -i ci --load --test 0 --apply "$INPUT"
echo healthspa-ci
python postclassifier.py -v -n healthspa -i ci --load --test 0 --apply "$INPUT"
echo offtopic-ci
python postclassifier.py -v -n offtopic -i ci --load --test 0 --apply "$INPUT"
echo typical-ci
python postclassifier.py -v -n typical -i ci --load --test 0 --apply "$INPUT"