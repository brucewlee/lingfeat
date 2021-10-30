# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: PhrF.py (Phrasal Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -

References:
>>> Phrasal features inspired by 
Publication 1: Feng, Lijun, Martin Jansche, Matt Huenerfauth, and Noémie Elhadad. "A Comparison of Features for Automatic Readability Assessment." In Coling 2010: Posters, pp. 276-284. 2010.
Publication 2: Lu, Xiaofei. "Automatic analysis of syntactic complexity in second language writing." International journal of corpus linguistics 15, no. 4 (2010): 474-496.
"""
from lingfeat.utils import division

def retrieve(SuPar, sent_token_list, n_token, n_sent):
    to_NoPhr_C = 0
    to_VePhr_C = 0
    to_SuPhr_C = 0
    to_PrPhr_C = 0
    to_AjPhr_C = 0
    to_AvPhr_C = 0
    for sent in sent_token_list:

        dataset = SuPar.predict([sent], prob=True, verbose=False)
        parsed_tree = str(dataset.sentences)
        to_NoPhr_C += parsed_tree.count("NP")
        to_VePhr_C += parsed_tree.count("VP")
        to_SuPhr_C += parsed_tree.count("SBAR")
        to_PrPhr_C += parsed_tree.count("PP")
        to_AjPhr_C += parsed_tree.count("ADJP")
        to_AvPhr_C += parsed_tree.count("ADVP")
    result = {
        "to_NoPhr_C": to_NoPhr_C,
        "as_NoPhr_C": float(division(to_NoPhr_C,n_sent)),
        "at_NoPhr_C": float(division(to_NoPhr_C,n_token)),
        "ra_NoVeP_C": float(division(to_NoPhr_C,to_VePhr_C)),
        "ra_NoSuP_C": float(division(to_NoPhr_C,to_SuPhr_C)),
        "ra_NoPrP_C": float(division(to_NoPhr_C,to_PrPhr_C)),
        "ra_NoAjP_C": float(division(to_NoPhr_C,to_AjPhr_C)),
        "ra_NoAvP_C": float(division(to_NoPhr_C,to_AvPhr_C)),

        "to_VePhr_C": to_VePhr_C,
        "as_VePhr_C": float(division(to_VePhr_C,n_sent)),
        "at_VePhr_C": float(division(to_VePhr_C,n_token)),
        "ra_VeNoP_C": float(division(to_VePhr_C,to_NoPhr_C)),
        "ra_VeSuP_C": float(division(to_VePhr_C,to_SuPhr_C)),
        "ra_VePrP_C": float(division(to_VePhr_C,to_PrPhr_C)),
        "ra_VeAjP_C": float(division(to_VePhr_C,to_AjPhr_C)),
        "ra_VeAvP_C": float(division(to_VePhr_C,to_AvPhr_C)),

        "to_SuPhr_C": to_SuPhr_C,
        "as_SuPhr_C": float(division(to_SuPhr_C,n_sent)),
        "at_SuPhr_C": float(division(to_SuPhr_C,n_token)),
        "ra_SuNoP_C": float(division(to_SuPhr_C,to_NoPhr_C)),
        "ra_SuVeP_C": float(division(to_SuPhr_C,to_VePhr_C)),
        "ra_SuPrP_C": float(division(to_SuPhr_C,to_PrPhr_C)),
        "ra_SuAjP_C": float(division(to_SuPhr_C,to_AjPhr_C)),
        "ra_SuAvP_C": float(division(to_SuPhr_C,to_AvPhr_C)),

        "to_PrPhr_C": to_PrPhr_C,
        "as_PrPhr_C": float(division(to_PrPhr_C,n_sent)),
        "at_PrPhr_C": float(division(to_PrPhr_C,n_token)),
        "ra_PrNoP_C": float(division(to_PrPhr_C,to_NoPhr_C)),
        "ra_PrVeP_C": float(division(to_PrPhr_C,to_VePhr_C)),
        "ra_PrSuP_C": float(division(to_PrPhr_C,to_SuPhr_C)),
        "ra_PrAjP_C": float(division(to_PrPhr_C,to_AjPhr_C)),
        "ra_PrAvP_C": float(division(to_PrPhr_C,to_AvPhr_C)),

        "to_AjPhr_C": to_AjPhr_C,
        "as_AjPhr_C": float(division(to_AjPhr_C,n_sent)),
        "at_AjPhr_C": float(division(to_AjPhr_C,n_token)),
        "ra_AjNoP_C": float(division(to_AjPhr_C,to_NoPhr_C)),
        "ra_AjVeP_C": float(division(to_AjPhr_C,to_VePhr_C)),
        "ra_AjSuP_C": float(division(to_AjPhr_C,to_SuPhr_C)),
        "ra_AjPrP_C": float(division(to_AjPhr_C,to_PrPhr_C)),
        "ra_AjAvP_C": float(division(to_AjPhr_C,to_AvPhr_C)),

        "to_AvPhr_C": to_AvPhr_C,
        "as_AvPhr_C": float(division(to_AvPhr_C,n_sent)),
        "at_AvPhr_C": float(division(to_AvPhr_C,n_token)),
        "ra_AvNoP_C": float(division(to_AvPhr_C,to_NoPhr_C)),
        "ra_AvVeP_C": float(division(to_AvPhr_C,to_VePhr_C)),
        "ra_AvSuP_C": float(division(to_AvPhr_C,to_SuPhr_C)),
        "ra_AvPrP_C": float(division(to_AvPhr_C,to_PrPhr_C)),
        "ra_AvAjP_C": float(division(to_AvPhr_C,to_AjPhr_C)),
    }
    return result







