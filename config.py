
# Get configuration values

from os.path import expanduser

name = '~/.commitwatch'

def get_username():
    path = expanduser(name)
    config_file = open(path)
    username = config_file.read()
    username = username[:-1]
    config_file.close()
    return username
