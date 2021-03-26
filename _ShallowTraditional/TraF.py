# -*- coding: UTF-8 -*-
"""
*** LingFeat - Comprehensive Linguistic Features for Readability Assessment 
*** Traditional Features
"""
import textstat as ts

def retrieve(origin_doc):
    FRE = ts.flesch_reading_ease(origin_doc)
    SMI = ts.smog_index(origin_doc)
    CML = ts.coleman_liau_index(origin_doc)
    DCR = ts.dale_chall_readability_score(origin_doc)
    GNF = ts.gunning_fog(origin_doc)
    ARI = ts.automated_readability_index(origin_doc)
    FKG = ts.flesch_kincaid_grade(origin_doc)
    LWF = ts.linsear_write_formula(origin_doc)
    result = {
        "FleschR_S":FRE,
        "SmogInd_S":SMI,
        "ColeLia_S":CML,
        "DaleCha_S":DCR,
        "Gunning_S":GNF,
        "AutoRea_S":ARI,
        "FleschG_S":FKG,
        "LinseaW_S":LWF,
    }
    return result