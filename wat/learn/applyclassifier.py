#!/usr/bin/python
# -*- coding: utf-8 -*-
# Filename: applyclassifier.py

'''
wat.learn.applyclassifier

Usage: python applyclassifer.py -c category -i indicator
Options:
\t-h, --help:\tprint help to STDOUT and quit
\t-v, --verbose:\tverbose output
\t-c, --category:\classifier to apply: (age, race, multi, agency, healthspa, offtopic, typical)
\t-i, --indicator:\thow to treat text: (cs, ci, default)
\t-t, --type\tfiletype (default: text)
'''

import sys
import re
from collections import defaultdict
import codecs
import pprint
import argparse
import json

from wat.tool.wattok import Tokenizer


def main(argv=None):
    '''this is called if run from command line'''
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-c','--category', required=False, 
                        help='major category of rules to apply (default: use all)')
    parser.add_argument('-f','--family', required=False,
                        help='minor category of rules to apply (default: use all)')
    parser.add_argument('-i','--indicator', required=False,
                        help='Indicate precise rule as X.Y.Z')
    parser.add_argument('-t','--type', required=False, default='text',
                        help='input file type', choices=('text', 'html'))
    parser.add_argument('-v','--verbose', required=False, help='verbose', action='store_true')
    args=parser.parse_args()

    with codecs.open(args.input, 'r', encoding='utf-8') as f:
        text = f.read()
        if args.type == 'html':
            from pymod.htmlextract import extract_text
            text = extract_text(text)

    tok = Tokenizer(text)
    tokens = [t for t in tok.genTokens()]
    result = patternScan(tokens, category=args.category, 
                         family=args.family, indicator=args.indicator)
    print >> sys.stdout, json.dumps(result, indent=4)

# call main() if this is run as standalone
if __name__ == "__main__":
    sys.exit(main())

# End of patscan.py
