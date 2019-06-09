#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyeast import saccharomyces_cerevisiae_genome as sc
sgd = sc.saccharomyces_cerevisiae_genome()


print sgd.promoter("ENO2").seq[0:10]
print sgd.promoter("TEF1").seq[0:10]
print sgd.promoter("TPI1").seq[0:10]
print sgd.promoter("PDC1").seq[0:10]
print sgd.promoter("FBA1").seq[0:10]
print sgd.promoter("TDH3").seq[0:10]
print sgd.promoter("PGI1").seq[0:10]

'''
ScENO2 Enolase II
ScFBA1 Fructose 1,6-bisphosphate aldolase
ScPDC1 Pyruvate decarboxylase
ScPGI1 Phosphoglucose isomerase
ScTDH3 glyceraldehyde-3-phosphate-dehydrogenase
ScTEF1 Translational elongation factor EF-1 alpha
ScTPI1 Triose phosphate isomerase

'''