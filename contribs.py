
# Get Contribution Count

import urllib
import datetime
import HTMLParser

class ContribParser(HTMLParser.HTMLParser):

    today = datetime.date.today().isoformat()
    
    def handle_starttag(self, tag, attrs):
        if tag == 'rect' and self.is_today(attrs):
            self.count = self.get_count(attrs)

    def is_today(self, attrs):
        for name, value in attrs:
            if name == 'data-date' and value == self.today:
                return True
        return False

    def get_count(self, attrs):
        for name, value in attrs:
            if name == 'data-count': 
                return value
        return None

def getContribs(username):
    url = 'https://github.com/users/:user/contributions'
    req = urllib.urlopen(url.replace(':user', username))
    parser = ContribParser()
    parser.feed(req.read())
    return parser.count
