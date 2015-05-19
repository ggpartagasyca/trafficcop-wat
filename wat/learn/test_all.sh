#!/bin/sh

echo  age
python learnblob.py -v -l age --train 800 --test 100 --validate 100 > age.test
echo  race
python learnblob.py -v -l race --train 800 --test 100 --validate 100 > race.test
echo  multi
python learnblob.py -v -l multi --train 800 --test 100 --validate 100 > multi.test
echo  agency
python learnblob.py -v -l agency --train 800 --test 100 --validate 100 > agency.test
echo  healthspa
python learnblob.py -v -l healthspa --train 800 --test 100 --validate 100 > healthspa.test
echo  offtopic
python learnblob.py -v -l offtopic --train 800 --test 100 --validate 100 > offtopic.test
echo  typical
python learnblob.py -v -l typical --train 800 --test 100 --validate 100 > typical.test