
# Github Tray App

import rumps
import contribs

username = 'chrisfosterelli'

class GithubTrayApp(rumps.App):

    @rumps.timer(60*5)
    def timer(self, sender):
        count = contribs.get_contribs(username)
        self.title = str(count)

    @rumps.clicked('Update')
    def onoff(self, sender):
        count = contribs.get_contribs(username)
        self.title = str(count)

    @rumps.clicked('Change Frequency')
    def onoff(self, sender):
        rumps.alert('jk! not ready yet!')

    @rumps.clicked('Change Username')    
    def prefs(self, _):
        rumps.alert('jk! not ready yet!')

if __name__ == "__main__":
    count = contribs.get_contribs(username)
    GithubTrayApp('Github', icon='github.png', title=str(count)).run()
