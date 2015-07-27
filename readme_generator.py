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

from prettytable import PrettyTable, HEADER
#from prettytable import

x = PrettyTable(["No.", "TP", "Promoter vector", "Terminator vector", "Promoter nb (or both)", "Terminator nb"])
x.align= "l"
x.hrules=HEADER
x.junction_char=" "
x.vertical_char=" "


for i,tp in enumerate(tps):
    lst = [n for n in nbs if tp in n]
    lst+= ['na'] * (2 - len(lst))
    x.add_row([i+1,
               tp,
               "[pYPKa_Z_{tp}.gb](pYPKa_Z_{tp}.gb)".format(tp=tp),
               "[pYPKa_E_{tp}.gb](pYPKa_E_{tp}.gb)".format(tp=tp)]+lst)

s+=x.get_string()
with codecs.open("README.md", "w", "utf8") as f: f.write(s.strip())

