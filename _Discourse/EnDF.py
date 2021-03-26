# -*- coding: UTF-8 -*-
"""
*** LingFeat - Comprehensive Linguistic Features for Readability Assessment
*** Entity Density Features

References:
>>> Entity Density features inspired by 
Publication 1: Feng, Lijun, Noémie Elhadad, and Matt Huenerfauth. "Cognitively motivated features for readability assessment." Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009). 2009.
"""

def retrieve(NLP_doc, n_sent, n_token):
        to_EntiM_C = 0
        to_UEnti_C = 0
        ent_list = []
        unique_ent_list = []

        for ent in NLP_doc.ents:
            to_EntiM_C += 1
            ent_list.append(ent.text)
        
        for ent in ent_list:
            if ent_list.count(ent) == 1:
                to_UEnti_C += 1
                unique_ent_list.append(ent)

        result = {
            "to_EntiM_C": to_EntiM_C, 
            "as_EntiM_C": to_EntiM_C/n_sent, 
            "at_EntiM_C": to_EntiM_C/n_token,
            "to_UEnti_C": to_UEnti_C, 
            "as_UEnti_C": to_UEnti_C/n_sent,
            "at_UEnti_C": to_UEnti_C/n_token,
        }

        return result