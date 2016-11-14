#!/usr/bin/python3

import collections, shelve, sys

PassInfo = collections.namedtuple('PassInfo', ['salt', 'length', 'symbols', 'id'])

def list_pinfo(path):
    db = get_db(path)
    print('Starting')
    for key in db:
        try:
            print(key, db[key])
        except AttributeError:
            print('Could not retrieve', key)

def get_db(path):
    try:
        return shelve.open(path)
    except IOError:
        print('Could not open the password info file. Please check your '
                      'permissions and try again.')
        exit(1)

if __name__ == '__main__':
    list_pinfo(sys.argv[1])
