# coding: utf-8

'''
                  >                           >                  >                >
pYPK0-ScTEF1_PacI-PsXYL1(TMB3061)-ScTDH3_PACI-PsXYL2-ScPGI1_PacI-ScXK-ScFBA1_PacI-ScTAL1-ScPDC1_PacI
                                                   <                <                  <

ScTEF1_PacI-PsXYL1(TMB3061)-ScTDH3_PACI
                            ScTDH3_PACI-PsXYL2-ScPGI1_PacI
                                               ScPGI1_PacI-ScXK-ScFBA1_PacI
                                                                ScFBA1_PacI-ScTAL1-ScPDC1_PacI



'''



from pydna import *
from pydna_helper.load_my_primers import primer
from pydna_helper import gb
from Bio.SeqUtils.CheckSum import seguid

from pygenome import sg as sgd


ScTEF1tp = pcr([primer[417],primer[626]], Dseqrecord(sgd.promoter("TEF1")))
ScTDH3tp = pcr([primer[415],primer[623]], Dseqrecord(sgd.promoter("TDH3")))
ScPGI1tp = pcr([primer[549],primer[622]], Dseqrecord(sgd.intergenic_sequence("YBR197C", "PGI1")))
ScFBA1tp = pcr([primer[409],primer[624]], Dseqrecord(sgd.promoter("FBA1")))
ScPDC1tp = pcr([primer[413],primer[625]], Dseqrecord(sgd.promoter("PDC1")))

# load pCAPs and pCAPs-pSU0 as dsdna objects
from pYPKa import pYPKa

from Bio.Restriction import EcoRV, ZraI, AjiI
pYPKa_ZraI  = pYPKa.linearize(ZraI)
pYPKa_AjiI  = pYPKa.linearize(AjiI)
pYPKa_EcoRV = pYPKa.linearize(EcoRV)

pCAPs_ZraI_ScTEF1tp  = (pYPKa_ZraI  + ScTEF1tp).looped()

pCAPs_ZraI_ScTDH3tp  = (pYPKa_ZraI  + ScTDH3tp).looped()
pCAPs_EcoRV_ScTDH3tp = (pYPKa_EcoRV + ScTDH3tp).looped()

pCAPs_ZraI_ScPGI1tp    = (pYPKa_ZraI  + ScPGI1tp).looped()
pCAPs_EcoRV_ScPGI1tp   = (pYPKa_EcoRV + ScPGI1tp).looped()

pCAPs_ZraI_ScFBA1tp  = (pYPKa_ZraI  + ScFBA1tp).looped()
pCAPs_EcoRV_ScFBA1tp = (pYPKa_EcoRV + ScFBA1tp).looped()

pCAPs_EcoRV_ScPDC1tp = (pYPKa_EcoRV + ScPDC1tp).looped()

XYL1 = pcr( primer[620], primer[619], Dseqrecord(gb("X59465"))) #xyl1 P. stipitis
pCAPs_AjiI_XR  = (pYPKa_AjiI + XYL1).looped()

XYL2 = pcr( primer[618], primer[617], Dseqrecord(gb("A16166"))) #xyl2 P. stipitis
pCAPs_AjiI_XDH = (pYPKa_AjiI + XYL2).looped()

ScXK = pcr( primer[616], primer[615], Dseqrecord(sgd.cds("XKS1")))
pCAPs_AjiI_XK = (pYPKa_AjiI + ScXK).looped()

ScTAL1 = pcr( primer[614], primer[613], Dseqrecord(sgd.cds("TAL1")))
pCAPs_AjiI_TAL = (pYPKa_AjiI + ScTAL1).looped()


from pYPK0 import pYPK0 as pCAPs_pSU0

pCAPs_pSU0_E_Z, stuffer = pCAPs_pSU0.cut((EcoRV,ZraI))

#ypk_primer = parse("/home/bjorn/Dropbox/wikidata/ypk_primers.wiki")






a=Dseqrecord("GTCgaggaacgccaggttgcccactttctcactagtgacctgcagccGAC")
b=Dseqrecord("GTGccatctgtgcagacaaacgcatcagGAT")

pw=(
ScTEF1tp,
a,
XYL1,
b,
ScTDH3tp,
a,
XYL2,
b,
ScPGI1tp,
a,
ScXK,
b,
ScFBA1tp,
a,
ScTAL1,
b,
ScPDC1tp,)

x=Dseqrecord("")
for p in pw:
    x+=p

theoretical_pw = (pCAPs_pSU0_E_Z + x).looped().synced("tcgcgcgtttcggtgatgacggtgaaaacc")




#ScTEF1_PacI-PsXYL1(TMB3061)-ScTDH3_PACI
A_ScTEF1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScTEF1tp)
PsXR         = pcr( primer[468],primer[467], pCAPs_AjiI_XR)
C_ScTDH3tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScTDH3tp)
circular = Assembly((  A_ScTEF1tp_b,
                        PsXR,
                        C_ScTDH3tp_d,
                        pCAPs_pSU0_E_Z), limit=31).assemble_circular()

pYPK0_ScTEF1tp_XR_ScTDH3tp = circular[0]


#ScTDH3_PACI-PsXYL2-ScPGI1_PacI

A_ScTDH3tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScTDH3tp)
PsXDH        = pcr( primer[468],primer[467], pCAPs_AjiI_XDH)
C_ScPGI1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScPGI1tp)
circular = Assembly((  A_ScTDH3tp_b,
                        PsXDH,
                        C_ScPGI1tp_d,
                        pCAPs_pSU0_E_Z), limit=31).assemble_circular()

pYPK0_ScTDH3tp_XDH_ScPGI1tp = circular[0]

#ScPGI1_PacI-ScXK-ScFBA1_PacI



A_ScPGI1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScPGI1tp)
ScXK         = pcr( primer[468],primer[467], pCAPs_AjiI_XK)
C_ScFBA1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScFBA1tp)
circular = Assembly((  A_ScPGI1tp_b,
                        ScXK,
                        C_ScFBA1tp_d,
                        pCAPs_pSU0_E_Z), limit=28).assemble_circular()
pYPK0_ScPGI1tp_XK_ScFBA1tp = circular[0]

#ScFBA1_PacI-ScTAL1-ScPDC1_PacI
A_ScFBA1tp_b = pcr( primer[167],primer[567], pCAPs_ZraI_ScFBA1tp)
ScTAL1       = pcr( primer[468],primer[467], pCAPs_AjiI_TAL)
C_ScPDC1tp_d = pcr( primer[568],primer[166], pCAPs_EcoRV_ScPDC1tp)
circular = Assembly((  A_ScFBA1tp_b,
                        ScTAL1,
                        C_ScPDC1tp_d,
                        pCAPs_pSU0_E_Z), limit=28).assemble_circular()
pYPK0_ScFBA1tp_TAL1_ScPDC1tp = circular[0]

tp_first  = pcr( primer[167], primer[467], pCAPs_ZraI_ScTEF1tp)
tp_last   = pcr( primer[468], primer[166], pCAPs_EcoRV_ScPDC1tp)

circular = Assembly((  tp_first,
                        tp_last,
                        pCAPs_pSU0_E_Z), limit=28).assemble_circular()

pYPK0_tp_tp = circular[0]

pYPK0_tp_tp_lin = pcr( primer[413], primer[626], pYPK0_tp_tp)

ScTEF1tp_XR_ScTDH3tp_2    = pcr( [primer[167],primer[166]], pYPK0_ScTEF1tp_XR_ScTDH3tp)
ScTDH3tp_XDH_ScPGI1tp_2   = pcr( [primer[167],primer[166]], pYPK0_ScTDH3tp_XDH_ScPGI1tp)
ScPGI1tp_XK_ScFBA1tp_2    = pcr( [primer[167],primer[166]], pYPK0_ScPGI1tp_XK_ScFBA1tp)
ScFBA1tp_TAL1_ScPDC1tp_2  = pcr( [primer[167],primer[166]], pYPK0_ScFBA1tp_TAL1_ScPDC1tp)



circular = Assembly((

ScTEF1tp_XR_ScTDH3tp_2,
            ScTDH3tp_XDH_ScPGI1tp_2,
                         ScPGI1tp_XK_ScFBA1tp_2,
                                     ScFBA1tp_TAL1_ScPDC1tp_2,

pYPK0_tp_tp_lin), limit=400).assemble_circular()

pYPK0_Df = circular[0].synced("tcgcgcgtttcggtgatgacggtgaaaacc")


assert len(pYPK0_Df)      == 14804
assert pYPK0_Df.seguid()  == "6iQyiTBnD+9tnheJYuSC04Di5t4"
assert eq(pYPK0_Df, theoretical_pw)

