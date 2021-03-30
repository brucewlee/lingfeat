# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: ShaF.py (Shallow Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Shallow features inspired by 
Publication 1: Feng, Lijun, Noémie Elhadad, and Matt Huenerfauth. "Cognitively motivated features for readability assessment." Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009). 2009.
"""
import math
from lingfeat.utils import count_syllables

def retrieve(origin_doc, token_list, n_token, n_sent):
    total_count_char = len(origin_doc.replace(" ",""))
    total_count_tokn = n_token
    total_count_syll = 0
    for token in token_list:
        total_count_syll += count_syllables(token)
    result = {
        "TokSenM_S":float(n_token*n_sent),
        "TokSenS_S":float(math.sqrt(n_token*n_sent)),
        "TokSenL_S":float(math.log(n_token)/math.log(n_sent)),
        "as_Token_C":float(total_count_tokn/n_sent),
        "as_Sylla_C":float(total_count_syll/n_sent),  
        "at_Sylla_C":float(total_count_syll/n_token),       
        "as_Chara_C":float(total_count_char/n_sent),   
        "at_Chara_C":float(total_count_char/n_token),
    }
    return result