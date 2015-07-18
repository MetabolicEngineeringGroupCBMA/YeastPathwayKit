#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, codecs


files = os.listdir(os.path.dirname(__file__))

nbs = [f for f in files if f.lower().endswith(".ipynb")]


tps = [os.path.splitext(f[8:])[0].strip("_") for f in files if f.startswith("pYPKa_")]
tps = sorted(set(tps))

s=u"""
# Yeast pathway kit promoter and terminator vectors

pYPKa_Z_* = promoter vector
pYPKa_E_* = terminator vector
"""



for tp in tps:
   s+= """
###{tp}
[pYPKa_Z_{tp}.gb](pYPKa_Z_{tp}.gb)
[pYPKa_E_{tp}.gb](pYPKa_E_{tp}.gb)\n""".format(tp=tp)

   for nb in [n for n in nbs if tp in n]:
       s+= "[{nb}]({nb})\n".format(nb=nb)


with codecs.open("README.md", "w", "utf8") as f: f.write(s.strip())













if __name__ is "__main__":
    pass

