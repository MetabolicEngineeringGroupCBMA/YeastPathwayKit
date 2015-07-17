#!/home/bjorn/anaconda/envs/bjorn/bin/python
# -*- coding: utf-8 -*-
import os, sys

d = os.path.dirname(os.path.realpath(sys.argv[0]))

try:
   pyfiles = [ sys.argv[1] ]
except IndexError:
   pyfiles = [f for f in os.listdir(d) if (f.endswith(".py") and f!="notebookifier.py" and f!="pythonifier.py")]

print pyfiles
  
import IPython.nbformat.current as nbf

for pf in pyfiles:
    name, ext = os.path.splitext(pf)
    new_name =  os.path.join(name+"."+"ipynb")
    if os.path.exists(new_name):
        continue
    print new_name
    nb = nbf.read(open(pf, 'r'), 'py')
    nbf.write(nb, open(new_name, 'w'), 'ipynb')
    


a=raw_input("return")
