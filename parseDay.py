
import urllib
import HTMLParser

class parseCommits(HTMLParser.HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        if tag == 'rect':
            for name, value in attrs:
                if name == 'data-count': count = value
                if name == 'data-date' and value == '2015-12-29':
                    self.count = count


aparser = parseCommits()
u = urllib.urlopen('https://github.com/users/chrisfosterelli/contributions')
aparser.feed(u.read())
print("Count")
print(aparser.count)
