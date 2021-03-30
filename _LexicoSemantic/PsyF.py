# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: PstF.py (Psycholinguistic Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Psycholinguistic features inspired by 
Publication 1: Kuperman, Victor, Hans Stadthagen-Gonzalez, and Marc Brysbaert. "Age-of-acquisition ratings for 30,000 English words." Behavior research methods 44.4 (2012): 978-990.
Publication 2: Vajjala, Sowmya, and Detmar Meurers. "Readability-based sentence ranking for evaluating text simplification." (2015).
"""

import pandas as pd

def retrieve(token_list, n_token, n_sent, dir_path):
    to_AAKuW_C = 0
    to_AAKuL_C = 0
    to_AABiL_C = 0
    to_AABrL_C = 0
    to_AACoL_C = 0

    DB = pd.read_csv(dir_path+'/_LexicoSemantic/resources/AoAKuperman.csv')
    DB.set_index('Word', inplace=True, drop=True)
    for token in token_list:
        if token in DB.index:
            scores_for_this_token = list(DB.loc[token, :])
            for i, score in enumerate(scores_for_this_token):
                scores_for_this_token[i] = 0 if str(score) == 'none' else scores_for_this_token[i]
            to_AAKuW_C += float(scores_for_this_token[7])
            to_AAKuL_C += float(scores_for_this_token[9])
            to_AABiL_C += float(scores_for_this_token[11])
            to_AABrL_C += float(scores_for_this_token[12])
            to_AACoL_C += float(scores_for_this_token[13])

    result = {
        "to_AAKuW_C": to_AAKuW_C,
        "as_AAKuW_C": to_AAKuW_C/n_sent ,
        "at_AAKuW_C": to_AAKuW_C/n_token,
        "to_AAKuL_C": to_AAKuL_C,
        "as_AAKuL_C": to_AAKuL_C/n_sent ,
        "at_AAKuL_C": to_AAKuL_C/n_token,
        "to_AABiL_C": to_AABiL_C,
        "as_AABiL_C": to_AABiL_C/n_sent ,
        "at_AABiL_C": to_AABiL_C/n_token,
        "to_AABrL_C": to_AABrL_C,
        "as_AABrL_C": to_AABrL_C/n_sent ,
        "at_AABrL_C": to_AABrL_C/n_token,
        "to_AACoL_C": to_AABrL_C,
        "as_AACoL_C": to_AABrL_C/n_sent ,
        "at_AACoL_C": to_AABrL_C/n_token,
    }
    return result   