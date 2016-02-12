
# Github Tray App

import rumps
import config
import contribs

class GithubTrayApp(rumps.App):

    red_icon = 'github0.png'
    black_icon = 'github.png'

    def __init__(self):
        super(GithubTrayApp, self).__init__('Github')
        self.count = rumps.MenuItem('Contributions: N/A')
        self.username = config.get_username()
        self.menu = [ 
            self.count, 
            'Update Now', 
            rumps.separator,
            'Change Frequency', 
            'Change Username' 
        ]
        self.update()

    def fetch(self):
        try: 
            num = str(contribs.get_contribs(self.username))
            self.icon = self.red_icon if num == '0' else self.black_icon
            self.count.title = 'Contributions: ' + num
        except ValueError as e:
            self.icon = self.red_icon
            self.count.title = 'Invalid username'
        except IOError as e:
            self.icon = self.red_icon
            self.count.title = 'No internet'
        except Exception as e: print(e)

    def show_username_error(self):
        self.count.title = 'No Username Set'
        self.icon = self.red_icon

    def update(self):
        print('Updating count')
        print(self.username)
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
    def change_username(self, _):
        window = rumps.Window(dimensions = (100, 23))
        window.message = 'Enter your Github username'
        window.icon = 'github.png'
        window.title = 'Username'
        self.username = window.run().text
        config.set_username(self.username)
        self.update()

if __name__ == '__main__':
    GithubTrayApp().run()
