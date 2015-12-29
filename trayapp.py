
# Github Tray App

import rumps

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
     GithubTrayApp('Github', icon='github.png').run()
