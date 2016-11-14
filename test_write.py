import shelve, sys, os.path
#Find the dir where this script is in
dir_path = os.path.dirname(sys.argv[0])
# Find the current version and save the database with the current version in
# the name
vi = sys.version_info
rel_path = 'file{}.{}.{}'.format(vi.major, vi.minor, vi.micro)
abs_path = os.path.join(dir_path, rel_path)
db = shelve.open(abs_path)
db['foo']='bar'
db.sync()
