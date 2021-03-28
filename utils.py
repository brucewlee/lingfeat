import re

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