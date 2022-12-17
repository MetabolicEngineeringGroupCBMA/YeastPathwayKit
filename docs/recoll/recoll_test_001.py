#!/usr/bin/python3

from recoll import recoll

db = recoll.connect()
query = db.query()
nres = query.execute("filename:pYPKa.gb")
results = query.fetchmany(200)
for doc in results:
    print("%s %s" % (doc.url, doc.title))
    


"""

bjorn@bjorn-ThinkPad-T450s:~/Desktop$ python3 recoll_test.py 
file:///home/bjorn/python_packages/ypkpathway/scripts/pth2/pYPKa.gb 
file:///home/bjorn/python_packages/ypkpathway/scripts/old/mypathway/pYPKa.gb 
file:///home/bjorn/python_packages/ypkpathway/scripts/old/pth1/pYPKa.gb 
file:///home/bjorn/python_packages/ypkpathway/docs/pth6/pYPKa.gb 
file:///home/bjorn/python_packages/pydna/tests/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.MiguelPacheco/ANACONDA FILES (Tese) (copy)/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.MiguelPacheco/ANACONDA FILES (Tese)/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.MiguelPacheco/old/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.GabrielaRibeiro/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.LeilaEsteki/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/JoanaCunha/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.old_yeast_pathway_kit_files.zip 
file:///home/bjorn/Dropbox/SHARED/.old_yeast_pathway_kit_files.zip 
file:///home/bjorn/Dropbox/SHARED/.old_yeast_pathway_kit_files.zip 
file:///home/bjorn/Dropbox/SHARED/HumbertoPereira/ACC coli/pYPK0_TDH3tp_accA_TEF1tp_accB_TPI1tp_accC_RPS19atp_accD_PGI1tp/gb/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/SaraBaptista/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/.MárioBarroca/DGA1_TLG3 pathway/pYPKa.gb 
file:///home/bjorn/Downloads/pYPKa.gb 
file:///home/bjorn/files/sequences/pYPKa.gb 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2015-02-24/pydna-DNA-assembly.zip 
file:///home/bjorn/files/ARCHIVE/2017-03-18/__________ pydna-DNA-assembly_______/sequence_files/pYPKa.gb 
file:///home/bjorn/files/ARCHIVE/2015-06-17/pydna papers/NAR methods/supplementary data_3/Lactose_pathway/pYPKa.gb 
file:///home/bjorn/files/ARCHIVE/2015-06-17/pydna papers/NAR methods/supplementary data_3.zip 
file:///home/bjorn/files/ARCHIVE/2015-06-17/pydna papers/BMC Bioinformatics/supplementary data.zip 
file:///home/bjorn/files/ARCHIVE/2015-06-17/pydna papers/BMC Bioinformatics/supplementary data/Lactose_pathway/genbank_files/pYPKa.gb 
file:///home/bjorn/files/ACC1_SNF1_analysis_2014-02-09/pYPKa.gb 
file:///home/bjorn/Teaching/.GMB18-Genetica-Molecular-e-Bioinformatica_17-18/2018-05-21_Monday_FINAL_PRACTICAL_CLASS/yeast_pathway_kit_betacarotene/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/AngelaCarvalho/lactose pathway/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/HumbertoPereira/ACC coli/pYPKa.gb 
file:///home/bjorn/Teaching/.GMB19-Genetica-Molecular-e-Bioinformatica_18-19/_yeast_pathway_kit_betacarotene/pYPKa.gb 
file:///home/bjorn/Documents/Berkeley2/pYPKa.gb 
file:///home/bjorn/Teaching/TPs/TP24_Small_scale_assembly_of_sequence_reads/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/PauloSilva/Berkeley/pYPKa.gb 
file:///home/bjorn/files/ARCHIVE/2020-09-28/ypk-xylose-pathways (copy)/notebooks/pYPKa.gb 
file:///home/bjorn/Dropbox/SHARED/PedroSantos/New TPs 2021/TP24_Small_scale_assembly_of_sequence_reads/pYPKa.gb 
file:///home/bjorn/python_packages/ypkpathway/src/ypkpathway/data/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectAnacondaBlogPost/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectChaetomiumTransporters/notebooks/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/.ProjectMalonylCoADecarboxylase/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectpTAx/pTA-GFP/pTA-GFP/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectACC_phosphorylation_site_screening/ACC1_phosphorylation_site_screening_KEGG/ACC1_SNF1_analysis_2014-02-09/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectBCKADH/BCKDH (another copy)/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectBCKADH/BCKDH (copy)/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/ProjectBCKADH/pYPKa.gb 
file:///home/bjorn/files/mec@github/ypk-xylose-pathways/notebooks/pYPKa.gb 
file:///home/bjorn/files/mec@github/Silva_et_al_2020/notebooks/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/LeilaEsteki/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/MárioBarroca/DGA1_TLG3 pathway/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/AngelaCarvalho/lactose pathway/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/MiguelPacheco/old/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/MiguelPacheco/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/JoanaCunha/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/_GabrielaRibeiro/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/FlavioAzevedo/_pYPKa_ZE_vectors GARBAGE/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/FlavioAzevedo/ACC coli/pYPK0_TDH3tp_accA_TEF1tp_accB_TPI1tp_accC_RPS19atp_accD_PGI1tp.zip 
file:///home/bjorn/files/mec@github/.old/constructs/_BjornJohansson/Berkeley/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/constructs/SaraBaptista/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/.constructs_old/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_TDH3tp_BsAraA_PDC1tp_KlLAC4_PGI1tp_KlLAC12_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_ENO2tp_FabH_RPL12Atp_FabD_RPL12Btp_FabG_RPS7Btp_acpP_RPL14Btp_FabF_RPL16Atp_FabB_RPL16Btp_FabA_RPL17Atp_FabZ_RPS18Btp_FabI_TDH1tp_TesA_RPL11Btp_acpS_TDH3tp_TesB_TEF1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_AgTEFp_KlLAC4_RPL14Btp_KlLAC12_AgTEFt.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_RPS19atp_PhXYL_RPL12atp_AnXLND_ScTEF1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_TEF1tp_ScALD6_TDH3tp_ScZWF1_PGI1tp_ScACS1_RPS19atp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_PDC1tp_KlLAC4_PGI1tp_KlLAC12_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_TPI1tp_YlACC1_PDC1tp_YlACL2_FBA1tp_YlACL2_ENO2tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_PGI1tp_ScACS1_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_RPS19atp_PhXYL_RPL12atp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_TDH3tp_FDH1_PDC1tp_pfLA_PGI1tp_pfLB_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old/archive/pYPK0_RPL12atp_AnXLND_ScTEF1tp.zip 
file:///home/bjorn/files/mec@github/.old/sequence_files/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/pYPKa.gb 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TDH3tp_BsAraA_PDC1tp_KlLAC4_PGI1tp_KlLAC12_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_ENO2tp_FabH_RPL12Atp_FabD_RPL12Btp_FabG_RPS7Btp_acpP_RPL14Btp_FabF_RPL16Atp_FabB_RPL16Btp_FabA_RPL17Atp_FabZ_RPS18Btp_FabI_TDH1tp_TesA_RPL11Btp_acpS_TDH3tp_TesB_TEF1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_AgTEFp_KlLAC4_RPL14Btp_KlLAC12_AgTEFt.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_RPS19atp_PhXYL_RPL12atp_AnXLND_ScTEF1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TEF1tp_ScALD6_TDH3tp_ScZWF1_PGI1tp_ScACS1_RPS19atp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_PDC1tp_KlLAC4_PGI1tp_KlLAC12_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TPI1tp_YlACC1_PDC1tp_YlACL2_FBA1tp_YlACL2_ENO2tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_PGI1tp_ScACS1_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_RPS19atp_PhXYL_RPL12atp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_TDH3tp_FDH1_PDC1tp_pfLA_PGI1tp_pfLB_TPI1tp.zip 
file:///home/bjorn/files/mec@github/.old/.constructs_old_old/archive/pYPK0_RPL12atp_AnXLND_ScTEF1tp.zip 
file:///home/bjorn/files/mec@github/dDEL/notebooks/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/.files/update/nb/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/.files/update/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/.files/update3/nb/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/.files/update3/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/.files/update2/nb/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/.files/update2/pYPKa.gb 
file:///home/bjorn/files/mec@github/YeastPathwayKit/sequences/pYPKa.gb 
file:///home/bjorn/files/mec@github/pydna-examples/notebooks/strawberry_aat/pYPKa.gb 
file:///home/bjorn/files/mec@github/pydna-examples/notebooks/primer_screening/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/Pozdniakova_et_al_2022/notebooks/pYPKa_A_vectors/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/Pozdniakova_et_al_2022/notebooks/pYPK0_FASII/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/old/pYPKa_A_FASII_vectors_2019-09-24T09:40:50.493551/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/old/pTA1_FASII_pathway (copy)/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/old/n/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/old/pTA1_FASII_pathway/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/old/pYPK0_FASII_pw12_assembly_2022-03-06T16:37:49.176671/pYPKa.gb 
file:///home/bjorn/files/work-in-progress/Project_yFASII/old/pYPK0_FASII_12_assembly_2019-09-25T06:54:58 (copy).438039/pYPKa.gb 
bjorn@bjorn-ThinkPad-T450s:~/Desktop$ 




"""