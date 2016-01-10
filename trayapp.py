
# Github Tray App

import rumps
import contribs

username = 'chrisfosterelli'

class GithubTrayApp(rumps.App):

    @rumps.clicked('Update')
    def onoff(self, sender):
        count = contribs.getContribs(username)
        self.title = str(count)

    @rumps.clicked('Change Frequency')
    def onoff(self, sender):
        rumps.alert('jk! not ready yet!')

    @rumps.clicked('Change Username')    
    def prefs(self, _):
        rumps.alert('jk! not ready yet!')

if __name__ == "__main__":
    count = contribs.getContribs(username)
    GithubTrayApp('Github', icon='github.png', title=str(count)).run()
