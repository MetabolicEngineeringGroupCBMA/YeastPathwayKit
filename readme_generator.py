#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, codecs

files = os.listdir(".")

nbs = [f for f in files if f.lower().endswith(".ipynb")]


tps = [os.path.splitext(f[8:])[0].strip("_") for f in files if f.startswith("pYPKa_")]
tps = sorted(set(tps))

s=u"""
# Yeast pathway kit promoter and terminator vectors

This list contain a total of {no} regulatory sequences
cloned in the [pYPKa](files/pYPKa.gb) vector in either the [ZraI](http://rebase.neb.com/rebase/enz/ZraI.html)
or the [EcoRV](http://rebase.neb.com/rebase/enz/EcoRV.html) site.

![files/pYPK_ZE.png](files/pYPK_ZE.png)

Plasmids with an insert in [ZraI](http://rebase.neb.com/rebase/enz/ZraI.html) are named
pYPKa_Z_* and plasmids with an insert in [EcoRV](http://rebase.neb.com/rebase/enz/EcoRV.html) are named
pYPKa_E_*. Inserts in ZraI and EcoRV can be used as promoters and terminators, respectively.

Each vector is described py an IPython notebook.
""".format(no=len(tps))



for i,tp in enumerate(tps):
   s+= """
{i}. {tp}
 ... [pYPKa_Z_{tp}.gb](pYPKa_Z_{tp}.gb)
 ... [pYPKa_E_{tp}.gb](pYPKa_E_{tp}.gb)  """.format(tp=tp, i=i+1)

   for nb in [n for n in nbs if tp in n]:
       s+= """ ... [{nb}]({nb})  """.format(nb=nb)


with codecs.open("README.md", "w", "utf8") as f: f.write(s.strip())













if __name__ is "__main__":
    pass

