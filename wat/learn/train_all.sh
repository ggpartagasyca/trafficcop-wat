#!/bin/sh

echo age-cs
python postclassifier.py -v -s age -i cs --train 800 --test 100 --validate 100
echo race-cs
python postclassifier.py -v -s race -i cs --train 800 --test 100 --validate 100
echo multi-cs
python postclassifier.py -v -s multi -i cs --train 800 --test 100 --validate 100
echo agency-cs
python postclassifier.py -v -s agency -i cs --train 800 --test 100 --validate 100
echo healthspa-cs
python postclassifier.py -v -s healthspa -i cs --train 800 --test 100 --validate 100
echo offtopic-cs
python postclassifier.py -v -s offtopic -i cs --train 800 --test 100 --validate 100
echo typical-cs
python postclassifier.py -v -s typical -i cs --train 800 --test 100 --validate 100

echo age-ci
python postclassifier.py -v -s age -i ci --train 800 --test 100 --validate 100
echo race-ci
python postclassifier.py -v -s race -i ci --train 800 --test 100 --validate 100
echo multi-ci
python postclassifier.py -v -s multi -i ci --train 800 --test 100 --validate 100
echo agency-ci
python postclassifier.py -v -s agency -i ci --train 800 --test 100 --validate 100
echo healthspa-ci
python postclassifier.py -v -s healthspa -i ci --train 800 --test 100 --validate 100
echo offtopic-ci
python postclassifier.py -v -s offtopic -i ci --train 800 --test 100 --validate 100
echo typical-ci
python postclassifier.py -v -s typical -i ci --train 800 --test 100 --validate 100

echo age-default
python postclassifier.py -v -s age -i default --train 800 --test 100 --validate 100
echo race-default
python postclassifier.py -v -s race -i default --train 800 --test 100 --validate 100
echo multi-default
python postclassifier.py -v -s multi -i default --train 800 --test 100 --validate 100
echo agency-default
python postclassifier.py -v -s agency -i default --train 800 --test 100 --validate 100
echo healthspa-default
python postclassifier.py -v -s healthspa -i default --train 800 --test 100 --validate 100
echo offtopic-default
python postclassifier.py -v -s offtopic -i default --train 800 --test 100 --validate 100
echo typical-default
python postclassifier.py -v -s typical -i default --train 800 --test 100 --validate 100
