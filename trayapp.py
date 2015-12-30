
# Github Tray App

import urllib
import rumps
import contribparser

class GithubTrayApp(rumps.App):

    @rumps.clicked('Update')
    def onoff(self, sender):
        rumps.alert('jk! not ready yet!')

    @rumps.clicked('Change Frequency')
    def onoff(self, sender):
        rumps.alert('jk! not ready yet!')

    @rumps.clicked('Change Username')    
    def prefs(self, _):
        rumps.alert('jk! not ready yet!')

if __name__ == "__main__":
    parser = contribparser.ContribParser()
    u = urllib.urlopen('https://github.com/users/chrisfosterelli/contributions')
    parser.feed(u.read())
    print("Count")
    print(parser.count)
    GithubTrayApp('Github', icon='github.png').run()
