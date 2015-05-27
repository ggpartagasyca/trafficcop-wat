#!/usr/bin/python
# Filename: wattok.py

'''
wat.tool.wattok
@author: Andrew Philpot
@version 1.5

Usage: python wattok.py <file>
'''

import sys
import nltk
import re
import pymod.util

VERSION = '1.5'
__version__ = VERSION
REVISION = "$Revision: 25451 $".replace("$","")

class Tokenizer(object):
    def __init__(self, input):
        '''create Wattok'''        
        self.input = input

    # MODEL
    # property attribute text
    def derive_text(self):
        try:
            # text = pymod.util.slurpAsciiEntitified(self.input)
            text = self.input
        except IOError:
            text = self.input
        return text
    @property
    def text(self):
        """I'm the 'text' property."""
        if not hasattr(self, '_text'):
            self._text = self.derive_text()
        return self._text
    @text.setter
    def text(self, value):
        self._text = value
    @text.deleter
    def text(self):
        del self._text

    # compiling here wrecks the re.sub in genTokens
    # entityRE = re.compile(r"(?:&#\d{2,5};|&gt;|&lt;|&quot;|&apos;)")
    entityRE = r"(?:&#\d{2,5};|&gt;|&lt;|&quot;|&apos;)"
    # so don't know if we can ever use this
    # compiledEntityRe = re.compile(entityRE)

    # digitRE = re.compile(r"\d")

    # need maximal segments of &#\d{2,4};\s* 
    def genSegments(self, s):
        while len(s) > 0:
            m = re.search(r"\s*%s(?:\s*%s)*" % (Tokenizer.entityRE, Tokenizer.entityRE), s)
            if m:
                if m.start(0) == 0:
                    yield (True, m.group(0))
                    s = s[m.end(0):]
                else:
                    yield (False, s[0:m.start(0)])
                    yield (True, m.group(0))
                    s = s[m.end(0):]
            else:
                yield (False, s)
                s = ""

    def genTokens0(self):
        # use the new property
        string = self.text
        # set off w/space any entities that are butted up to preceding data
        # print "sub %r with %r in %r" % (r'(?<!\s)(?P<entityref>%s)' % Tokenizer.entityRE, 
        #                                 ' \g<entityref>',
        #                                 string)
        string = re.sub(r'(?<!\s)(?P<entityref>%s)' % Tokenizer.entityRE, 
                      ' \g<entityref>',
                      string)
        # set off w/space any entities that are butted up to following data
        string = re.sub(r'(?P<entityref>%s)(?!\s)' % Tokenizer.entityRE,
                      '\g<entityref> ',
                      string)
        for (entities, segment) in self.genSegments(string):
            # print "SEGMENT: [%s %r]" % (entities,segment)
            segment = segment.strip()
            if entities:
                for entity in re.split(r'\s+',segment):
                    # print " ENTITY: [%s]" % entity;
                    yield entity
            else:
                sentences = nltk.sent_tokenize(segment)
                # correct for any embedded newlines (irrelevant?)
                sentences = [re.sub(r'[\n\t]+', ' ', sent).strip() for sent in sentences]
                # inexplicably, NLTK thinks big,red should be a single token
                sentences = [re.sub(r'\b,\b', ', ', sent) for sent in sentences]
                for sentence in sentences:
                    # print "  SENTENCE: [%s]" % sentence
                    for tok in nltk.word_tokenize(sentence):
                        # print "    TOK: [%s]" % tok
                        yield tok
        
    # Some imperfect tokens created by above tokenizer joining at '.':
    # dirty.This
    # DAYS.......
    # But we would want to retain as single tokens:
    # 1.25
    # www.backpage.com
    # J.U.L.I.E (ideally)
    #
    # Propose:
    # If token contains period:
    #    If token contains two or more periods in a row:
    #       split at each group of 2+ periods, then call recursively on each segment
    #    Else if token contains digits:
    #       yield it
    #    Else if token contains ".com" (etc.) and/or "http" and/or "www"
    #       yield it
    #    Else split at each period    

    ellipsisRE = re.compile(r'''(.*?)(\.{2,})''')
    allperiodsRE = re.compile(r'''^\.+$''')
    digitsRE = re.compile('\d')
    urlRE = re.compile('.com|.net|.org|.xxx|.biz|.edu|.info|www|http')
    periodRE = re.compile('(.*?)(\.)')

    def genTokens(self):
        # use the new property
        string = self.text
        # set off w/space any entities that are butted up to preceding data
        string = re.sub(r'(?<!\s)(?P<entityref>%s)' % Tokenizer.entityRE, 
                        ' \g<entityref>',
                        string)
        # set off w/space any entities that are butted up to following data
        string = re.sub(r'(?P<entityref>%s)(?!\s)' % Tokenizer.entityRE,
                        '\g<entityref> ',
                        string)
        for (entities, segment) in self.genSegments(string):
            # print "SEGMENT: [%s %r]" % (entities,segment)
            segment = segment.strip()
            if entities:
                for entity in re.split(r'\s+',segment):
                    # print " ENTITY: [%s]" % entity;
                    yield entity
            else:
                sentences = nltk.sent_tokenize(segment)
                # correct for any embedded newlines (irrelevant?)
                sentences = [re.sub(r'[\n\t]+', ' ', sent).strip() for sent in sentences]
                # inexplicably, NLTK thinks big,red should be a single token
                sentences = [re.sub(r'\b,\b', ', ', sent) for sent in sentences]
                for runon in sentences:
                    for sentence in re.split(Tokenizer.ellipsisRE, runon):
                        # print "  SENTENCE: [%s]" % sentence
                        if sentence:
                            # may have some empty strings
                            if re.search(Tokenizer.allperiodsRE, sentence):
                                # may be all periods
                                yield sentence
                            else:
                                for tok in nltk.word_tokenize(sentence):
                                    # print "    TOK: [%s]" % tok
                                    if Tokenizer.digitsRE.search(tok) or Tokenizer.urlRE.search(tok):
                                        yield tok
                                    else:
                                        for subtok in re.split(Tokenizer.periodRE, tok):
                                            # may have some empty strings
                                            if subtok:
                                                yield subtok

def main(argv=None):
    '''this is called if run from command line'''
    n = Tokenizer((sys.argv and len(sys.argv)>1 and sys.argv[1]) or "/tmp/test.txt")
    # print n
    print [tok for tok in n.genTokens0()]
    print
    print [tok for tok in n.genTokens()]

# call main() if this is run as standalone
if __name__ == "__main__":
    sys.exit(main())

# End of wattok.py
