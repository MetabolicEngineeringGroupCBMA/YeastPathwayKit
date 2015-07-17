#!/usr/bin/env python
# -*- coding: utf-8 -*-

tps='''ScRPE1 557 556 NM_001181554.1
       ScRKI1 555 554 NM_001183514.1'''

tps='''ScALD6 527 528 BK006949.2 REGION: 432587..434090'''

tps='''ScALD6 527 528 BK006949.2 REGION: 432587..434090'''


from Bio.Restriction import AjiI

enz = AjiI

t='''
# pYPKa_{letter}_{insert}
###Freezer ID
    Strain#..: ?
    Box......: ?
    Position.: ?

Importing the [pydna](https://pypi.python.org/pypi/pydna/) package.
Pydna is [open source](https://github.com/BjornFJohansson/pydna), documentated [here](http://pydna.readthedocs.org/en/latest/) and has a support [forum](https://groups.google.com/forum/#!forum/pydna) as well as a publication:

[Pereira F, Azevedo F, Carvalho Â, Ribeiro GF, Budde MW, Johansson B: Pydna: a simulation and documentation tool for DNA assembly strategies using python. BMC Bioinformatics 2015, 16:142.](http://www.biomedcentral.com/1471-2105/16/142/abstract)

    import pydna
    from pydna import ipynb_importer

Read the cloning vector from a local file.

    pYPKa = pydna.read("pYPKa.gb")

This vector should be a circular 3128 bp DNA molecule.

     pYPKa

The circular seguid checksum of pYPKa should be

```aV1eIrzOiCjvw01yvKkxDXHKLMk```

    pYPKa.cseguid()

Importing the restriction enzyme to be used for cloning from Biopython.

    from Bio.Restriction import {enz}

With the recognition site

    print {enz}.site

This enzyme should cut only once in pYPKa.

    pYPKa.cut({enz})

pYPKa is digested with {enz} to form a linear DNA fragment.

    pYPKa_{enz} = pYPKa.linearize({enz})

The insert comes from a Genbank [record](http://www.ncbi.nlm.nih.gov/nuccore/{gblink}).
Access to Genbank is needed in order to download the template.
If you execute this script, change the email address below to your own.
Always tell Genbank who you are, when using the service.

    gb = pydna.Genbank("myemail@home.se")

The template is downloaded from Genbank below.

    template = gb.nucleotide("{gbref}")

The template length and a representation:

    print len(template)
    print str(template.seq)

The seguid checksum of the template should be

```{insertseguid}```


Two primers are used to amplify the insert:

    f,r = pydna.parse(""">{fpn}
                          {fps}
                         >{rpn}
                          {rps}""", ds=False)

    insert = pydna.pcr(f, r, template)

The primers anneal on the template like this.

    insert.figure()

A recombinant plasmid is formed by ligating the insert PCR product to the linear vector.

    plasmid = (pYPKa_{enz} + insert).looped()

The plasmid sequence is rotated so that the origin is in the same position as for the cloning vector sequence.

    pYPKa_{letter}_{insert} = plasmid.synced(pYPKa)

Stamp sequence with cSEGUID checksum

    pYPKa_{letter}_{insert}.stamp()

Write sequence to a local file.

    pYPKa_{letter}_{insert}.write("pYPKa_{letter}_{insert}.gb")

Calculate cseguid:

    pYPKa_{letter}_{insert}.cseguid()

### Download

[pYPKa_{letter}_{insert}](pYPKa_{letter}_{insert}.gb)

    import pydna

    pYPKa_{letter}_{insert} = pydna.read("pYPKa_{letter}_{insert}.gb")

    pYPKa_{letter}_{insert}.verify_stamp()

'''





import subprocess

from pydna_helper import load_my_primers as lp

from pygenome import sg

for insertname, pf, pr, gbref in (x.split(None, 3) for x in tps.split("\n")):

    fp = lp.primer[int(pf)]
    rp = lp.primer[int(pr)]

    insertseguid = "insertseguid"

    gblink = gbref.split()[0]

    r =  t.format( letter=repr(enz)[0],
                   insert=insertname,
                   enz=repr(enz),
                   gbref = gbref,
                   gblink =gblink,
                   insertseguid = insertseguid,
                   fpn=fp.name,
                   fps=fp.seq,
                   rpn=rp.name,
                   rps=rp.seq )

    newfn = "pYPKa_{}_{}".format(repr(enz)[0],insertname)

    with open("."+newfn+".md", "w") as f: f.write(r)

    cmd = "/home/bjorn/anaconda/envs/bjorn/bin/notedown .{n}.md > {n}.ipynb".format(n=newfn)

    print subprocess.check_output(cmd, shell=True)
    print newfn+".ipynb"
