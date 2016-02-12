
# Get Contribution Count

import urllib
import datetime
import HTMLParser

class ContribParser(HTMLParser.HTMLParser):

    def __init__(self):
        self.today = datetime.date.today().isoformat()
        HTMLParser.HTMLParser.__init__(self)

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

def get_contribs(username):
    url = 'https://github.com/users/:user/contributions'
    req = urllib.urlopen(url.replace(':user', username))
    if req.getcode() == 404: raise ValueError('No such user')
    parser = ContribParser()
    parser.feed(req.read())
    return parser.count
