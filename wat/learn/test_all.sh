#!/bin/sh

echo  age-ci
python postclassifier.py -v -l -n age -i ci --train 800 --test 100 --validate 100 > results/age-ci.test
echo  race-ci
python postclassifier.py -v -l -n race -i ci --train 800 --test 100 --validate 100 > results/race-ci.test
echo  multi-ci
python postclassifier.py -v -l -n multi -i ci --train 800 --test 100 --validate 100 > results/multi-ci.test
echo  agency-ci
python postclassifier.py -v -l -n agency -i ci --train 800 --test 100 --validate 100 > results/agency-ci.test
echo  healthspa-ci
python postclassifier.py -v -l -n healthspa -i ci --train 800 --test 100 --validate 100 > results/healthspa-ci.test
echo  offtopic-ci
python postclassifier.py -v -l -n offtopic -i ci --train 800 --test 100 --validate 100 > results/offtopic-ci.test
echo  typical-ci
python postclassifier.py -v -l -n typical -i ci --train 800 --test 100 --validate 100 > results/typical-ci.test

echo  age-cs
python postclassifier.py -v -l -n age -i cs --train 800 --test 100 --validate 100 > results/age-cs.test
echo  race-cs
python postclassifier.py -v -l -n race -i cs --train 800 --test 100 --validate 100 > results/race-cs.test
echo  multi-cs
python postclassifier.py -v -l -n multi -i cs --train 800 --test 100 --validate 100 > results/multi-cs.test
echo  agency-cs
python postclassifier.py -v -l -n agency -i cs --train 800 --test 100 --validate 100 > results/agency-cs.test
echo  healthspa-cs
python postclassifier.py -v -l -n healthspa -i cs --train 800 --test 100 --validate 100 > results/healthspa-cs.test
echo  offtopic-cs
python postclassifier.py -v -l -n offtopic -i cs --train 800 --test 100 --validate 100 > results/offtopic-cs.test
echo  typical-cs
python postclassifier.py -v -l -n typical -i cs --train 800 --test 100 --validate 100 > results/typical-cs.test

echo  age-default
python postclassifier.py -v -l -n age -i default --train 800 --test 100 --validate 100 > results/age-default.test
echo  race-default
python postclassifier.py -v -l -n race -i default --train 800 --test 100 --validate 100 > results/race-default.test
echo  multi-default
python postclassifier.py -v -l -n multi -i default --train 800 --test 100 --validate 100 > results/multi-default.test
echo  agency-default
python postclassifier.py -v -l -n agency -i default --train 800 --test 100 --validate 100 > results/agency-default.test
echo  healthspa-default
python postclassifier.py -v -l -n healthspa -i default --train 800 --test 100 --validate 100 > results/healthspa-default.test
echo  offtopic-default
python postclassifier.py -v -l -n offtopic -i default --train 800 --test 100 --validate 100 > results/offtopic-default.test
echo  typical-default
python postclassifier.py -v -l -n typical -i default --train 800 --test 100 --validate 100 > results/typical-default.test