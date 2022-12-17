#!/usr/bin/python3

from recoll import recoll

db = recoll.connect()
query = db.query()
nres = query.execute("filename:pYPKa_Z_*.gb")
results = query.fetchmany(2000)
for doc in results:
    print("%s %s" % (doc.url, doc.title))
