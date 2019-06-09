# coding: utf-8
'''
ScPDC1_PacI-ScTKL1-ScRPS19b_PacI
                   ScRPS19b_PacI-ScRPE1-ScRPS19a_PacI
                                        ScRPS19a_PacI-ScRKI1-ScTPI1_PacI
                                                             ScTPI1_PacI-CiGXF1-ScENO2_PacI
'''

from pydna import *
from pydna_helper.load_my_primers import primer, new_primer
from pydna_helper import gb, ape
from Bio.SeqUtils.CheckSum import seguid

from pygenome import sg as sgd

ScPDC1tp   = pcr([primer[413],primer[625]], Dseqrecord(sgd.promoter("PDC1")))
ScRPS19atp = pcr([primer[538],primer[539]], Dseqrecord(sgd.promoter("RPS19a")))
ScRPS19btp = pcr([primer[537],primer[536]], Dseqrecord(sgd.promoter("RPS19b")))
ScTPI1tp   = pcr([primer[419],primer[621]], Dseqrecord(sgd.promoter("TPI1")))
ScENO2tp   = pcr([primer[411],primer[452]], Dseqrecord(sgd.intergenic_sequence("YHR172W", "YHR174W")))


# load pCAPs and pCAPs-pSU0 as dsdna objects
from pYPK0 import pYPK0 as pCAPs

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


ScRPE1            = pcr( primer[556], primer[557],  Dseqrecord(sgd.cds("RPE1")))
pCAPs_AjiI_ScRPE1 = (pCAPs_AjiI + ScRPE1).looped()

ScRKI1            = pcr( primer[555], primer[554],  Dseqrecord(sgd.cds("RKI1")))
pCAPs_AjiI_ScRKI1 = (pCAPs_AjiI + ScRKI1).looped()

CiGXF1            = pcr( primer[553], primer[552], gb("AJ937350"))
pCAPs_AjiI_CiGXF1 = (pCAPs_AjiI + CiGXF1).looped()

pCAPs_pSU0 = read("/home/bjorn/Dropbox/wikidata/pCAPs-pSU0.wiki")

pCAPs_pSU0_E_Z, stuffer = pCAPs_pSU0.cut((EcoRV,ZraI))

ypk_primer = parse("/home/bjorn/Dropbox/wikidata/ypk_primers.wiki")




#ScPDC1_PacI-ScTKL1-ScRPS19b_PacI

A_ScPDC1tp_b   = pcr( primer[167],   primer[567],   pCAPs_ZraI_ScPDC1tp)
ScTKL1         = pcr( ypk_primer[8], ypk_primer[9], Dseqrecord(sgd.cds("TKL1")))
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