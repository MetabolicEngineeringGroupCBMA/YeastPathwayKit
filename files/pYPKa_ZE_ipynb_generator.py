#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pydna

pYPKa = pydna.read('''
LOCUS       pYPKa                   3128 bp    DNA     circular UNK 08-MAY-2015
DEFINITION  Product_568_pCAPsAjiIR (22-mer)_567_pCAPsAjiIF (23-mer)
            cSEGUID_aV1eIrzOiCjvw01yvKkxDXHKLMk_2015-05-08T16:41:28.034624
ACCESSION   3128bp TmU_6uVdgKq5aQhTpHux7dVk9J8
VERSION     3128bp TmU_6uVdgKq5aQhTpHux7dVk9J8
KEYWORDS    .
SOURCE      .
  ORGANISM  .
            .
FEATURES             Location/Qualifiers
     primer_bind     complement(558..578)
                     /note="567_pCAPsAjiIF"
                     /ApEinfo_fwdcolor="green"
                     /ApEinfo_revcolor="red"
     misc            complement(558..580)
                     /label="567_pCAPsAjiIF"
     misc            581..602
                     /label="568_pCAPsAjiIR"
     primer_bind     583..602
                     /note="568_pCAPsAjiIR"
                     /ApEinfo_fwdcolor="green"
                     /ApEinfo_revcolor="red"
     rep_origin      1313
                     /direction=BOTH
     gene            complement(2072..2932)
                     /gene="bla"
     CDS             complement(2072..2932)
                     /product="beta-lactamase"
                     /codon_start=1
                     /transl_table=11
                     /db_xref="GI:2769263"
                     /db_xref="GOA:Q79DR3"
                     /db_xref="HSSP:P62593"
                     /db_xref="InterPro:IPR000871"
                     /db_xref="InterPro:IPR001466"
                     /db_xref="InterPro:IPR012338"
                     /db_xref="UniProtKB/TrEMBL:Q79DR3"
                     /translation="MSIQHFRVALIPFFAAFCLPVFAHPETLVKVKDAEDQLGARVGYI
                     ELDLNSGKILESFRPEERFPMMSTFKVLLCGAVLSRIDAGQEQLGRRIHYSQNDLVEYS
                     PVTEKHLTDGMTVRELCSAAITMSDNTAANLLLTTIGGPKELTAFLHNMGDHVTRLDRW
                     EPELNEAIPNDERDTTMPVAMATTLRKLLTGELLTLASRQQLIDWMEADKVAGPLLRSA
                     LPAGWFIADKSGAGERGSRGIIAALGPDGKPSRIVVIYTTGSQATMDERNRQIAEIGAS
                     LIKHW"
                     /gene="bla"
                     /protein_id="CAA04868.1"
ORIGIN
        1 tcgcgcgttt cggtgatgac ggtgaaaacc tctgacacat gcagctcccg gagacggtca
       61 cagcttgtct gtaagcggat gccgggagca gacaagcccg tcagggcgcg tcagcgggtg
      121 ttggcgggtg tcggggctgg cttaactatg cggcatcaga gcagattgta ctgagagtgc
      181 accatagatc ctgaggatcg gggtgataaa tcagtctgcg ccacatcggg ggaaacaaaa
      241 tggcgcgaga tctaaaaaaa aaggctccaa aaggagcctt tcgcgctacc aggtaacgcg
      301 ccactccgac gggattaacg agtgccgtaa acgacgatgg ttttaccgtg tgcggagatc
      361 aggttctgat cctcgagcat cttaagaatt cgtcccacgg tttgtctaga gcagccgaca
      421 atctggccaa tttcctgacg ggtaattttg atttgcatgc cgtccgggtg agtcatagcg
      481 tctggttgtt ttgccagatt cagcagagtc tgtgcaatgc ggccgctgac gtcgaggaac
      541 gccaggttgc ccactttctc actagtgacc tgcagccgac gtgccatctg tgcagacaaa
      601 cgcatcagga tatccggatt tacctgaatc aattggcgaa attttttgta cgaaatttca
      661 gccacttcac aggcggtttt cgcacgtacc catgcgctac gttcctggcc ctcttcaaac
      721 aggcccagtt cgccaataaa atcaccctga ttcagatagg agaggatcat ttctttaccc
      781 tcttcgtctt tgatcagcac tgccacagag cctttaacga tgtagtacag cgtttccgct
      841 ttttcaccct ggtgaataag cgtgctcttg gatgggtact tatgaatgtg gcaatgagac
      901 aagaaccatt cgagagtagg atccgtttga ggtttaccaa gtaccataag atccttaaat
      961 ttttattatc tagctagatg ataatattat atcaagaatt gtacctgaaa gcaaataaat
     1021 tttttatctg gcttaactat gcggcatcag agcagattgt actgagagtg caccatatgc
     1081 ggtgtgaaat accgcacaga tgcgtaagga gaaaataccg catcaggcgc tcttccgctt
     1141 cctcgctcac tgactcgctg cgctcggtcg ttcggctgcg gcgagcggta tcagctcact
     1201 caaaggcggt aatacggtta tccacagaat caggggataa cgcaggaaag aacatgtgag
     1261 caaaaggcca gcaaaaggcc aggaaccgta aaaaggccgc gttgctggcg tttttccata
     1321 ggctccgccc ccctgacgag catcacaaaa atcgacgctc aagtcagagg tggcgaaacc
     1381 cgacaggact ataaagatac caggcgtttc cccctggaag ctccctcgtg cgctctcctg
     1441 ttccgaccct gccgcttacc ggatacctgt ccgcctttct cccttcggga agcgtggcgc
     1501 tttctcatag ctcacgctgt aggtatctca gttcggtgta ggtcgttcgc tccaagctgg
     1561 gctgtgtgca cgaacccccc gttcagcccg accgctgcgc cttatccggt aactatcgtc
     1621 ttgagtccaa cccggtaaga cacgacttat cgccactggc agcagccact ggtaacagga
     1681 ttagcagagc gaggtatgta ggcggtgcta cagagttctt gaagtggtgg cctaactacg
     1741 gctacactag aaggacagta tttggtatct gcgctctgct gaagccagtt accttcggaa
     1801 aaagagttgg tagctcttga tccggcaaac aaaccaccgc tggtagcggt ggtttttttg
     1861 tttgcaagca gcagattacg cgcagaaaaa aaggatctca agaagatcct ttgatctttt
     1921 ctacggggtc tgacgctcag tggaacgaaa actcacgtta agggattttg gtcatgagat
     1981 tatcaaaaag gatcttcacc tagatccttt taaattaaaa atgaagtttt aaatcaatct
     2041 aaagtatata tgagtaaact tggtctgaca gttaccaatg cttaatcagt gaggcaccta
     2101 tctcagcgat ctgtctattt cgttcatcca tagttgcctg actccccgtc gtgtagataa
     2161 ctacgatacg ggagggctta ccatctggcc ccagtgctgc aatgataccg cgagacccac
     2221 gctcaccggc tccagattta tcagcaataa accagccagc cggaagggcc gagcgcagaa
     2281 gtggtcctgc aactttatcc gcctccatcc agtctattaa ttgttgccgg gaagctagag
     2341 taagtagttc gccagttaat agtttgcgca acgttgttgc cattgctaca ggcatcgtgg
     2401 tgtcacgctc gtcgtttggt atggcttcat tcagctccgg ttcccaacga tcaaggcgag
     2461 ttacatgatc ccccatgttg tgcaaaaaag cggttagctc cttcggtcct ccgatcgttg
     2521 tcagaagtaa gttggccgca gtgttatcac tcatggttat ggcagcactg cataattctc
     2581 ttactgtcat gccatccgta agatgctttt ctgtgactgg tgagtactca accaagtcat
     2641 tctgagaata gtgtatgcgg cgaccgagtt gctcttgccc ggcgtcaata cgggataata
     2701 ccgcgccaca tagcagaact ttaaaagtgc tcatcattgg aaaacgttct tcggggcgaa
     2761 aactctcaag gatcttaccg ctgttgagat ccagttcgat gtaacccact cgtgcaccca
     2821 actgatcttc agcatctttt actttcacca gcgtttctgg gtgagcaaaa acaggaaggc
     2881 aaaatgccgc aaaaaaggga ataagggcga cacggaaatg ttgaatactc atactcttcc
     2941 tttttcaata ttattgaagc atttatcagg gttattgtct catgagcgga tacatatttg
     3001 aatgtattta gaaaaataaa caaatagggg ttccgcgcac atttccccga aaagtgccac
     3061 ctgctaagaa accattatta tcatgacatt aacctataaa aataggcgta tcacgaggcc
     3121 ctttcgtc
//
''')


tps='''
Z TDH1
E
Z RPS18b
E
'''


tps='''
Z   TEF1 417 626
E   TDH3 415 623

Z   TDH3 415 623
E   FBA1 409 624

Z   FBA1 409 624
E   PDC1 413 625

Z   PDC1 413 625
E   RPS19b 648 647

Z   RPS19b 648 647
E   RPS19a 538 651

Z   RPS19a 538 651
E   TPI1 419 621

Z   TPI1 419 621
E   ENO2 411 660
'''
tps='''
RPL12A	 751    752	OK
RPL12B	 753    754	OK
RPS7B	 755    756	OK
RPL14B	 761    762	OK
RPL16A	 763    764	OK
RPL16B	 765    766	OK
RPL17A	 767    768	OK
RPL11B	 646    645	OK
RPL1A	 864    863	OK
RPL20B	 862    861	OK
RPL21A	 860    859	OK
RPL21B	 858    857	OK
RPL22A	 856    855	Check
RPL23A	 854    853	OK
RPL2A	 852    851	OK
RPL31B	 848    847	OK
RPL34A	 846    845	OK
RPL35A	 842    841	OK
RPL35B	 840    839	OK
RPL36A	 838    837	OK
RPL36B	 836    835	OK
RPL42A	 832    831	OK
RPL5   830    829	OK


'''

'''
Z	RPL6A	828    827	  NO
E	RPL6A	828    827	  NO
Z	RPL41A	834    833	  NO
E	RPL41A	834    833	  NO
Z	RPL34B	844    843	  NO
E	RPL34B	844    843	  NO
Z	RPL2B	850    849	  NO
E	RPL2B	850    849	  NO
'''
tps=tps.strip()

tps = "\n".join(x.strip() for x in tps.splitlines() if x)

from Bio.Restriction import ZraI, EcoRV

t='''
#Construction of promoter vector pYPKa_Z_{tp} and terminator vector pYPKa_E_{tp}

This notebook describe the construction of E. coli vectors [pYPKa_Z_{tp}](pYPKa_Z_{tp}.gb) and [pYPKa_E_{tp}](pYPKa_E_{tp}.gb)

The insert defined below is cloned in pYPKa using the blunt restriction
enzymes [ZraI](http://rebase.neb.com/rebase/enz/ZraI.html) and [EcoRV](http://rebase.neb.com/rebase/enz/EcoRV.html) in
two different plasmids. The insert cloned in ZraI will be used as a promoter, while in the EcoRV site it will be used as a
terminator.

![pYPKa_Z and pYPKa_E plasmids](pYPK_ZE.png "pYPKa_Z and pYPKa_E plasmids")

The [pydna](https://pypi.python.org/pypi/pydna/) package is imported in the code cell below.
There is a [publication](http://www.biomedcentral.com/1471-2105/16/142) describing pydna as well as
[documentation](http://pydna.readthedocs.org/en/latest/) available online.
Pydna is developed on [Github](https://github.com/BjornFJohansson/pydna).

	import pydna

The vector backbone pYPKa is read from a local [file](pYPKa.gb).

	pYPKa = pydna.read("pYPKa.gb")

Both restriction enzymes are imported from [Biopython](http://biopython.org/wiki/Main_Page)

	from Bio.Restriction import ZraI, EcoRV

The vector is cut with both enzymes.

	pYPKa_ZraI  = pYPKa.linearize(ZraI)
	pYPKa_EcoRV = pYPKa.linearize(EcoRV)

The template below comes from a Genbank [record](http://www.ncbi.nlm.nih.gov/nuccore/{gblink}).
Access to Genbank is needed in order to download the template.
If you execute this script, change the email address below to your own.
Always tell Genbank who you are, when using their web service.

    gb = pydna.Genbank("myownemail@example.com")

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

    fp,rp = pydna.parse(""">{fpn}
                            {fps}
                           >{rpn}
                            {rps}""", ds=False)

PCR to create the insert using the primers above.

    prd = pydna.pcr(fp, rp, template)
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
fifty percent of the clones. The PCR strategy below is used to identify the correct clones.

	pYPKa_Z_{tp}b = (pYPKa_ZraI  + prd.rc()).looped().synced(pYPKa)
	pYPKa_E_{tp}b = (pYPKa_EcoRV + prd.rc()).looped().synced(pYPKa)

A combination of standard primers and the primers above are
used for the strategy to identify correct clones.
Standard primers are listed [here](primers.fasta).

	p = {{ x.id: x for x in pydna.parse(""">577
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

##Diagnostic PCR confirmation

The correct structure of pYPKa_Z_{tp} is confirmed by PCR using standard primers
577 and 342 that are vector specific together with the {tp}fw primer specific for the insert
in a multiplex PCR reaction with
all three primers present.

Two PCR products are expected if the insert was cloned, the sizes depend
on the orientation. If the vector is empty or contains another insert, only one
product is formed.

####Expected PCR products sizes from pYPKa_Z_{tp}:

pYPKa_Z_{tp} with insert in correct orientation.

    pydna.Anneal( (p['577'], p['342'], fp), pYPKa_Z_{tp}).products

pYPKa_Z_{tp} with insert in reverse orientation.

    pydna.Anneal( (p['577'], p['342'], fp), pYPKa_Z_{tp}b).products

Empty pYPKa clone.

    pydna.Anneal( (p['577'], p['342'], fp), pYPKa).products

####Expected PCR products sizes pYPKa_E_{tp}:

pYPKa_E_{tp} with insert in correct orientation.

    pydna.Anneal( (p['577'], p['342'], fp), pYPKa_E_{tp}).products

pYPKa_E_{tp} with insert in reverse orientation.

    pydna.Anneal( (p['577'], p['342'], fp), pYPKa_E_{tp}b).products


Calculate cseguid checksums for the resulting plasmids for future reference.
Cseguid is a checksum that uniquely describes a circular double stranded
sequence.

	print(pYPKa_Z_{tp}.cseguid())
	print(pYPKa_E_{tp}.cseguid())

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
    pass

#[pYPKa_Z_{tp}](pYPKa_Z_{tp}.gb)

	import pydna
	reloaded = pydna.read("pYPKa_Z_{tp}.gb")
	reloaded.verify_stamp()

#[pYPKa_E_{tp}](pYPKa_E_{tp}.gb)

	import pydna
	reloaded = pydna.read("pYPKa_E_{tp}.gb")
	reloaded.verify_stamp()

'''





import subprocess

from pydna_helper import load_my_primers as lp

from pygenome import sg


tp="tp"

for insertname, pf, pr, status in (x.split() for x in tps.split("\n")):
    print "in:", letter, insertname, pf, pr,

    fp = lp.primer[int(pf)]
    rp = lp.primer[int(pr)]

    gbref  = sg.gene[insertname.upper()].promoter().description
    gblink = sg.gene[insertname.upper()].cds().id

    template = pydna.Dseqrecord(sg.gene[insertname.upper()].promoter())

    templatesize = len(template)
    insertseguid = template.seguid()

    finalcseguid = (pYPKa.linearize(enz)+pydna.pcr(fp, rp, template)).looped().cseguid()

    #import sys;sys.exit()

    r =  t.format( tp = insertname,
                   enz=repr(enz),
                   gbref = gbref,
                   gblink =gblink,
                   templatesize = templatesize,
                   insertseguid = insertseguid,
                   finalcseguid = finalcseguid,
                   fpn=fp.name,
                   fps=fp.seq,
                   rpn=rp.name,
                   rps=rp.seq)

    newfn = "pYPKa_ZE_{}".format(insertname)

    with open("."+newfn+".md", "w") as f: f.write(r)


    cmd = "/home/bjorn/anaconda/envs/bjorn/bin/notedown .{n}.md > {n}.ipynb".format(n=newfn)

    print subprocess.check_output(cmd, shell=True),
    print newfn+".ipynb"
    print

    #break




