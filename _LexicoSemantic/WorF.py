# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: WorF.py (Word Frequency Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Word Frequency features inspired by 
Publication 1: Vajjala, Sowmya, and Detmar Meurers. "Readability-based sentence ranking for evaluating text simplification." (2015).
"""

import pandas as pd

def retrieve(token_list, n_token, n_sent, dir_path):
    to_SbFrQ_C = 0
    to_SbCDC_C = 0
    to_SbFrL_C = 0
    to_SbCDL_C = 0
    to_SbSBW_C = 0
    to_SbL1W_C = 0
    to_SbSBC_C = 0
    to_SbL1C_C = 0

    DB = pd.read_csv(dir_path+'/_LexicoSemantic/resources/SUBTLEXus.csv')
    DB.set_index('Word_lowercased', inplace=True, drop=True)
    for token in token_list:
        if token in DB.index:
            scores_for_this_token = list(DB.loc[token, :])
            for i, score in enumerate(scores_for_this_token):
                scores_for_this_token[i] = 0 if str(score) == 'none' else scores_for_this_token[i]
            to_SbFrQ_C += float(scores_for_this_token[1])
            to_SbCDC_C += float(scores_for_this_token[2])
            to_SbFrL_C += float(scores_for_this_token[3])
            to_SbCDL_C += float(scores_for_this_token[4])
            to_SbSBW_C += float(scores_for_this_token[5])
            to_SbL1W_C += float(scores_for_this_token[6])
            to_SbSBC_C += float(scores_for_this_token[7])
            to_SbL1C_C += float(scores_for_this_token[8])

    result = {
        "to_SbFrQ_C": to_SbFrQ_C,
        "as_SbFrQ_C": to_SbFrQ_C/n_sent ,
        "at_SbFrQ_C": to_SbFrQ_C/n_token,
        "to_SbCDC_C": to_SbCDC_C,
        "as_SbCDC_C": to_SbCDC_C/n_sent ,
        "at_SbCDC_C": to_SbCDC_C/n_token,
        "to_SbFrL_C": to_SbFrL_C,
        "as_SbFrL_C": to_SbFrL_C/n_sent ,
        "at_SbFrL_C": to_SbFrL_C/n_token,
        "to_SbCDL_C": to_SbCDL_C,
        "as_SbCDL_C": to_SbCDL_C/n_sent ,
        "at_SbCDL_C": to_SbCDL_C/n_token,
        "to_SbSBW_C": to_SbSBW_C,
        "as_SbSBW_C": to_SbSBW_C/n_sent ,
        "at_SbSBW_C": to_SbSBW_C/n_token,
        "to_SbL1W_C": to_SbL1W_C,
        "as_SbL1W_C": to_SbL1W_C/n_sent ,
        "at_SbL1W_C": to_SbL1W_C/n_token,
        "to_SbSBC_C": to_SbSBC_C,
        "as_SbSBC_C": to_SbSBC_C/n_sent ,
        "at_SbSBC_C": to_SbSBC_C/n_token,
        "to_SbL1C_C": to_SbL1C_C,
        "as_SbL1C_C": to_SbL1C_C/n_sent ,
        "at_SbL1C_C": to_SbL1C_C/n_token,
    }
    return result  