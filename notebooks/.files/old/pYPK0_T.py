#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from pydna import pcr, parse, Assembly
from Bio.Restriction import ZraI, AjiI, EcoRV

from pYPK0 import pYPK0

p167,p166 = parse('''>167_pCAPSfw (24-mer)
                     TCCTGACGGGTAATTTTGATTTGC
                     >166_pCAPSrv (24-mer)
                     CTGTGAAGTGGCTGAAATTTCGTA''')                      

p413,p625 = parse('''>413_ScPDC1tpf (24-mer)
                     TTAAATAAGGGTAGCCTCCCCATA
                     >625_ScPDC1tpr_PacI (34-mer)
                     taattaaTTTGATTGATTTGACTGTGTTATTTTG''', ds=False)
                       
p648,p647 = parse('''>648_ScRPS19btpf2
                     ttaaatTCTAGTATGGTTTGAAACCT 
                     >647_ScRPS19btpr_PacI
                     taattaaCTTTATTATCTTTGGTTCTAT''', ds=False)


#652
p538,p651 = parse('''>538_ScRPS19atpr_FspA (26-mer)
                     gcgcatGTTAACTGAAATGAAAATTT                         
                     >651_ScRPS19atpr_PacI
                     taattaaTTTTACTCTATTTGTCGATC''', ds=False)

p419,p621 = parse('''>419_ScTPI1tpf (32-mer)
                     TTAAATTGTTTAAAGATTACGGATATTTAACT
                     >621_ScTPI1tpr_PacI (35-mer)
                     taattaaTTTTAGTTTATGTATGTGTTTTTTGTAG''', ds=False)
                     
#PDC1tp_ScTKL1_RPS19btp
#              RPS19btp_ScRPE1_RPS19atp
#                              RPS19atp_ScRKI1tp_TPI1tp
#                                                TPI1tp_CiGXF1_ENO2tp

from pYPK0_PDC1tp_ScTKL1_RPS19btp   import pYPK0_PDC1tp_ScTKL1_RPS19btp   as cas1
from pYPK0_RPS19btp_ScRPE1_RPS19atp import pYPK0_RPS19btp_ScRPE1_RPS19atp as cas2
from pYPK0_RPS19atp_ScRKI1_TPI1tp   import pYPK0_RPS19atp_ScRKI1_TPI1tp   as cas3
from pYPK0_TPI1tp_CiGXF1_ENO2tp     import pYPK0_TPI1tp_CiGXF1_ENO2tp     as cas4



cas1  = pcr( p167, p647, cas1)
cas2  = pcr( p648, p651, cas2)
cas3  = pcr( p538, p621, cas3) 
cas4  = pcr( p419, p166, cas4)

pYPK0_E_Z, stuffer = pYPK0.cut((EcoRV, ZraI))

#print [cas1, cas2, cas3, cas4, pYPK0_E_Z]

a = Assembly([cas1, cas2, cas3, cas4, pYPK0_E_Z], limit = 61)

seq = a.assemble_circular()[0]

print seq.small_fig()
    
seq=seq.synced("tcgcgcgtttcggtgatgacggtgaaaacctctg")

pYPK0_T=seq

'''
# coding: utf-8

ScPDC1tp_ScTKL1_ScRPS19btp
          ScRPS19btp_ScRPE1_ScRPS19atp
                          ScRPS19a_ScRKI1tp_ScTPI1tp
                                          ScTPI1tp_CiGXF1_ScENO2tp


from pydna import *
from pydna_helper.load_my_primers import primer, new_primer
from pydna_helper import gb, ape
from Bio.SeqUtils.CheckSum import seguid

from pygenome import sg



ScPDC1tp   = pcr([primer[413],primer[625]], Dseqrecord(sg.promoter("PDC1")))
ScRPS19atp = pcr([primer[538],primer[539]], Dseqrecord(sg.promoter("RPS19a")))
ScRPS19btp = pcr([primer[537],primer[536]], Dseqrecord(sg.promoter("RPS19b")))
ScTPI1tp   = pcr([primer[419],primer[621]], Dseqrecord(sg.promoter("TPI1")))
ScENO2tp   = pcr([primer[411],primer[452]], Dseqrecord(sg.intergenic_sequence("YHR172W", "YHR174W")))

import sys;sys.exit()

# load pCAPs and pCAPs-pSU0 as dsdna objects
pCAPs      = read("/home/bjorn/Dropbox/wikidata/pCAPs-AjiI.wiki")

from Bio.Restriction import EcoRV, ZraI, AjiI
pCAPs_ZraI  = pCAPs.cut(ZraI).pop()
pCAPs_AjiI  = pCAPs.cut(AjiI).pop()
pCAPs_EcoRV = pCAPs.cut(EcoRV).pop()

pCAPs_ZraI_ScPDC1tp  = (pCAPs_ZraI  + ScPDC1tp).looped()

pCAPs_ZraI_ScRPS19atp  = (pCAPs_ZraI  + ScRPS19atp).looped()
pCAPs_EcoRV_ScRPS19atp = (pCAPs_EcoRV + ScRPS19atp).looped()

pCAPs_ZraI_ScRPS19btp    = (pCAPs_ZraI  + ScRPS19btp).looped()
pCAPs_EcoRV_ScRPS19btp   = (pCAPs_EcoRV + ScRPS19btp).looped()

pCAPs_ZraI_ScTPI1tp  = (pCAPs_ZraI  + ScTPI1tp).looped()
pCAPs_EcoRV_ScTPI1tp = (pCAPs_EcoRV + ScTPI1tp).looped()

pCAPs_EcoRV_ScENO2tp = (pCAPs_EcoRV + ScENO2tp).looped()


ScRPE1            = pcr( primer[556], primer[557], sg.cds("RPE1"))
pCAPs_AjiI_ScRPE1 = (pCAPs_AjiI + ScRPE1).looped()
            
ScRKI1            = pcr( primer[555], primer[554], sg.cds("RKI1"))
pCAPs_AjiI_ScRKI1 = (pCAPs_AjiI + ScRKI1).looped()

CiGXF1            = pcr( primer[553], primer[552], gb("AJ937350"))
pCAPs_AjiI_CiGXF1 = (pCAPs_AjiI + CiGXF1).looped()

pCAPs_pSU0 = read("/home/bjorn/Dropbox/wikidata/pCAPs-pSU0.wiki")

pCAPs_pSU0_E_Z, stuffer = pCAPs_pSU0.cut((EcoRV,ZraI))

ypk_primer = parse("/home/bjorn/Dropbox/wikidata/ypk_primers.wiki")




#ScPDC1_PacI-ScTKL1-ScRPS19b_PacI

A_ScPDC1tp_b   = pcr( primer[167],   primer[567],   pCAPs_ZraI_ScPDC1tp)
ScTKL1         = pcr( ypk_primer[8], ypk_primer[9], sg.cds("TKL1"))
C_ScRPS19btp_d = pcr( primer[568],   primer[166],   pCAPs_EcoRV_ScRPS19btp)

sequences, circular = circular_assembly((  A_ScPDC1tp_b,
                                       ScTKL1,
                                       C_ScRPS19btp_d,
                                       pCAPs_pSU0_E_Z), limit=29)

pYPK0_ScPDC1tp_ScTKL1_ScRPS19btp = circular[0]


#ScRPS19b_PacI-ScRPE1-ScRPS19a_PacI

A_ScRPS19btp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScRPS19btp)
ScRPE1         = pcr( primer[468],primer[467], pCAPs_AjiI_ScRPE1)
C_ScRPS19atp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScRPS19atp)

sequences, circular = circular_assembly((  A_ScRPS19btp_b,
                                       ScRPE1,
                                       C_ScRPS19atp_d,
                                       pCAPs_pSU0_E_Z), limit=31)

pYPK0_ScRPS19btp_ScRPE1_ScRPS19atp = circular[0]


#ScRPS19a_PacI-ScRKI1-ScTPI1_PacI

A_ScRPS19atp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScRPS19atp)
ScRKI1           = pcr( primer[468],primer[467], pCAPs_AjiI_ScRKI1)         
C_ScTPI1tp_d   = pcr( primer[568],primer[166], pCAPs_EcoRV_ScTPI1tp)
sequences, circular = circular_assembly((  A_ScRPS19atp_b,
                                       ScRKI1,
                                       C_ScTPI1tp_d,
                                       pCAPs_pSU0_E_Z), limit=28)
pYPK0_ScRPS19atp_ScRKI1_ScTPI1tp = circular[0]


#ScTPI1_PacI-CiGXF1-ScENO2_PacI

A_ScTPI1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScTPI1tp)
CiGXF1       = pcr( primer[468],primer[467], pCAPs_AjiI_CiGXF1)
C_ScENO2tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScENO2tp)
sequences, circular = circular_assembly((  A_ScTPI1tp_b,
                                       CiGXF1,
                                       C_ScENO2tp_d,
                                       pCAPs_pSU0_E_Z), limit=28)

pYPK0_ScTPI1tp_CiGXF1_ScENO2tp = circular[0]


tp_first  = pcr( primer[167], primer[467], pCAPs_ZraI_ScPDC1tp)
tp_last   = pcr( primer[468], primer[166], pCAPs_EcoRV_ScENO2tp)

sequences, circular = circular_assembly((  tp_first,
                                       tp_last,
                                       pCAPs_pSU0_E_Z), limit=28)

pYPK0_tp_tp = circular.pop()

pYPK0_tp_tp_lin = pcr( primer[411], primer[625], pYPK0_tp_tp)


ScPDC1tp_ScTKL1_ScRPS19btp_2    = pcr([primer[167],primer[166]], pYPK0_ScPDC1tp_ScTKL1_ScRPS19btp )
ScRPS19btp_ScRPE1_ScRPS19atp_2  = pcr([primer[167],primer[166]], pYPK0_ScRPS19btp_ScRPE1_ScRPS19atp )
ScRPS19atp_ScRKI1_ScTPI1tp_2    = pcr([primer[167],primer[166]], pYPK0_ScRPS19atp_ScRKI1_ScTPI1tp )
ScTPI1tp_CiGXF1_ScENO2tp_2      = pcr([primer[167],primer[166]], pYPK0_ScTPI1tp_CiGXF1_ScENO2tp )

sequences, circular = circular_assembly((

ScPDC1tp_ScTKL1_ScRPS19btp_2,
             ScRPS19btp_ScRPE1_ScRPS19atp_2,
                               ScRPS19atp_ScRKI1_ScTPI1tp_2,
                                                 ScTPI1tp_CiGXF1_ScENO2tp_2,                                
                                                     
                                                         pYPK0_tp_tp_lin), limit=400)




pYPK0_T = sync(circular[0], "tcgcgcgtttcggtgatgacggtgaaaacc")

#print len(pYPK0_T)
#print pYPK0_T.seguid()

assert len(pYPK0_T)      == 14502
assert pYPK0_T.seguid()  == "j1knGaLOluEtN5aiWGdt61leHt0"

pYPK0_T.write("pYPK0_T.gb")

print "done!"

'''
