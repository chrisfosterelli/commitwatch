
# Github Tray App

import rumps
import config
import contribs

class GithubTrayApp(rumps.App):

    red_icon = 'github0.png'
    black_icon = 'github.png'

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
        self.update()

    def fetch(self):
        try: 
            num = str(contribs.get_contribs(self.username))
            self.icon = self.red_icon if num == '0' else self.black_icon
            self.count.title = num + ' commits'
        except Exception as e: print(e)

    def show_username_error(self):
        self.count.title = 'No Username Set'
        self.icon = self.red_icon

    def update(self):
        print('Updating count')
        if self.username != None: self.fetch()
        else: self.show_username_error()

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
