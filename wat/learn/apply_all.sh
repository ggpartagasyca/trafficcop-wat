#!/bin/sh

# INPUT='Welcome to Paradise Spa'
# echo healthspa-default
# python postclassifier.py -v --name healthspa -i default --load --test 0 --apply "$INPUT"


INPUT='<html><body>No black men please</body></html>'
echo race-default
python postclassifier.py -v --name race -i ci --load --test 0 --type html --apply "$INPUT"

exit


echo age-cs
python postclassifier.py -v --name age -i cs --load --test 0 --apply "$INPUT"
# echo race-cs
# python postclassifier.py -v --name race -i cs --load --test 0 --apply "$INPUT"
# echo multi-cs
# python postclassifier.py -v --name multi -i cs --load --test 0 --apply "$INPUT"
# echo agency-cs
# python postclassifier.py -v --name agency -i cs --load --test 0 --apply "$INPUT"
echo healthspa-cs
python postclassifier.py -v --name healthspa -i cs --load --test 0 --apply "$INPUT"
# echo offtopic-cs
# python postclassifier.py -v --name offtopic -i cs --load --test 0 --apply "$INPUT"
# echo typical-cs
# python postclassifier.py -v --name typical -i cs --load --test 0 --apply "$INPUT"

# echo age-ci
# python postclassifier.py -v --name age -i ci --load --test 0 --apply "$INPUT"
# echo race-ci
# python postclassifier.py -v --name race -i ci --load --test 0 --apply "$INPUT"
# echo multi-ci
# python postclassifier.py -v --name multi -i ci --load --test 0 --apply "$INPUT"
# echo agency-ci
# python postclassifier.py -v --name agency -i ci --load --test 0 --apply "$INPUT"
# echo healthspa-ci
# python postclassifier.py -v --name healthspa -i ci --load --test 0 --apply "$INPUT"
# echo offtopic-ci
# python postclassifier.py -v --name offtopic -i ci --load --test 0 --apply "$INPUT"
# echo typical-ci
# python postclassifier.py -v --name typical -i ci --load --test 0 --apply "$INPUT"