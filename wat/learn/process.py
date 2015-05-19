#!/usr/bin/python

import json, codecs
from collections import defaultdict

def canonTags(tags):
    s = set()
    for t in tags.split(','):
        s.add(t)
    s = list(s)
    s.sort()
    return s

def canonUri(uri):
    if uri.startswith('http://localhost'):
        return uri
    else:
        return 'http://localhost/watsortdesk/data/backpage/20150201/' + uri[7:]
    return uri

def canonTitle(title):
    return title

INPUT = "/Users/philpot/project/wat/branches/dig-18/wat/learn/dat/bookmarks/bookmarks-2015-04-26.json"
INPUT = "/Users/philpot/project/wat/branches/dig-18/wat/learn/dat/bookmarks/bookmarks-2015-04-28.json"
INPUT = "/Users/philpot/project/wat/branches/dig-18/wat/learn/dat/bookmarks/bookmarks-2015-04-29.json"
with open(INPUT, 'r') as f:
    j = json.load(f)

bytag=defaultdict(set)
rows=[]
for c1 in j["children"]:
    if c1['title'] == 'Bookmarks Toolbar':
        for c2 in c1['children']:
            if c2['title'] == 'wat annot escort 01':
                for c3 in c2['children']:
                    uri = canonUri(c3['uri'])
                    tags = canonTags(c3['tags'])
                    title = canonTitle(c3['title'])
                    row = (uri, ','.join(tags), title)
                    rows.append(row)
                    for tag in tags:
                        bytag[tag].add(uri)
                    if not tags:
                        print "uri %s had no tags" % (uri)
                    if len(tags)>1:
                        print "uri %s had %s tags" % (uri, len(tags))

with codecs.open("all_ads.tsv", 'w', encoding="utf-8") as f:
    for row in rows:
        print >> f, '''"%s"\t"%s"\t"%s"''' % row

print "%s total ads annotated" % len(rows)

total_tags = 0
for tag in bytag.keys():
    k = 0
    with codecs.open("%s.tsv" % tag, 'w', encoding="utf-8") as f:
        for uri in bytag[tag]:
            print >> f, uri
            k += 1
            total_tags += 1
    print "%s ads marked %s" % (k, tag)
print "%s total tags applied" % (total_tags)



