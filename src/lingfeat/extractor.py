# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: extractor.py
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -
"""

# utilities
import math
import os
import warnings
import logging
import tqdm
def nop(it, *a, **k):
    return it
tqdm.tqdm = nop
from lingfeat.utils import nan_check

# performance-central dependencies
import spacy 
import supar
from supar import Parser
import gensim # for World Knowledge Features

# advanced Semantic features
import lingfeat._AdvancedSemantic.WoKF as AdSem_WoKF
import lingfeat._AdvancedSemantic.WBKF as AdSem_WBKF
import lingfeat._AdvancedSemantic.OSKF as AdSem_OSKF

# discourse features
import lingfeat._Discourse.EnDF as Disco_EnDF
import lingfeat._Discourse.EnGF as Disco_EnGF

# syntactic features
import lingfeat._Syntactic.POSF as Synta_POSF
import lingfeat._Syntactic.PhrF as Synta_PhrF
import lingfeat._Syntactic.TrSF as Synta_TrSF

# lexico-Semantic features
import lingfeat._LexicoSemantic.TTRF as LxSem_TTRF
import lingfeat._LexicoSemantic.VarF as LxSem_VarF
import lingfeat._LexicoSemantic.PsyF as LxSem_PsyF
import lingfeat._LexicoSemantic.WorF as LxSem_WorF

# shallow features
import lingfeat._ShallowTraditional.ShaF as ShaTr_ShaF
import lingfeat._ShallowTraditional.TraF as ShaTr_TraF

# ignore warning
warnings.filterwarnings("ignore")

# current path
dir_path = os.path.dirname(os.path.realpath(__file__))

# load models
NLP = spacy.load('en_core_web_sm')
SuPar = Parser.load('crf-con-en')


class pass_text:
    
    """
    Initialize pipeline

    input :
    - text: original input text to analyze

    saves :
    - self.origin_doc
    - self.NLP_doc: spacy pipeline object
    """
    def __init__(self, text:str):
        self.NLP_doc = NLP(text)
        self.origin_doc = text



    """
    Preprocess given text, count tokens & sentences
    ** throughout this program, only n_token and n_sent are defaulted at 1 to prevent division error

    input :
    - short (default False): include shorts words of under 3 letters
    - see_token (default False): return token_list
    - see_sent_token (default False): return sent_token_list

    saves :
    - self.n_token
    - self.n_sent
    - self.token_list: lemmatized token list, only alphabets
    - self.sent_token_list: token list, no lemmatization, list of list in sentence

    output:
    - n_token
    - n_sent
    - token_list (optional)
    - sent_token_list (optional)
    """
    def preprocess(self, short=False, see_token=False, see_sent_token=False):
        n_token = 1
        n_sent = 1
        token_list = []
        raw_token_list = []
        sent_token_list = []

        # sent_list is for raw string sentences
        sent_list = []

        # count tokens, sentence + make lists
        for sent in self.NLP_doc.sents:
            n_sent += 1
            sent_list.append(sent.text)
            temp_list = []
            for token in sent:
                if token.text.isalpha():
                    temp_list.append(token.text)
                    if short == True:
                        n_token += 1
                        token_list.append(token.lemma_.lower())
                    if short == False:
                        if len(token.text) >= 3:
                            n_token += 1
                            token_list.append(token.lemma_.lower())
            if len(temp_list) > 3:
                sent_token_list.append(temp_list)

        self.n_token = n_token 
        self.n_sent = n_sent
        self.token_list = token_list
        self.sent_token_list = sent_token_list
        
        result = {"n_token": self.n_token, 
                    "n_sent": self.n_sent
                    }

        if see_token == True:
            result["token"] = token_list
        if see_sent_token == True:
            result["sent_token"] = sent_token_list

        return result



    """
    Extract World Knowledge Features -> 12

    output (type -> dictionary): 
    - WRich05_S: Semantic Richness, 50 topics extracted from Wikipedia
    - WClar05_S: Semantic Clarity, 50 topics extracted from Wikipedia
    - WNois05_S: Semantic Noise, 50 topics extracted from Wikipedia
    - WTopc05_S: Number of topics, 50 topics extracted from Wikipedia
    - WRich10_S: Semantic Richness, 100 topics extracted from Wikipedia
    - WClar10_S: Semantic Clarity, 100 topics extracted from Wikipedia
    - WNois10_S: Semantic Noise, 100 topics extracted from Wikipedia
    - WTopc10_S: Number of topics, 100 topics extracted from Wikipedia
    - WRich15_S: Semantic Richness, 150 topics extracted from Wikipedia
    - WClar15_S: Semantic Clarity, 150 topics extracted from Wikipedia
    - WNois15_S: Semantic Noise, 150 topics extracted from Wikipedia
    - WTopc15_S: Number of topics, 150 topics extracted from Wikipedia
    - WRich20_S: Semantic Richness, 200 topics extracted from Wikipedia
    - WClar20_S: Semantic Clarity, 200 topics extracted from Wikipedia
    - WNois20_S: Semantic Noise, 200 topics extracted from Wikipedia
    - WTopc20_S: Number of topics, 200 topics extracted from Wikipedia
    """
    def WoKF_(self):
        result = AdSem_WoKF.retrieve(self.token_list, dir_path)
        result = nan_check(result)
        return result



    """
    Extract WeeBit Corpus Knowledge Features -> 12

    output (type -> dictionary): 
    - BRich05_S: Semantic Richness, 50 topics extracted from WeeBit Corpus
    - BClar05_S: Semantic Clarity, 50 topics extracted from WeeBit Corpus
    - BNois05_S: Semantic Noise, 50 topics extracted from WeeBit Corpus
    - BTopc05_S: Number of topics, 50 topics extracted from WeeBit Corpus
    - BRich10_S: Semantic Richness, 100 topics extracted from WeeBit Corpus
    - BClar10_S: Semantic Clarity, 100 topics extracted from WeeBit Corpus
    - BNois10_S: Semantic Noise, 100 topics extracted from WeeBit Corpus
    - BTopc10_S: Number of topics, 100 topics extracted from WeeBit Corpus
    - BRich15_S: Semantic Richness, 150 topics extracted from WeeBit Corpus
    - BClar15_S: Semantic Clarity, 150 topics extracted from WeeBit Corpus
    - BNois15_S: Semantic Noise, 150 topics extracted from WeeBit Corpus
    - BTopc15_S: Number of topics, 150 topics extracted from WeeBit Corpus
    - BRich20_S: Semantic Richness, 200 topics extracted from WeeBit Corpus
    - BClar20_S: Semantic Clarity, 200 topics extracted from WeeBit Corpus
    - BNois20_S: Semantic Noise, 200 topics extracted from WeeBit Corpus
    - BTopc20_S: Number of topics, 200 topics extracted from WeeBit Corpus
    """
    def WBKF_(self):
        result = AdSem_WBKF.retrieve(self.token_list, dir_path)
        result = nan_check(result)
        return result



    """
    Extract OneStopEng Corpus Knowledge Features -> 12

    output (type -> dictionary): 
    - ORich05_S: Semantic Richness, 50 topics extracted from OneStopEng Corpus
    - OClar05_S: Semantic Clarity, 50 topics extracted from OneStopEng Corpus
    - ONois05_S: Semantic Noise, 50 topics extracted from OneStopEng Corpus
    - OTopc05_S: Number of topics, 50 topics extracted from OneStopEng Corpus
    - ORich10_S: Semantic Richness, 100 topics extracted from OneStopEng Corpus
    - OClar10_S: Semantic Clarity, 100 topics extracted from OneStopEng Corpus
    - ONois10_S: Semantic Noise, 100 topics extracted from OneStopEng Corpus
    - OTopc10_S: Number of topics, 100 topics extracted from OneStopEng Corpus
    - ORich15_S: Semantic Richness, 150 topics extracted from OneStopEng Corpus
    - OClar15_S: Semantic Clarity, 150 topics extracted from OneStopEng Corpus
    - ONois15_S: Semantic Noise, 150 topics extracted from OneStopEng Corpus
    - OTopc15_S: Number of topics, 150 topics extracted from OneStopEng Corpus
    - ORich20_S: Semantic Richness, 200 topics extracted from OneStopEng Corpus
    - OClar20_S: Semantic Clarity, 200 topics extracted from OneStopEng Corpus
    - ONois20_S: Semantic Noise, 200 topics extracted from OneStopEng Corpus
    - OTopc20_S: Number of topics, 200 topics extracted from OneStopEng Corpus
    """
    def OSKF_(self):
        result = AdSem_OSKF.retrieve(self.token_list, dir_path)
        result = nan_check(result)
        return result



    """
    Extract Entity Density Features -> 6

    output (type -> dictionary): 
    - to_EntiM_C: total count of Entities Mentions counts
    - as_EntiM_C: average count of Entities Mentions counts per sentence
    - at_EntiM_C: average count of Entities Mentions counts per token (word)
    - to_UEnti_C: total count of unique Entities
    - as_UEnti_C: average count of unique Entities per sentence
    - at_UEnti_C: average count of unique Entities per token (word)
    """
    def EnDF_(self):
        result = Disco_EnDF.retrieve(self.NLP_doc, self.n_sent, self.n_token)
        result = nan_check(result)
        return result
    


    """
    Extract Entity Grid Features -> 22

    output (type -> dictionary):
    - ra_SSToT_C: ratio of ss transitions to total
    - ra_SOToT_C: ratio of so transitions to total
    - ra_SXToT_C: ratio of sx transitions to total
    - ra_SNToT_C: ratio of sn transitions to total
    - ra_OSToT_C: ratio of os transitions to total
    - ra_OOToT_C: ratio of oo transitions to total
    - ra_OXToT_C: ratio of ox transitions to total
    - ra_ONToT_C: ratio of on transitions to total
    - ra_XSToT_C: ratio of xs transitions to total
    - ra_XOToT_C: ratio of xo transitions to total
    - ra_XXToT_C: ratio of xx transitions to total
    - ra_XNToT_C: ratio of xn transitions to total
    - ra_NSToT_C: ratio of ns transitions to total
    - ra_NOToT_C: ratio of no transitions to total
    - ra_NXToT_C: ratio of nx transitions to total
    - ra_NNToT_C: ratio of nn transitions to total
    - LoCohPA_S: Local Coherence for PA score
    - LoCohPW_S: Local Coherence for PW score
    - LoCohPU_S: Local Coherence for PU score
    - LoCoDPA_S: Local Coherence distance for PA score    
    - LoCoDPW_S: Local Coherence distance for PW score    
    - LoCoDPU_S: Local Coherence distance for PU score    
    """
    def EnGF_(self):
        """
        if self.n_sent <= 2:
            raise RuntimeError(
                "\n|-.-'-.- LingFeat -.-'-.-|\n"
                +"Error Raised:\n"
                +"This problem might be caused due to the following reasons.\n"
                +"1.Entity Grid needs at least two sentences, found: {}.\n".format(self.n_sent))
        else:
        """
        result = Disco_EnGF.EntityGrid(self.NLP_doc, n_sent=self.n_sent).retrieve()
        result = nan_check(result)
        return result



    """
    Extract Phrasal Features -> 48

    output (type -> dictionary): 
    - to_NoPhr_C: total count of Noun phrases
    - as_NoPhr_C: average count of Noun phrases per sentence
    - at_NoPhr_C: average count of Noun phrases per token
    - ra_NoVeP_C: ratio of Noun phrases count to Verb phrases count
    - ra_NoSuP_C: ratio of Noun phrases count to Subordinate Clauses count
    - ra_NoPrP_C: ratio of Noun phrases count to Prep phrases count
    - ra_NoAjP_C: ratio of Noun phrases count to Adj phrases count
    - ra_NoAvP_C: ratio of Noun phrases count to Adv phrases count

    - to_VePhr_C: total count of Verb phrases
    - as_VePhr_C: average count of Verb phrases per sentence
    - at_VePhr_C: average count of Verb phrases per token
    - ra_VeNoP_C: ratio of Verb phrases count to Noun phrases count
    - ra_VeSuP_C: ratio of Verb phrases count to Subordinate Clauses count
    - ra_VePrP_C: ratio of Verb phrases count to Prep phrases count
    - ra_VeAjP_C: ratio of Verb phrases count to Adj phrases count
    - ra_VeAvP_C: ratio of Verb phrases count to Adv phrases count

    - to_SuPhr_C: total count of Subordinate Clauses
    - as_SuPhr_C: average count of Subordinate Clauses per sentence
    - at_SuPhr_C: average count of Subordinate Clauses per token
    - ra_SuNoP_C: ratio of Subordinate Clauses count to Noun phrases count
    - ra_SuVeP_C: ratio of Subordinate Clauses count to Verb phrases count
    - ra_SuPrP_C: ratio of Subordinate Clauses count to Prep phrases count
    - ra_SuAjP_C: ratio of Subordinate Clauses count to Adj phrases count
    - ra_SuAvP_C: ratio of Subordinate Clauses count to Adv phrases count

    - to_PrPhr_C: total count of prepositional phrases
    - as_PrPhr_C: average count of prepositional phrases per sentence
    - at_PrPhr_C: average count of prepositional phrases per token
    - ra_PrNoP_C: ratio of Prep phrases count to Noun phrases count
    - ra_PrVeP_C: ratio of Prep phrases count to Verb phrases count
    - ra_PrSuP_C: ratio of Prep phrases count to Subordinate Clauses count
    - ra_PrAjP_C: ratio of Prep phrases count to Adj phrases count
    - ra_PrAvP_C: ratio of Prep phrases count to Adv phrases count

    - to_AjPhr_C: total count of Adjective phrases
    - as_AjPhr_C: average count of Adjective phrases per sentence
    - at_AjPhr_C: average count of Adjective phrases per token
    - ra_AjNoP_C: ratio of Adj phrases count to Noun phrases count
    - ra_AjVeP_C: ratio of Adj phrases count to Verb phrases count
    - ra_AjSuP_C: ratio of Adj phrases count to Subordinate Clauses count
    - ra_AjPrP_C: ratio of Adj phrases count to Prep phrases count
    - ra_AjAvP_C: ratio of Adj phrases count to Adv phrases count

    - to_AvPhr_C: total count of Adverb phrases
    - as_AvPhr_C: average count of Adverb phrases per sentence
    - at_AvPhr_C: average count of Adverb phrases per token
    - ra_AvNoP_C: ratio of Adv phrases count to Noun phrases count
    - ra_AvVeP_C: ratio of Adv phrases count to Verb phrases count
    - ra_AvSuP_C: ratio of Adv phrases count to Subordinate Clauses count
    - ra_AvPrP_C: ratio of Adv phrases count to Prep phrases count
    - ra_AvAjP_C: ratio of Adv phrases count to Adj phrases count
    """
    def PhrF_(self):
        result = Synta_PhrF.retrieve(SuPar, self.sent_token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result
    


    """
    Extract Tree Structure Features -> 6

    output (type -> dictionary): 
    - to_TreeH_C: total Tree height of all sentences
    - as_TreeH_C: average Tree height per sentence
    - at_TreeH_C: average Tree height per token (word)
    - to_FTree_C: total length of flattened Trees
    - as_FTree_C: average length of flattened Trees per sentence
    - at_FTree_C: average length of flattened Trees per token (word)
    """
    def TrSF_(self):
        result = Synta_TrSF.retrieve(SuPar, self.sent_token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result



    """
    Part-of-Speech Features -> 55

    output (type -> dictionary): 
    - to_NoTag_C: total count of Noun POS tags
    - as_NoTag_C: average count of Noun POS tags per sentence
    - at_NoTag_C: average count of Noun POS tags per token
    - ra_NoAjT_C: ratio of Noun POS count to Adjective POS count
    - ra_NoVeT_C: ratio of Noun POS count to Verb POS count
    - ra_NoAvT_C: ratio of Noun POS count to Adverb POS count
    - ra_NoSuT_C: ratio of Noun POS count to Subordinating Conjunction count
    - ra_NoCoT_C: ratio of Noun POS count to Coordinating Conjunction count

    - to_VeTag_C: total count of Verb POS tags
    - as_VeTag_C: average count of Verb POS tags per sentence
    - at_VeTag_C: average count of Verb POS tags per token
    - ra_VeAjT_C: ratio of Verb POS count to Adjective POS count
    - ra_VeNoT_C: ratio of Verb POS count to Noun POS count
    - ra_VeAvT_C: ratio of Verb POS count to Adverb POS count
    - ra_VeSuT_C: ratio of Verb POS count to Subordinating Conjunction count
    - ra_VeCoT_C: ratio of Verb POS count to Coordinating Conjunction count

    - to_AjTag_C: total count of Adjective POS tags
    - as_AjTag_C: average count of Adjective POS tags per sentence
    - at_AjTag_C: average count of Adjective POS tags per token
    - ra_AjNoT_C: ratio of Adjective POS count to Noun POS count
    - ra_AjVeT_C: ratio of Adjective POS count to Verb POS count
    - ra_AjAvT_C: ratio of Adjective POS count to Adverb POS count
    - ra_AjSuT_C: ratio of Adjective POS count to Subordinating Conjunction count
    - ra_AjCoT_C: ratio of Adjective POS count to Coordinating Conjunction count

    - to_AvTag_C: total count of Adverb POS tags
    - as_AvTag_C: average count of Adverb POS tags per sentence
    - at_AvTag_C: average count of Adverb POS tags per token
    - ra_AvAjT_C: ratio of Adverb POS count to Adjective POS count
    - ra_AvNoT_C: ratio of Adverb POS count to Noun POS count
    - ra_AvVeT_C: ratio of Adverb POS count to Verb POS count
    - ra_AvSuT_C: ratio of Adverb POS count to Subordinating Conjunction count
    - ra_AvCoT_C: ratio of Adverb POS count to Coordinating Conjunction count

    - to_SuTag_C: total count of Subordinating Conjunction POS tags
    - as_SuTag_C: average count of Subordinating Conjunction POS tags per sentence
    - at_SuTag_C: average count of Subordinating Conjunction POS tags per token
    - ra_SuAjT_C: ratio of Subordinating Conjunction POS count to Adjective POS count
    - ra_SuNoT_C: ratio of Subordinating Conjunction POS count to Noun POS count
    - ra_SuVeT_C: ratio of Subordinating Conjunction POS count to Verb POS count
    - ra_SuAvT_C: ratio of Subordinating Conjunction POS count to Adverb POS count
    - ra_SuCoT_C: ratio of Subordinating Conjunction POS count to Coordinating Conjunction count

    - to_CoTag_C: total count of Coordinating Conjunction POS tags
    - as_CoTag_C: average count of Coordinating Conjunction POS tags per sentence
    - at_CoTag_C: average count of Coordinating Conjunction POS tags per token
    - ra_CoAjT_C: ratio of Coordinating Conjunction POS count to Adjective POS count
    - ra_CoNoT_C: ratio of Coordinating Conjunction POS count to Noun POS count
    - ra_CoVeT_C: ratio of Coordinating Conjunction POS count to Verb POS count
    - ra_CoAvT_C: ratio of Coordinating Conjunction POS count to Adverb POS count
    - ra_CoSuT_C: ratio of Coordinating Conjunction POS count to Subordinating Conjunction count

    - to_ContW_C: total count of Content words
    - as_ContW_C: average count of Content words per sentence
    - at_ContW_C: average count of Content words per token
    - to_FuncW_C: total count of Function words
    - as_FuncW_C: average count of Function words per sentence
    - at_FuncW_C: average count of Function words per token
    - ra_CoFuW_C: ratio of Content words to Function words
    """
    def POSF_(self):
        result = Synta_POSF.retrieve(self.NLP_doc, self.n_token, self.n_sent)
        result = nan_check(result)
        return result



    """
    Extract Type Token Ratio Features -> 5

    output (type -> dictionary): 
    - SimpTTR_S: unique tokens/total tokens (TTR)
    - CorrTTR_S: unique tokens/sqrt(2*total tokens) (Corrected TTR)
    - BiLoTTR_S: log(unique tokens)/log(total tokens) (Bi-Logarithmic TTR)
    - UberTTR_S: (log(unique tokens))^2/log(total tokens/unique tokens) (Uber Index)
    - MTLDTTR_S: Measure of Textual Lexical Diversity (default TTR = 0.72)
    """
    def TTRF_(self):
        result = LxSem_TTRF.retrieve(self.n_token, self.token_list)
        result = nan_check(result)
        return result
    


    """
    Extract Variation Ratio Features -> 12

    output (type -> dictionary): 
    - SimpNoV_S: unique Nouns/total Nouns (Noun Variation-1)
    - SquaNoV_S: (unique Nouns**2)/total Nouns (Squared Noun Variation-1)
    - CorrNoV_S: unique Nouns/sqrt(2*total Nouns) (Corrected Noun Variation-1)

    - SimpVeV_S: unique Verbs/total Verbs (Verb Variation-1)
    - SquaVeV_S: (unique Verbs**2)/total Verbs (Squared Verb Variation-1)
    - CorrVeV_S: unique Verbs/sqrt(2*total Verbs) (Corrected Verb Variation-1)

    - SimpAjV_S: unique Adjectives/total Adjectives (Adjective Variation-1)
    - SquaAjV_S: (unique Adjectives**2)/total Adjectives (Squared Adjective Variation-1)
    - CorrAjV_S: unique Adjectives/sqrt(2*total Adjectives) (Corrected Adjective Variation-1)

    - SimpAvV_S: unique Adverbs/total Adverbs (AdVerb Variation-1)
    - SquaAvV_S: (unique Adverbs**2)/total Adverbs (Squared AdVerb Variation-1)
    - CorrAvV_S: unique Adverbs/sqrt(2*total Adverbs) (Corrected AdVerb Variation-1)
    """
    def VarF_(self):
        result = LxSem_VarF.retrieve(self.NLP_doc)
        result = nan_check(result)
        return result



    """
    Extract Psycholinguistic Features -> 15

    - to_AAKuW_C: total AoA (Age of Acquisition) of words
    - as_AAKuW_C: average AoA of words per sentence
    - at_AAKuW_C: average AoA of words per token
    - to_AAKuL_C: total lemmas AoA of lemmas
    - as_AAKuL_C: average lemmas AoA of lemmas per sentence
    - at_AAKuL_C: average lemmas AoA of lemmas per token
    - to_AABiL_C: total lemmas AoA of lemmas, Bird norm
    - as_AABiL_C: average lemmas AoA of lemmas, Bird norm per sentence
    - at_AABiL_C: average lemmas AoA of lemmas, Bird norm per token
    - to_AABrL_C: total lemmas AoA of lemmas, Bristol norm
    - as_AABrL_C: average lemmas AoA of lemmas, Bristol norm per sentence
    - at_AABrL_C: average lemmas AoA of lemmas, Bristol norm per token
    - to_AACoL_C: total AoA of lemmas, Cortese and Khanna norm
    - as_AACoL_C: average AoA of lemmas, Cortese and Khanna norm per sentence
    - at_AACoL_C: average AoA of lemmas, Cortese and Khanna norm per token
    """
    def PsyF_(self):
        result = LxSem_PsyF.retrieve(self.token_list, self.n_token, self.n_sent, dir_path)
        result = nan_check(result)
        return result



    """
    Extract Word Frequency Features -> 18

    - to_SbFrQ_C: total SubtlexUS FREQcount value
    - as_SbFrQ_C: average SubtlexUS FREQcount value per sentence
    - at_SbFrQ_C: average SubtlexUS FREQcount value per token

    - to_SbCDC_C: total SubtlexUS CDcount value
    - as_SbCDC_C: average SubtlexUS CDcount value per sentence
    - at_SbCDC_C: average SubtlexUS CDcount value per token

    - to_SbFrL_C: total SubtlexUS FREQlow value
    - as_SbFrL_C: average SubtlexUS FREQlow value per sentence
    - at_SbFrL_C: average SubtlexUS FREQlow value per token

    - to_SbCDL_C: total SubtlexUS CDlow value
    - as_SbCDL_C: average SubtlexUS CDlow value per sentence
    - at_SbCDL_C: average SubtlexUS CDlow value per token

    - to_SbSBW_C: total SubtlexUS SUBTLWF value
    - as_SbSBW_C: average SubtlexUS SUBTLWF value per sentence
    - at_SbSBW_C: average SubtlexUS SUBTLWF value per token

    - to_SbL1W_C: total SubtlexUS Lg10WF value
    - as_SbL1W_C: average SubtlexUS Lg10WF value per sentence
    - at_SbL1W_C: average SubtlexUS Lg10WF value per token

    - to_SbSBC_C: total SubtlexUS SUBTLCD value
    - as_SbSBC_C: average SubtlexUS SUBTLCD value per sentence
    - at_SbSBC_C: average SubtlexUS SUBTLCD value per token

    - to_SbL1C_C: total SubtlexUS Lg10CD value
    - as_SbL1C_C: average SubtlexUS Lg10CD value per sentence
    - at_SbL1C_C: average SubtlexUS Lg10CD value per token
    """
    def WorF_(self):
        result = LxSem_WorF.retrieve(self.token_list, self.n_token, self.n_sent, dir_path)
        result = nan_check(result)
        return result



    """
    Shallow Features -> 6

    output (type -> dictionary): 
    - TokSenM_S: total count of tokens x total count of sentence
    - as_Token_C: average count of tokens per sentence
    - as_Sylla_C: average count of syllables per sentence
    - at_Sylla_C: average count of syllables per token
    - as_Chara_C: average count of characters per sentence
    - at_Chara_C: average count of characters per token
    """
    def ShaF_(self):
        result = ShaTr_ShaF.retrieve(self.origin_doc, self.token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result


    
    """
    Traditional Formulas Features -> 6

    output (type -> dictionary): 
    - SmogInd_S: Smog Index
    - ColeLia_S: Coleman Liau Readability Score
    - Gunning_S: Gunning Fog
    - AutoRea_S: Automated Readability Index
    - FleschG_S: Flesch Kincaid Grade
    - LinseaW_S: Linsear Write
    """
    def TraF_(self):
        result = ShaTr_TraF.retrieve(self.origin_doc, self.sent_token_list, self.n_sent, self.n_token)
        result = nan_check(result)
        return result