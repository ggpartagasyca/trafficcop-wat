
from HTMLParser import HTMLParser

class HTMLTextExtractor(HTMLParser):

    def __init__(self):
        self.buffer = []
        # this works only for new-style class
        # super(HTMLShedder,self).__init__()
        HTMLParser.__init__(self)
    def handle_data(self, data):
        if data:
            self.buffer.append(data)
    # def handle_endtag(self,tag):
    #     if tag == "br" or tag in blockLevelElements:
    #         self.buffer.append(" ")

TEST="""<img title='Ottawa Senators owner Eugene Melnyk reacts to media questions regarding the NHL team&#39;s failure to make the 2008-2009 playoffs at Scotiabank Place in Ottawa on Wednesday, April 8, 2009. Melnyk is looking for consistency.Like many, the Senators owner had high hopes for the team this season, and he admits to being disappointed at the team&#39;s current state.' height='259' alt='HKN Senators Melnyk' width='460' src='http://i.cbc.ca/1.2474721.1431631261!/fileImage/httpImage/image.jpg_gen/derivatives/16x9_460/hkn-senators-melnyk.jpg' /> <p>Ottawa Senators owner Eugene Melnyk needs an urgent liver transplant after battling major health issues since January, and the team is appealing to the public for help.</p>"""

class HTMLImageExtractor(HTMLParser):

    def __init__(self):
        self.images = []
        # this works only for new-style class
        # super(HTMLShedder,self).__init__()
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if tag == 'img':
            src = attributes.get("src", None)
            if src:
                self.images.append(src)
    def handle_startendtag(self, tag, attributes):
        return self.handle_starttag(tag, attributes)
    # def handle_endtag(self,tag):
    #     if tag == "br" or tag in blockLevelElements:
    #         self.images.append(" ")
        
def extract_text(html):
    parser = HTMLTextExtractor()
    parser.feed(html)
    output = " ".join(parser.buffer)
    parser.close()
    return output

def extract_images(html):
    parser = HTMLImageExtractor()
    parser.feed(html)
    output = "\t".join(parser.images)
    parser.close()
    return output
    
