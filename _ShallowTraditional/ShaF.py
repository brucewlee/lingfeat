# -*- coding: UTF-8 -*-
"""
*** LingFeat - Comprehensive Linguistic Features for Readability Assessment
*** Shallow Features

References:
>>> Shallow features inspired by 
Publication 1: Feng, Lijun, Noémie Elhadad, and Matt Huenerfauth. "Cognitively motivated features for readability assessment." Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009). 2009.
"""
import re

def count_syllables(word:str):
    return len(
        re.findall('(?!e$)[aeiouy]+', word, re.I) +
        re.findall('^[^aeiouy]*e$', word, re.I)
    )

def retrieve(origin_doc, token_list, n_token, n_sent):
    total_count_char = len(origin_doc.replace(" ",""))
    total_count_tokn = n_token
    total_count_syll = 0
    for token in token_list:
        total_count_syll += count_syllables(token)
    result = {
        "TokSenM_S":float(n_token*n_sent),
        "as_Token_C":float(total_count_tokn/n_sent),
        "as_Sylla_C":float(total_count_syll/n_sent),  
        "at_Sylla_C":float(total_count_syll/n_token),       
        "as_Chara_C":float(total_count_char/n_sent),   
        "at_Chara_C":float(total_count_char/n_token),
    }
    return result