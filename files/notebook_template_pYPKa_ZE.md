# pYPKa_Z_{tp} and pYPKa_E_{tp}

This notebook describe the construction of E. coli vectors [pYPKa_Z_{tp}](pYPKa_Z_{tp}.gb) and [pYPKa_E_{tp}](pYPKa_E_{tp}.gb)

The insert defined below is cloned in pYPKa using the blunt restriction
enzymes [ZraI](http://rebase.neb.com/rebase/enz/ZraI.html) and [EcoRV](http://rebase.neb.com/rebase/enz/EcoRV.html) in
two different plasmids. The insert cloned in ZraI will be used as a promoter, while in the EcoRV site it will be used as a
terminator.

![pYPKa_Z and pYPKa_E plasmids](pYPK_ZE.png "pYPKa_Z and pYPKa_E plasmids")

The [pydna](https://pypi.python.org/pypi/pydna/) package is imported in the code cell below.
There is a [publication](http://www.biomedcentral.com/1471-2105/16/142) describing pydna as well as
[documentation](http://pydna.readthedocs.io/) available online.
Pydna is developed on [Github](https://github.com/BjornFJohansson/pydna).

    from pydna.readers import read
    from pydna.parsers import parse_primers
    from pydna.genbank import Genbank
    from pydna.amplify import pcr
    from pydna.amplify import Anneal

The vector backbone pYPKa is read from a local [file](pYPKa.gb).

    pYPKa = read("pYPKa.gb")

Both restriction enzymes are imported from [Biopython](http://biopython.org/wiki/Main_Page)

    from Bio.Restriction import ZraI, EcoRV

The vector is cut with both enzymes.

    pYPKa_ZraI  = pYPKa.linearize(ZraI)
    pYPKa_EcoRV = pYPKa.linearize(EcoRV)

The template below comes from a Genbank [record](http://www.ncbi.nlm.nih.gov/nuccore/{gblink}).
Access to Genbank is needed in order to download the template.
If you execute this script, change the email address below to your own.
Always tell Genbank who you are, when using their web service.

    gb = Genbank("bjornjobb@gmail.com")

The template is downloaded from Genbank below.

    template = gb.nucleotide("{gbref}")

The template is a {templatesize} bp linear DNA fragment.

    template

The insert has the sequence shown below.

    print(str(template.seq))

The seguid checksum of the template should be

```{insertseguid}```

    template.seguid()

Two primers are used to amplify the insert:

    fp,rp = parse_primers(""">{fpn}
                             {fps}
                             >{rpn}
                             {rps}""")

PCR to create the insert using the primers above.

    prd = pcr(fp, rp, template)
    assert str(fp.seq) in prd

The PCR product has this length in bp.

    len(prd)

A figure of the primers annealing on template.

    prd.figure()

A suggested PCR program.

    prd.program()

The final vectors are:

    pYPKa_Z_{tp} = (pYPKa_ZraI  + prd).looped().synced(pYPKa)
    pYPKa_E_{tp} = (pYPKa_EcoRV + prd).looped().synced(pYPKa)

The final vectors with reverse inserts are created below. These vectors theoretically make up
fifty percent of the clones. The PCR strategy below is used to identify clones with the insert
in the correct orientation.

    pYPKa_Z_{tp}b = (pYPKa_ZraI  + prd.rc()).looped().synced(pYPKa)
    pYPKa_E_{tp}b = (pYPKa_EcoRV + prd.rc()).looped().synced(pYPKa)

A combination of standard primers and the primers above are
used for the strategy to identify correct clones.
Standard primers are listed [here](primers.fasta).

    p = {{ x.id: x for x in parse_primers(""">577
                                             gttctgatcctcgagcatcttaagaattc
                                             >578
                                             gttcttgtctcattgccacattcataagt
                                             >468
                                             gtcgaggaacgccaggttgcccact
                                             >467
                                             ATTTAAatcctgatgcgtttgtctgcacaga
                                             >567
                                             GTcggctgcaggtcactagtgag
                                             >568
                                             GTGCcatctgtgcagacaaacg
                                             >775
                                             gcggccgctgacTTAAAT
                                             >778
                                             ggtaaatccggatTAATTAA
                                             >342
                                             CCTTTTTACGGTTCCTGGCCT""") }}

## Diagnostic PCR confirmation

The correct structure of pYPKa_Z_{tp} is confirmed by PCR using standard primers
577 and 342 that are vector specific together with the {tp}fw primer specific for the insert
in a multiplex PCR reaction with
all three primers present.

Two PCR products are expected if the insert was cloned, the sizes depend
on the orientation. If the vector is empty or contains another insert, only one
product is formed.

#### Expected PCR products sizes from pYPKa_Z_{tp}:

pYPKa_Z_{tp} with insert in correct orientation.

    Anneal( (p['577'], p['342'], fp), pYPKa_Z_{tp}).products

pYPKa_Z_{tp} with insert in reverse orientation.

    Anneal( (p['577'], p['342'], fp), pYPKa_Z_{tp}b).products

Empty pYPKa clone.

    Anneal( (p['577'], p['342'], fp), pYPKa).products

#### Expected PCR products sizes pYPKa_E_{tp}:

pYPKa_E_{tp} with insert in correct orientation.

    Anneal( (p['577'], p['342'], fp), pYPKa_E_{tp}).products

pYPKa_E_{tp} with insert in reverse orientation.

    Anneal( (p['577'], p['342'], fp), pYPKa_E_{tp}b).products


Calculate cseguid checksums for the resulting plasmids for future reference.
Cseguid is a checksum that uniquely describes a circular double stranded
sequence.

pYPKa_Z_{tp}.cseguid() should be {finalcseguidZ} 

    print(pYPKa_Z_{tp}.cseguid())
    assert pYPKa_Z_{tp}.cseguid() == "{finalcseguidZ}"

pYPKa_E_{tp}.cseguid() should be {finalcseguidE}
    
    print(pYPKa_E_{tp}.cseguid())
    assert pYPKa_E_{tp}.cseguid() == "{finalcseguidE}"
    
The sequences are named based on the name of the cloned insert.

    pYPKa_Z_{tp}.locus = "pYPKa_Z_{tp}"[:16]
    pYPKa_E_{tp}.locus = "pYPKa_Z_{tp}"[:16]

Stamp sequence with cseguid checksum. This can be used to verify the
integrity of the sequence file.

    pYPKa_Z_{tp}.stamp()
    pYPKa_E_{tp}.stamp()

Sequences are written to local files.

    pYPKa_Z_{tp}.write("pYPKa_Z_{tp}.gb")
    pYPKa_E_{tp}.write("pYPKa_E_{tp}.gb")

# [pYPKa_Z_{tp}](pYPKa_Z_{tp}.gb)

    from pydna.readers import read
    reloaded = read("pYPKa_Z_{tp}.gb")
    reloaded.verify_stamp()

# [pYPKa_E_{tp}](pYPKa_E_{tp}.gb)

    from pydna.readers import read
    reloaded = read("pYPKa_E_{tp}.gb")
    reloaded.verify_stamp()
