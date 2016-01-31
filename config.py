
# Get configuration values

from os.path import expanduser

name = '~/.commitwatch'

def get_username():
    path = expanduser(name)
    try: config_file = open(path)
    except IOError: return None
    username = config_file.read()
    username = username[:-1]
    config_file.close()
    return username

def set_username(username):
    path = expanduser(name)
    print(username)
    try: config_file = open(path, 'w')
    except IOError: return None
    config_file.write(username + '\n')
    config_file.close()
