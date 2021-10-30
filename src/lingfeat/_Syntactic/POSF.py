# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: POSF.py (Part-of-Speech Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -

References:
>>> Part-of-Speech features inspired by 
Publication 1: Feng, Lijun, Noémie Elhadad, and Matt Huenerfauth. "Cognitively motivated features for readability assessment." Proceedings of the 12th Conference of the European Chapter of the ACL (EACL 2009). 2009.
"""

from lingfeat.utils import division
    
def retrieve(NLP_doc, n_token, n_sent):
    to_NoTag_C = 0
    to_VeTag_C = 0
    to_AjTag_C = 0
    to_AvTag_C = 0
    to_SuTag_C = 0
    to_CoTag_C = 0
    to_ContW_C = 0
    to_FuncW_C = 0

    for token in NLP_doc:
        if token.pos_ == "NOUN" or token.pos_ == "VERB" or token.pos_ == "NUM" or token.pos_ == "ADJ" or token.pos_ == "ADV":
            to_ContW_C += 1
        else:
            to_FuncW_C += 1

        if token.pos_ == "NOUN":
            to_NoTag_C += 1
        if token.pos_ == "VERB":
            to_VeTag_C += 1
        if token.pos_ == "ADJ":
            to_AjTag_C += 1
        if token.pos_ == "ADV":
            to_AvTag_C += 1
        if token.pos_ == "SCONJ":
            to_SuTag_C += 1
        if token.pos_ == "CCONJ":
            to_CoTag_C += 1
    
    result = {
        "to_NoTag_C":float(to_NoTag_C),
        "as_NoTag_C":float(division(to_NoTag_C,n_sent)),
        "at_NoTag_C":float(division(to_NoTag_C,n_token)),
        "ra_NoAjT_C":float(division(to_NoTag_C,to_AjTag_C)),
        "ra_NoVeT_C":float(division(to_NoTag_C,to_VeTag_C)),
        "ra_NoAvT_C":float(division(to_NoTag_C,to_AvTag_C)),
        "ra_NoSuT_C":float(division(to_NoTag_C,to_SuTag_C)),
        "ra_NoCoT_C":float(division(to_NoTag_C,to_CoTag_C)),
        "to_VeTag_C":float(to_VeTag_C),
        "as_VeTag_C":float(division(to_VeTag_C,n_sent)),
        "at_VeTag_C":float(division(to_VeTag_C,n_token)),
        "ra_VeAjT_C":float(division(to_VeTag_C,to_AjTag_C)),
        "ra_VeNoT_C":float(division(to_VeTag_C,to_NoTag_C)),
        "ra_VeAvT_C":float(division(to_VeTag_C,to_AvTag_C)),
        "ra_VeSuT_C":float(division(to_VeTag_C,to_SuTag_C)),
        "ra_VeCoT_C":float(division(to_VeTag_C,to_CoTag_C)),
        "to_AjTag_C":float(to_AjTag_C),
        "as_AjTag_C":float(division(to_AjTag_C,n_sent)),
        "at_AjTag_C":float(division(to_AjTag_C,n_token)),
        "ra_AjNoT_C":float(division(to_AjTag_C,to_NoTag_C)),
        "ra_AjVeT_C":float(division(to_AjTag_C,to_VeTag_C)),
        "ra_AjAvT_C":float(division(to_AjTag_C,to_AvTag_C)),
        "ra_AjSuT_C":float(division(to_AjTag_C,to_SuTag_C)),
        "ra_AjCoT_C":float(division(to_AjTag_C,to_CoTag_C)),
        "to_AvTag_C":float(to_AvTag_C),
        "as_AvTag_C":float(division(to_AvTag_C,n_sent)),
        "at_AvTag_C":float(division(to_AvTag_C,n_token)),
        "ra_AvAjT_C":float(division(to_AvTag_C,to_AjTag_C)),
        "ra_AvNoT_C":float(division(to_AvTag_C,to_NoTag_C)),
        "ra_AvVeT_C":float(division(to_AvTag_C,to_VeTag_C)),
        "ra_AvSuT_C":float(division(to_AvTag_C,to_SuTag_C)),
        "ra_AvCoT_C":float(division(to_AvTag_C,to_CoTag_C)),
        "to_SuTag_C":float(to_SuTag_C),
        "as_SuTag_C":float(division(to_SuTag_C,n_sent)),
        "at_SuTag_C":float(division(to_SuTag_C,n_token)),
        "ra_SuAjT_C":float(division(to_SuTag_C,to_AjTag_C)),
        "ra_SuNoT_C":float(division(to_SuTag_C,to_NoTag_C)),
        "ra_SuVeT_C":float(division(to_SuTag_C,to_VeTag_C)),
        "ra_SuAvT_C":float(division(to_SuTag_C,to_AvTag_C)),
        "ra_SuCoT_C":float(division(to_SuTag_C,to_CoTag_C)),
        "to_CoTag_C":float(to_CoTag_C),
        "as_CoTag_C":float(division(to_CoTag_C,n_sent)),
        "at_CoTag_C":float(division(to_CoTag_C,n_token)),
        "ra_CoAjT_C":float(division(to_CoTag_C,to_AjTag_C)),
        "ra_CoNoT_C":float(division(to_CoTag_C,to_NoTag_C)),
        "ra_CoVeT_C":float(division(to_CoTag_C,to_VeTag_C)),
        "ra_CoAvT_C":float(division(to_CoTag_C,to_AvTag_C)),
        "ra_CoSuT_C":float(division(to_CoTag_C,to_SuTag_C)),
        "to_ContW_C":float(to_ContW_C),
        "as_ContW_C":float(division(to_ContW_C,n_sent)),
        "at_ContW_C":float(division(to_ContW_C,n_token)),
        "to_FuncW_C":float(to_FuncW_C),
        "as_FuncW_C":float(division(to_FuncW_C,n_sent)),
        "at_FuncW_C":float(division(to_FuncW_C,n_token)),
        "ra_CoFuW_C":float(division(to_ContW_C,to_FuncW_C)), 
    }
    return result