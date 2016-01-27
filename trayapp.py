
# Github Tray App

import rumps
import config
import contribs

class GithubTrayApp(rumps.App):

    def __init__(self):
        super(GithubTrayApp, self).__init__('Github')
        self.count = rumps.MenuItem('commits')
        self.username = config.get_username()
        self.menu = [ 
            self.count, 
            'Update Now', 
            'Change Frequency', 
            'Change Username' 
        ]

    def update(self):
        try: 
            print('Updating user')
            num = str(contribs.get_contribs(self.username))
            self.icon = 'github0.png' if num == '0' else 'github.png'
            self.count.title = num + ' commits'
        except Exception as e: print(e)

    @rumps.timer(60*5)
    def timer(self, _):
        self.update()

    @rumps.clicked('Update Now')
    def update_now(self, _):
        self.update()

    @rumps.clicked('Change Frequency')
    def change_frequency(_):
        rumps.alert('jk! not ready yet!')

    @rumps.clicked('Change Username')    
    def change_username(_):
        rumps.alert('jk! not ready yet!')

if __name__ == '__main__':
    GithubTrayApp().run()
