#!/bin/sh

echo age-cs
python postclassifier.py -v -s -n age -i cs --train 800 --test 100 --validate 100
echo race-cs
python postclassifier.py -v -s -n race -i cs --train 800 --test 100 --validate 100
echo multi-cs
python postclassifier.py -v -s -n multi -i cs --train 800 --test 100 --validate 100
echo agency-cs
python postclassifier.py -v -s -n agency -i cs --train 800 --test 100 --validate 100
echo healthspa-cs
python postclassifier.py -v -s -n healthspa -i cs --train 800 --test 100 --validate 100
echo offtopic-cs
python postclassifier.py -v -s -n offtopic -i cs --train 800 --test 100 --validate 100
echo typical-cs
python postclassifier.py -v -s -n typical -i cs --train 800 --test 100 --validate 100

echo age-ci
python postclassifier.py -v -s -n age -i ci --train 800 --test 100 --validate 100
echo race-ci
python postclassifier.py -v -s -n race -i ci --train 800 --test 100 --validate 100
echo multi-ci
python postclassifier.py -v -s -n multi -i ci --train 800 --test 100 --validate 100
echo agency-ci
python postclassifier.py -v -s -n agency -i ci --train 800 --test 100 --validate 100
echo healthspa-ci
python postclassifier.py -v -s -n healthspa -i ci --train 800 --test 100 --validate 100
echo offtopic-ci
python postclassifier.py -v -s -n offtopic -i ci --train 800 --test 100 --validate 100
echo typical-ci
python postclassifier.py -v -s -n typical -i ci --train 800 --test 100 --validate 100

echo age-default
python postclassifier.py -v -s -n age -i default --train 800 --test 100 --validate 100
echo race-default
python postclassifier.py -v -s -n race -i default --train 800 --test 100 --validate 100
echo multi-default
python postclassifier.py -v -s -n multi -i default --train 800 --test 100 --validate 100
echo agency-default
python postclassifier.py -v -s -n agency -i default --train 800 --test 100 --validate 100
echo healthspa-default
python postclassifier.py -v -s -n healthspa -i default --train 800 --test 100 --validate 100
echo offtopic-default
python postclassifier.py -v -s -n offtopic -i default --train 800 --test 100 --validate 100
echo typical-default
python postclassifier.py -v -s -n typical -i default --train 800 --test 100 --validate 100
