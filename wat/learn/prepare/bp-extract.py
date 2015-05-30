#!/usr/bin/python

import re, sys, os
from bs4 import BeautifulSoup
import simplejson as json
import argparse
from htmltoken import tokenize
import cgi
import util
import io

def genescaped(text):
    """All tokens in TEXT with any odd characters (such as <>&) encoded using HTML escaping"""
    for tok in tokenize(text, interpret=cgi.escape):
        yield tok

def isValidFileArg(parser, arg):
    """ensure arg (string) is an existing, readable input file"""
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        # return open(arg, 'r')  # return an open file handle
        return arg

def pathname2soup(pathname):
    with io.open(pathname, 'r', encoding='UTF-8') as f:
        return BeautifulSoup(f)

def find_location(soup):
    posting = soup.find("div", attrs={"class": "posting"})
    for location in posting.find_all("div", attrs={"style": "padding-left:2em;"}):
        m = re.search("Location:\s+(.*)", location.text)
        if m:
            return m.group(1).strip()
    return None

def find_post_id(soup):
    posting = soup.find("div", attrs={"class": "posting"})
    for post_id in posting.find_all("div", attrs={"style": "padding-left:2em;"}):
        m = re.search("Post ID:\s+(\d+)", post_id.text)
        if m:
            return m.group(1).strip()
    return None

def find_title(soup):
    try:
        h1 = soup.find("h1")
        return h1.text.strip()
    except:
        pass
    return None

def find_title_html(soup):
    try:
        h1 = soup.find("h1")
        return unicode(h1)
    except:
        pass
    return None

def find_posting_date(soup):
    for postDate in soup.find_all("div", attrs={"class": "adInfo"}):
        m = re.search("Posted:\s+(.*)", postDate.text)
        if m:
            return m.group(1).strip()
    return None

def find_cookie_crumb(soup):
    for crumb in soup.find_all("div", attrs={"id": "cookieCrumb"}):
        return crumb.text
    return None

def find_body(soup):
    return soup.find("div", attrs={"class": "postingBody"})

def find_body_html(soup):
    body = find_body(soup)
    return unicode(body)

def find_images(soup):
    images = []
    body = find_body(soup)
    for img in body.find_all("img"):
        images.append(img["src"])
    return images


def extend_json(j, verbose=True):
    soup = BeautifulSoup(j["full_page_text"])
    location = find_location(soup) or ""
    title = find_title(soup) or ""
    posting_date = find_posting_date(soup) or ""
    post_id = find_post_id(soup) or ""
    cookie_crumb = find_cookie_crumb(soup) or ""
    body_html = find_body_html(soup) or ""
    images = find_images(soup) or []
    j["location"] = location
    j["title"] = title
    j["posting_date"] = posting_date
    j["post_id"] = post_id
    j["cookie_crumb"] = cookie_crumb
    j["body_html"] = body_html
    j["images"] = images
    if verbose:
        print "Location %r, Title %r, Posting Date %r, Post ID %r, Cookie Crumb %r, Body HTML %r, Images %r" % (location, title, posting_date, post_id, cookie_crumb, body_html, images)
    return j

# f= e(j())

def extract_all(verbose=False, printEvery=1000):
    i = 0
    with open('backpage-20150414-scrapy-extracted.json', 'w') as outfile:
        with open('backpage-20150414-scrapy', 'r') as infile:
            for line in infile:
                try:
                    j = json.loads(line)
                    j2 = extend_json(j, verbose=verbose)
                    json.dump(j2, outfile)
                    print >> outfile
                except Exception as e:
                    print e
                    print "ignoring"
                i +=1
                if i % printEvery == 0:
                    print i
            
class Extractor():
    def __init__(self, pathname, extractBody=None, extractTitle=None, verbose=False):
        self.pathname = pathname
        self.extractBody = extractBody
        self.extractTitle = extractTitle
        self.verbose = verbose

    def adaptPathname(self, extension):
        return self.pathname + "__" + extension

    def process(self):
        self.soup = pathname2soup(self.pathname)
        try:
            if self.extractTitle:
                self.title = [tok for tok in genescaped(find_title_html(self.soup))]
                with io.open(self.adaptPathname("title.tok"), 'w', encoding='UTF-8') as f:
                    for tok in self.title:
                        f.write(tok)
                        f.write(u'\n')
            if self.extractBody:
                self.body = [tok for tok in genescaped(find_body_html(self.soup))]
                with io.open(self.adaptPathname("body.tok"), 'w', encoding='UTF-8') as f:
                    for tok in self.body:
                        f.write(tok)
                        f.write(u'\n')
        except TypeError as te:
            print "Problem with %s [%r]" % (self.pathname, te)

def main(argv=None):
    '''this is called if run from command line'''
    parser = argparse.ArgumentParser()
    parser.add_argument("pathname", help='input backpage HTML file', type=lambda x: isValidFileArg(parser, x))
    parser.add_argument('-b','--body', required=False, help='verbose', action='store_true')
    parser.add_argument('-t','--title', required=False, help='verbose', action='store_true')
    parser.add_argument('-v','--verbose', required=False, help='verbose', action='store_true')
    args=parser.parse_args()

    pathname = args.pathname
    extractBody = args.body
    extractTitle = args.title
    verbose = args.verbose
    e = Extractor(pathname, extractBody=extractBody, extractTitle=extractTitle, verbose=verbose)
    e.process()

# call main() if this is run as standalone
if __name__ == "__main__":
    sys.exit(main())
