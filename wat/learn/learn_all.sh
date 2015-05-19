#!/bin/sh

echo  age
python learnblob.py -v -s age --train 800 --test 100 --validate 100
echo  race
python learnblob.py -v -s race --train 800 --test 100 --validate 100
echo  multi
python learnblob.py -v -s multi --train 800 --test 100 --validate 100
echo  agency
python learnblob.py -v -s agency --train 800 --test 100 --validate 100
echo  healthspa
python learnblob.py -v -s healthspa --train 800 --test 100 --validate 100
echo  offtopic
python learnblob.py -v -s offtopic --train 800 --test 100 --validate 100
echo  typical
python learnblob.py -v -s typical --train 800 --test 100 --validate 100