#!/usr/bin/python3
"""docstring."""
import sys
from recoll import recoll

scriptname, *searchstring = sys.argv

searchstring, = searchstring

db = recoll.connect()
query = db.query()
nres = query.execute(searchstring)
results = query.fetchmany(2000)
for doc in results:
    print(doc.items()["filename"])


# https://docs.python.org/3/library/pickle.html
"""
>>> dir(doc)
['__class__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'get', 'getbinurl', 'items', 'keys', 'setbinurl']
>>> doc.keys
<built-in method keys of _recoll.Doc object at 0x7f5ef49ad450>
>>> doc.keys()
['url', 'sig', 'title', 'fbytes', 'abstract', 'dbytes', 'filename', 'rcludi', 'ipath', 'relevancyrating', 'fmtime', 'mtype', 'origcharset', 'mtime', 'dmtime', 'pcbytes']
>>> doc.items()
{'url': 'file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TDH3tp_FDH1_PDC1tp_pfLA_PGI1tp_pfLB_TPI1tp.zip', 'sig': '2364611559642864', 'title': '', 'fbytes': '9498', 'abstract': '', 'dbytes': '0', 'filename': 'pYPKa_Z_PGI1tp.gb', 'rcludi': '/home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TDH3tp_FDH1_PDC1tp_pfLA_PGI1tp_pfLB_TPI1tp.zip|pYPKa_Z_PGI1tp.gb', 'ipath': 'pYPKa_Z_PGI1tp.gb', 'relevancyrating': '  1%', 'fmtime': '01397753920', 'mtype': 'application/octet-stream', 'origcharset': '', 'mtime': '01385204076', 'dmtime': '01385204076', 'pcbytes': '236461'}
>>> 



{'url': 'file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TDH3tp_FDH1_PDC1tp_pfLA_PGI1tp_pfLB_TPI1tp.zip'
 'sig': '2364611559642864'
 'title': ''
 'fbytes': '9498'
 'abstract': ''
 'dbytes': '0'
 'filename': 'pYPKa_Z_PGI1tp.gb'
 'rcludi': '/home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TDH3tp_FDH1_PDC1tp_pfLA_PGI1tp_pfLB_TPI1tp.zip|pYPKa_Z_PGI1tp.gb'
 'ipath': 'pYPKa_Z_PGI1tp.gb'
 'relevancyrating': '  1%'
 'fmtime': '01397753920'
 'mtype': 'application/octet-stream'
 'origcharset': ''
 'mtime': '01385204076'
 'dmtime': '01385204076'
 'pcbytes': '236461'}


"""