#!/usr/bin/python3

import collections, shelve, sys, base64, json

PassInfo = collections.namedtuple('PassInfo', ['salt', 'length', 'symbols', 'id'])

def list_pinfo(path):
    db = get_db(path)
    print(json.dumps(
        {key : pinfo_to_json(db[key])
         for key in db  if key != 'senado.leg.brmsl09'}
    ))

def pinfo_to_json(pinfo):
    return {
        'length': pinfo.length,
        'symbols': pinfo.symbols,
        'id' : pinfo.id,
        'salt' : base64.b64encode(pinfo.salt).decode('utf-8')
    }

def get_db(path):
    try:
        return shelve.open(path)
    except IOError:
        print('Could not open the password info file. Please check your '
                      'permissions and try again.')
        exit(1)

if __name__ == '__main__':
    list_pinfo(sys.argv[1])
