#!/bin/sh

echo  age
python learnblob.py -i ci -v -s age --train 800 --test 100 --validate 100 > age_ci.test
echo  race
python learnblob.py -i ci -v -s race --train 800 --test 100 --validate 100 > race_ci.test
echo  multi
python learnblob.py -i ci -v -s multi --train 800 --test 100 --validate 100 > multi_ci.test
echo  agency
python learnblob.py -i ci -v -s agency --train 800 --test 100 --validate 100 > agency_ci.test
echo  healthspa
python learnblob.py -i ci -v -s healthspa --train 800 --test 100 --validate 100 > healthspa_ci.test
echo  offtopic
python learnblob.py -i ci -v -s offtopic --train 800 --test 100 --validate 100 > offtopic_ci.test
echo  typical
python learnblob.py -i ci -v -s typical --train 800 --test 100 --validate 100 > typical_ci.test