#!/bin/sh

echo  age
python postclassifier.py -v -l age --train 800 --test 100 --validate 100 > age.test
# echo  race
# python postclassifier.py -v -l race --train 800 --test 100 --validate 100 > race.test
# echo  multi
# python postclassifier.py -v -l multi --train 800 --test 100 --validate 100 > multi.test
# echo  agency
# python postclassifier.py -v -l agency --train 800 --test 100 --validate 100 > agency.test
# echo  healthspa
# python postclassifier.py -v -l healthspa --train 800 --test 100 --validate 100 > healthspa.test
# echo  offtopic
# python postclassifier.py -v -l offtopic --train 800 --test 100 --validate 100 > offtopic.test
# echo  typical
# python postclassifier.py -v -l typical --train 800 --test 100 --validate 100 > typical.test