import sqlite3 as db
import sys
import json
from pprint import pprint

json_data = open('../crawler/data/vice_data.json')
data = json.load(json_data)
pprint(data)
json_data.close()

con = None

try:
    con = db.connect('podcasts.db')
    cur = con.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLITE version: %s" % data

except db.Error, e:

    print "Error %s" % e.args[0]
    sys.exit(1)

finally:
  if con:
      con.close()


