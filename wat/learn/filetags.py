#!/usr/bin/python

import os
from collections import defaultdict
import io

#  see readme.txt

testUrls = [# locally served URLs
            'http://localhost/watsortdesk/data/backpage/20150201/dallas.backpage.com/FemaleEscorts/avail-nowsat-specials-for-massage-therapy-avail-now-madame-sophia-469-682-7639/29901578',
            # equivalent file location
            '/Library/WebServer/Documents/watsortdesk/data/backpage/20150201/anchorage.backpage.com/FemaleEscorts/two-for-one/3962559',
            # post-annotation experiment
            '/Users/philpot/project/wat/branches/annotate/dat/wat_annot_escort_01/watsortdesk/data/backpage/20150201/anchorage.backpage.com/FemaleEscorts/two-for-one/3962559',
            '/Users/philpot/project/wat/branches/dig-18/wat/learn/dat/wat_annot_escort_01/watsortdesk/data/backpage/20150201/anchorage.backpage.com/FemaleEscorts/two-for-one/3962559'
            ]

def canonUrl(thing):
    if thing.startswith('http://localhost'):
        return "http://" + thing[52:]
    elif thing.startswith('http://'):
        return thing
    else:
        thing = os.path.realpath(thing)
        if thing.startswith('/Users/philpot/Documents/project/wat/branches/annotate/dat/wat_annot_escort_01/watsortdesk/data/backpage'):
            return "http://" + thing[114:]
        elif thing.startswith('/Users/philpot/Documents/project/wat/branches/dig-18/wat/learn/dat/wat_annot_escort_01/watsortdesk/data/backpage'):
            return "http://" + thing[122:]
        elif thing.startswith('/Library/WebServer/Documents/watsortdesk/data/backpage/'):
            return "http://" + thing[64:]
        else:
            # assume it is an original url
            return thing

def experimentFile(thing, date='20150201'):
    url = canonUrl(thing)
    # return "/Users/philpot/Documents/project/wat/branches/annotate/dat/wat_annot_escort_01/watsortdesk/data/backpage/" + str(date) + '/' + url[7:]
    return "/Users/philpot/Documents/project/wat/branches/dig-18/wat/learn/dat/wat_annot_escort_01/watsortdesk/data/backpage/" + str(date) + '/' + url[7:]

# for testUrl in testUrls:
#     print canonUrl(testUrl)
#     print experimentFile(testUrl)
# exit(0)

TSVS = ['age.tsv',
	'agency.tsv',
	# 'dance.tsv',
	# 'employment.tsv',
	'healthspa.tsv',
	'multi.tsv',
	'offtopic.tsv',
	# 'party.tsv',
	'race.tsv',
	# 'spam.tsv',
	'typical.tsv']

filetags = defaultdict(set)

for tsv in TSVS:
    tag,_ = os.path.splitext(tsv)
    tag = tag.lstrip('.')
    with open('./data/input/tsv/' + tsv, 'r') as f:
        for url in f:
            url = canonUrl(url.strip())
            filetags[url].add(tag)

def urlBodyTokens(url):
    ef = experimentFile(url)
    bodyPath = experimentFile(url) + "__body.tok"
    with io.open(bodyPath, 'r', encoding='UTF-8') as f:
        return [s.strip() for s in f.readlines()]

def urlTitleTokens(url):
    ef = experimentFile(url)
    titlePath = experimentFile(url) + "__title.tok"
    with io.open(titlePath, 'r', encoding='UTF-8') as f:
        return [s.strip() for s in f.readlines()]

