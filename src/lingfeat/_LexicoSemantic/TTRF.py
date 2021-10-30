# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: TTRF.py (Type-Token-Ratio Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Entity Density features inspired by 
Publication 1: Malvern, David, and Brian Richards. "Measures of lexical richness." The encyclopedia of applied linguistics (2012).
"""
import math
from lingfeat.utils import division
    
def retrieve(n_token,token_list):
    n_utoken = 1
    default_MTLD = 0.72
    MTLD_count = 0
    for token in token_list:
        if token_list.count(token) == 1:
            n_utoken += 1
        if float(n_utoken/n_token) >= 0.72:
            MTLD_count += 1

    result={
        "SimpTTR_S":float(n_utoken/n_token),
        "CorrTTR_S":float(n_utoken/math.sqrt(2*n_token)),
        "BiLoTTR_S":float(math.log(n_utoken)/math.log(n_token)),
        "UberTTR_S":float(division(((math.log(n_utoken))**2),(math.log(n_token/n_utoken)))),
        "MTLDTTR_S":float(MTLD_count)
    }
    return result