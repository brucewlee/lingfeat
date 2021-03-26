# -*- coding: UTF-8 -*-
"""
*** LingFeat - Comprehensive Linguistic Features for Readability Assessment
*** Tree Structure Features

References:
>>> Tree Structure features inspired by 
Publication 1: Schwarm, Sarah E., and Mari Ostendorf. "Reading level assessment using support vector machines and statistical language models." Proceedings of the 43rd Annual Meeting of the Association for Computational Linguistics (ACL’05). 2005.
"""

import nltk
from lingfeat.utils import division

def retrieve(SuPar, sent_token_list, n_token, n_sent):
    to_TreeH_C = 0
    to_FTree_C = 0
    for sent in sent_token_list:
        dataset = SuPar.predict([sent], prob=True, verbose=False)
        parsed_tree = dataset.sentences
        nltk_tree = nltk.Tree.fromstring(str(parsed_tree[0]))
        to_TreeH_C += int(nltk_tree.height())
        to_FTree_C += len(nltk_tree.flatten())
    result = {
        "to_TreeH_C": to_TreeH_C,
        "as_TreeH_C": float(division(to_TreeH_C,n_sent)),
        "at_TreeH_C": float(division(to_TreeH_C,n_token)),
        "to_FTree_C": to_FTree_C,
        "as_FTree_C": float(division(to_FTree_C,n_sent)),
        "at_FTree_C": float(division(to_FTree_C,n_token)),
    }
    return result