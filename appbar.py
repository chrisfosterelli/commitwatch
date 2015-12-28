import rumps

class AwesomeStatusBarApp(rumps.App):

    @rumps.clicked('Enable')
    def onoff(self, sender):
        sender.state = not sender.state

    @rumps.clicked('Username')    
    def prefs(self, _):
        rumps.alert('jk! not ready yet!')

if __name__ == "__main__":
     AwesomeStatusBarApp('Github', icon='github.png').run()
