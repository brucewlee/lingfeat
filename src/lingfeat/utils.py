"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: utils.py
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -
"""
import re
import math

def division(x, y):
    try:
        result = x/y
    except:
        result = 0
    return result

def nan_check(result):
    for key in result:
        if math.isnan(float(result[key])):
            result[key] = 0
    return result

def count_syllables(word:str):
        return len(
        re.findall('(?!e$)[aeiouy]+', word, re.I) +
        re.findall('^[^aeiouy]*e$', word, re.I)
    )