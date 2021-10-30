# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: WoKF.py (Wiki Knowledge Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -
"""

import gensim
from lingfeat.utils import division

def richness(probability_list):
    sum_ = 0
    for idx, number in enumerate(probability_list):
        sum_ += float((idx+1)*number)
    return sum_


def clarity(probability_list):
    sum_ = 0
    for number in probability_list[1:]:
        sum_ += (probability_list[0] - number)
    result = division(sum_,len(probability_list))
    if len(probability_list) == 1:
        result = probability_list[0]
    return result


def noise(probability_list):
    mean = float(1.0/len(probability_list))
    s2 = 0
    s4 = 0
    for number in probability_list:
        s2 += (number - mean)**2
        s4 += (number - mean)**4

    result = len(probability_list)*(division(s4,(s2)**2))

    return result


def get_probability_lists(token_list, dir_path):
    n_topic_list = [50, 100, 150, 200]

    # lda_list is a list of Gensim lda objects
    lda_list = []

    # probability_lists is a list of list. 
    # [[probability list at topic 50],[probability list at topic 100],[probability list at topic 150],[probability list at topic 200]]
    probability_lists = []

    common_dictionary = gensim.corpora.dictionary.Dictionary([token_list])
    common_corpus = [common_dictionary.doc2bow(token_list)]

    for n_topic in n_topic_list:
        lda_list.append(gensim.models.ldamodel.LdaModel.load(dir_path+"/_AdvancedSemantic/model/enwiki" + str(n_topic)))

    probability_list = []
    for lda in lda_list:
        for topic_probability in lda.get_document_topics(common_corpus)[0]:
            probability_list.append(topic_probability[1])
            probability_list = sorted(probability_list, reverse=True)
        probability_lists.append(probability_list)
    return probability_lists


def retrieve(token_list, dir_path):
    n_topic_list_for_naming = ["05", "10", "15", "20"]
    probability_lists = get_probability_lists(token_list, dir_path)

    # obtain each feature list
    richness_list = []
    clarity_list = []
    noise_list = []
    n_topics_list = []
    for probability_list in probability_lists:
        richness_list.append(richness(probability_list))
        clarity_list.append(clarity(probability_list))
        noise_list.append(noise(probability_list))
        n_topics_list.append(len(probability_list))
    
    # make resulting dictionary
    result = {}
    for i,feature in enumerate(richness_list):
        result["WRich"+n_topic_list_for_naming[i]+"_S"] = feature
    for i,feature in enumerate(clarity_list):
        result["WClar"+n_topic_list_for_naming[i]+"_S"] = feature
    for i,feature in enumerate(noise_list):
        result["WNois"+n_topic_list_for_naming[i]+"_S"] = feature
    for i,feature in enumerate(n_topics_list):
        result["WTopc"+n_topic_list_for_naming[i]+"_S"] = feature
    
    return result