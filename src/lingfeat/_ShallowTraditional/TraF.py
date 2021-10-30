# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: TraF.py (Traditional Formulas Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Shallow features inspired by 
Publication 1: Kincaid, J. Peter, Robert P. Fishburne Jr, Richard L. Rogers, and Brad S. Chissom. Derivation of new readability formulas (automated readability index, fog count and flesch reading ease formula) for navy enlisted personnel. Naval Technical Training Command Millington TN Research Branch, 1975.
Publication 2: Luo Si and Jamie Callan. 2001. A statistical model for scientific readability. In Proceedings of the tenth international conference on Information and knowledge management (CIKM '01). Association for Computing Machinery, New York, NY, USA, 574–576.
Publication 3: Eltorai, Adam EM, Syed S. Naqvi, Soha Ghanian, Craig P. Eberson, Arnold‐Peter C. Weiss, Christopher T. Born, and Alan H. Daniels. "Readability of invasive procedure consent forms." Clinical and translational science 8, no. 6 (2015): 830-833.
"""
import math
from lingfeat.utils import count_syllables

class formulas:
    def __init__(self, origin_doc, sent_token_list, n_sent, n_token):
        self.n_sent = n_sent
        self.n_token = n_token
        n_syll = 0
        n_char = 0
        n_diff_token = 0
        n_poly_token = 0
        SMOG_upper_bound = len(sent_token_list)-10
        SMOG_middle_bound1 = len(sent_token_list)/2 - 5
        SMOG_middle_bound2 = len(sent_token_list)/2 + 5
        for i,sent in enumerate(sent_token_list):
            for token in sent:
                syll_this_token = count_syllables(token)
                n_syll += syll_this_token
                if syll_this_token >= 3:
                    n_diff_token += 1
                if syll_this_token >= 2:
                    if n_sent <= 30:
                        n_poly_token += 1
                    else:
                        if i <= 10 or i >= SMOG_upper_bound or SMOG_middle_bound1 <= i <= SMOG_middle_bound2:
                            n_poly_token += 1
                n_char += len(token)

        self.n_syll = n_syll
        self.n_char = n_char
        self.n_diff_token = n_diff_token
        self.n_easy_token = n_token - n_diff_token
        self.n_poly_token = n_poly_token

    # follow "new" automated readability index in reference 1
    def automated_readability_index(self):
        result = 0.37*(self.n_token/self.n_sent)+5.84*(self.n_char/self.n_token)-26.01
        return result
    
    # follow "new" fog count in reference 1
    def fog_count(self):
        result = ((self.n_easy_token + 3*(self.n_diff_token))/self.n_sent - 3)/2
        return result

    """
    # follow "old" flesch reading ease in reference 1
    def flesch_reading_ease(self):
        result = 206.835 - 1.015(self.n_token/self.n_sent) - 0.836(self.n_syll/(self.n_token/100))
        return result
    """

    # follow "new" flesch reading ease in reference 1
    def flesch_grade_level(self):
        result = 0.39*(self.n_token/self.n_sent) + 11.8*(self.n_syll/self.n_token) - 15.59
        return result

    # follow reference 2
    def smog_index(self):
        result = math.sqrt(self.n_poly_token)
        return result
    
    # follow reference 3
    def coleman_liau_index(self):
        result = 0.0588*(self.n_token/100) - 0.00296*(self.n_sent) - 15.8
        return result
    
    # follow reference 3
    def linsear_write_formula(self):
        result = (self.n_easy_token + 3*(self.n_diff_token))/self.n_sent
        if result > 10:
            result /= 2
        else:
            result -= 2
            result /= 2
        return result
    

def retrieve(origin_doc, sent_token_list, n_sent, n_token):
    Formulas = formulas(origin_doc, sent_token_list, n_sent, n_token)
    SMI = Formulas.smog_index()
    CML = Formulas.coleman_liau_index()
    GNF = Formulas.fog_count()
    ARI = Formulas.automated_readability_index()
    FKG = Formulas.flesch_grade_level()
    LWF = Formulas.linsear_write_formula()
    result = {
        "FleschG_S":FKG,
        "AutoRea_S":ARI,
        "ColeLia_S":CML,
        "SmogInd_S":SMI,
        "Gunning_S":GNF,
        "LinseaW_S":LWF,
    }
    return result