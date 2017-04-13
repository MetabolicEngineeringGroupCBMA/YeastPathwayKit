#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydna.myprimers import primer_list as lp
from pydna.dseqrecord import Dseqrecord
from pydna.amplify import pcr
from Bio.Restriction import ZraI, EcoRV
from pygenome import sg
import nbformat
from nbconvert.preprocessors.execute import ExecutePreprocessor
import notedown
from pydna.readers import read
pYPKa = read("pYPKa.gb")
with open("pYPKa_ZE_template.md", "r", encoding="utf8") as f:
    t=f.read()
with open("TP List.txt", "r") as f:
    tps = f.readlines()
    
tp_dict = {}

for letter, insertname, pf, pr, status in (x.split() for x in tps if x):
    
    try:
        old = tp_dict[insertname]
    except KeyError:
        tp_dict[insertname] = (pf, pr, status)
    else:
        assert (old[0], old[1]) == (pf, pr)

for insertname in sorted(tp_dict):
    pf, pr, status = tp_dict[insertname]
    print(insertname, pf, pr, status)

    fp = lp[int(pf)]
    rp = lp[int(pr)]

    gbref  = sg.gene[insertname].promoter.description
    gblink = sg.gene[insertname].cds.id

    template = Dseqrecord(sg.gene[insertname].promoter)

    templatesize = len(template)
    insertseguid = template.seguid()

    finalcseguidZ = (pYPKa.linearize(ZraI)+pcr(fp, rp, template)).looped().cseguid()
    finalcseguidE = (pYPKa.linearize(EcoRV)+pcr(fp, rp, template)).looped().cseguid()

    content =  t.format( tp                = insertname,
                         gbref             = gbref,
                         gblink            = gblink,
                         templatesize      = templatesize,
                         insertseguid      = insertseguid,
                         finalcseguidZ     = finalcseguidZ,
                         finalcseguidE     = finalcseguidE,
                         fpn=fp.name,
                         fps=fp.seq,
                         rpn=rp.name,
                         rps=rp.seq)

    newname = "pYPKa_ZE_{}.ipynb".format(insertname)
    
    obj = notedown.MarkdownReader()
    
    #nb = nbformat.write(obj.to_notebook(content), newname)
    nb = obj.to_notebook(content)
    
    pp = ExecutePreprocessor(timeout=600, kernel_name='python3')
    pp.timeout = 120 # seconds
    pp.interrupt_on_timeout = True

    pp.preprocess(nb, resources={})
    
    with open(newname, 'wt') as f:
        nbformat.write(nb, f)