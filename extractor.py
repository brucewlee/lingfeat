# -*- coding: UTF-8 -*-
"""
Program Name: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Author: Bruce W. Lee (이웅성)
Affiliation: Researcher - LXPER AI, Seoul, South Korea
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

# performance-central dependencies
import spacy 
import supar
from supar import Parser
import gensim # for World Knowledge Features

# advanced semantic features
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

# lexico-semantic features
import lingfeat._LexicoSemantic.TTRF as LxSem_TTRF
import lingfeat._LexicoSemantic.VarF as LxSem_VarF
import lingfeat._LexicoSemantic.PsyF as LxSem_PsyF
import lingfeat._LexicoSemantic.WoLF as LxSem_WoLF

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


class start:
    
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
    - WRich05_S: semantic Richness from 50 topics extracted from wikipedia
    - WClar05_S: semantic Clarity calculated from 50 topics extracted from wikipedia
    - WNois05_S: semantic Noise calculated from 50 topics extracted from wikipedia
    - WTopc05_S: number of topics identified (in input data) out of 50 topics extracted from wikipedia
    - WRich10_S: semantic Richness from 100 topics extracted from wikipedia
    - WClar10_S: semantic Clarity calculated from 100 topics extracted from wikipedia
    - WNois10_S: semantic Noise calculated from 100 topics extracted from wikipedia
    - WTopc10_S: number of topics identified (in input data) out of 100 topics extracted from wikipedia
    - WRich15_S: semantic Richness from 150 topics extracted from wikipedia
    - WClar15_S: semantic Clarity calculated from 150 topics extracted from wikipedia
    - WNois15_S: semantic Noise calculated from 150 topics extracted from wikipedia
    - WTopc15_S: number of topics identified (in input data) out of 150 topics extracted from wikipedia
    - WRich20_S: semantic Richness from 200 topics extracted from wikipedia
    - WClar20_S: semantic Clarity calculated from 200 topics extracted from wikipedia
    - WNois20_S: semantic Noise calculated from 200 topics extracted from wikipedia
    - WTopc20_S: number of topics identified (in input data) out of 200 topics extracted from wikipedia
    """
    def WoKF_(self):
        result = AdSem_WoKF.retrieve(self.token_list, dir_path)
        result = nan_check(result)
        return result



    """
    Extract Advanced Semantic Features WeeBit -> 12

    output (type -> dictionary): 
    - BRich05_S: semantic Richness from 50 topics extracted from weebit
    - BClar05_S: semantic Clarity calculated from 50 topics extracted from weebit
    - BNois05_S: semantic Noise calculated from 50 topics extracted from weebit
    - BTopc05_S: number of topics identified (in input data) out of 50 topics extracted from weebit
    - BRich10_S: semantic Richness from 100 topics extracted from weebit
    - BClar10_S: semantic Clarity calculated from 100 topics extracted from weebit
    - BNois10_S: semantic Noise calculated from 100 topics extracted from weebit
    - BTopc10_S: number of topics identified (in input data) out of 100 topics extracted from weebit
    - BRich15_S: semantic Richness from 150 topics extracted from weebit
    - BClar15_S: semantic Clarity calculated from 150 topics extracted from weebit
    - BNois15_S: semantic Noise calculated from 150 topics extracted from weebit
    - BTopc15_S: number of topics identified (in input data) out of 150 topics extracted from weebit
    - BRich20_S: semantic Richness from 200 topics extracted from weebit
    - BClar20_S: semantic Clarity calculated from 200 topics extracted from weebit
    - BNois20_S: semantic Noise calculated from 200 topics extracted from weebit
    - BTopc20_S: number of topics identified (in input data) out of 200 topics extracted from weebit
    """
    def WBKF_(self):
        result = AdSem_WBKF.retrieve(self.token_list, dir_path)
        result = nan_check(result)
        return result



    """
    Extract Advanced Semantic Features OneStop -> 12

    output (type -> dictionary): 
    - ORich05_S: semantic Richness from 50 topics extracted from OneStop
    - OClar05_S: semantic Clarity calculated from 50 topics extracted from OneStop
    - ONois05_S: semantic Noise calculated from 50 topics extracted from OneStop
    - OTopc05_S: number of topics identified (in input data) out of 50 topics extracted from OneStop
    - ORich10_S: semantic Richness from 100 topics extracted from OneStop
    - OClar10_S: semantic Clarity calculated from 100 topics extracted from OneStop
    - ONois10_S: semantic Noise calculated from 100 topics extracted from OneStop
    - OTopc10_S: number of topics identified (in input data) out of 100 topics extracted from OneStop
    - ORich15_S: semantic Richness from 150 topics extracted from OneStop
    - OClar15_S: semantic Clarity calculated from 150 topics extracted from OneStop
    - ONois15_S: semantic Noise calculated from 150 topics extracted from OneStop
    - OTopc15_S: number of topics identified (in input data) out of 150 topics extracted from OneStop
    - ORich20_S: semantic Richness from 200 topics extracted from OneStop
    - OClar20_S: semantic Clarity calculated from 200 topics extracted from OneStop
    - ONois20_S: semantic Noise calculated from 200 topics extracted from OneStop
    - OTopc20_S: number of topics identified (in input data) out of 200 topics extracted from OneStop
    """
    def OSKF_(self):
        result = AdSem_OSKF.retrieve(self.token_list, dir_path)
        result = nan_check(result)
        return result



    """
    Extract Entity Density Features -> 6

    output (type -> dictionary): 
    - to_EntiM_C: total number of entities mentions counts
    - as_EntiM_C: average number of entities mentions counts per sentence
    - at_EntiM_C: average number of entities mentions counts per token (word)
    - to_UEnti_C: total number of unique entities
    - as_UEnti_C: average number of unique entities per sentence
    - at_UEnti_C: average number of unique entities per token (word)
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

    - LoCohPA_S: local coherence for PA score
    - LoCohPW_S: local coherence for PW score
    - LoCohPU_S: local coherence for PU score
    - LoCoDPA_S: local coherence distance for PA score    
    - LoCoDPW_S: local coherence distance for PW score    
    - LoCoDPU_S: local coherence distance for PU score    
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
    - to_NoPhr_C: total number of noun phrases
    - as_NoPhr_C: average number of noun phrases per sentence
    - at_NoPhr_C: average number of noun phrases per token
    - ra_NoVeP_C: ratio of noun phrases count to verb phrases count
    - ra_NoSuP_C: ratio of noun phrases count to subordinate clauses count
    - ra_NoPrP_C: ratio of noun phrases count to prep phrases count
    - ra_NoAjP_C: ratio of noun phrases count to adj phrases count
    - ra_NoAvP_C: ratio of noun phrases count to adv phrases count

    - to_VePhr_C: total number of verb phrases
    - as_VePhr_C: average number of verb phrases per sentence
    - at_VePhr_C: average number of verb phrases per token
    - ra_VeNoP_C: ratio of verb phrases count to noun phrases count
    - ra_VeSuP_C: ratio of verb phrases count to subordinate clauses count
    - ra_VePrP_C: ratio of verb phrases count to prep phrases count
    - ra_VeAjP_C: ratio of verb phrases count to adj phrases count
    - ra_VeAvP_C: ratio of verb phrases count to adv phrases count

    - to_SuPhr_C: total number of subordinate clauses
    - as_SuPhr_C: average number of subordinate clauses per sentence
    - at_SuPhr_C: average number of subordinate clauses per token
    - ra_SuNoP_C: ratio of subordinate clauses count to noun phrases count
    - ra_SuVeP_C: ratio of subordinate clauses count to verb phrases count
    - ra_SuPrP_C: ratio of subordinate clauses count to prep phrases count
    - ra_SuAjP_C: ratio of subordinate clauses count to adj phrases count
    - ra_SuAvP_C: ratio of subordinate clauses count to adv phrases count

    - to_PrPhr_C: total number of prepositional phrases
    - as_PrPhr_C: average number of prepositional phrases per sentence
    - at_PrPhr_C: average number of prepositional phrases per token
    - ra_PrNoP_C: ratio of prep phrases count to noun phrases count
    - ra_PrVeP_C: ratio of prep phrases count to verb phrases count
    - ra_PrSuP_C: ratio of prep phrases count to subordinate clauses count
    - ra_PrAjP_C: ratio of prep phrases count to adj phrases count
    - ra_PrAvP_C: ratio of prep phrases count to adv phrases count

    - to_AjPhr_C: total number of adjective phrases
    - as_AjPhr_C: average number of adjective phrases per sentence
    - at_AjPhr_C: average number of adjective phrases per token
    - ra_AjNoP_C: ratio of adj phrases count to noun phrases count
    - ra_AjVeP_C: ratio of adj phrases count to verb phrases count
    - ra_AjSuP_C: ratio of adj phrases count to subordinate clauses count
    - ra_AjPrP_C: ratio of adj phrases count to prep phrases count
    - ra_AjAvP_C: ratio of adj phrases count to adv phrases count
    
    - to_AvPhr_C: total number of adverb phrases
    - as_AvPhr_C: average number of adverb phrases per sentence
    - at_AvPhr_C: average number of adverb phrases per token
    - ra_AvNoP_C: ratio of adv phrases count to noun phrases count
    - ra_AvVeP_C: ratio of adv phrases count to verb phrases count
    - ra_AvSuP_C: ratio of adv phrases count to subordinate clauses count
    - ra_AvPrP_C: ratio of adv phrases count to prep phrases count
    - ra_AvAjP_C: ratio of adv phrases count to adj phrases count
    """
    def PhrF_(self):
        result = Synta_PhrF.retrieve(SuPar, self.sent_token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result
    


    """
    Extract Tree Structure Features -> 6

    output (type -> dictionary): 
    - to_TreeH_C: total tree height of all sentences
    - as_TreeH_C: average tree height per sentence
    - at_TreeH_C: average tree height per token (word)
    - to_FTree_C: total length of flattened trees
    - as_FTree_C: average length of flattened trees per sentence
    - at_FTree_C: average length of flattened trees per token (word)
    """
    def TrSF_(self):
        result = Synta_TrSF.retrieve(SuPar, self.sent_token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result



    """
    Part-of-Speech Features -> 55

    output (type -> dictionary): 
    - to_NoTag_C: total number of noun POS tags
    - as_NoTag_C: average number of noun POS tags per sentence
    - at_NoTag_C: average number of noun POS tags per token
    - ra_NoAjT_C: ratio of noun POS count to adjective POS count
    - ra_NoVeT_C: ratio of noun POS count to verb POS count
    - ra_NoAvT_C: ratio of noun POS count to adverb POS count
    - ra_NoSuT_C: ratio of noun POS count to subordinating conjunction count
    - ra_NoCoT_C: ratio of noun POS count to coordinating conjunction count

    - to_VeTag_C: total number of verb POS tags
    - as_VeTag_C: average number of verb POS tags per sentence
    - at_VeTag_C: average number of verb POS tags per token
    - ra_VeAjT_C: ratio of verb POS count to adjective POS count
    - ra_VeNoT_C: ratio of verb POS count to noun POS count
    - ra_VeAvT_C: ratio of verb POS count to adverb POS count
    - ra_VeSuT_C: ratio of verb POS count to subordinating conjunction count
    - ra_VeCoT_C: ratio of verb POS count to coordinating conjunction count
    
    - to_AjTag_C: total number of adjective POS tags
    - as_AjTag_C: average number of adjective POS tags per sentence
    - at_AjTag_C: average number of adjective POS tags per token
    - ra_AjNoT_C: ratio of adjective POS count to noun POS count
    - ra_AjVeT_C: ratio of adjective POS count to verb POS count
    - ra_AjAvT_C: ratio of adjective POS count to adverb POS count
    - ra_AjSuT_C: ratio of adjective POS count to subordinating conjunction count
    - ra_AjCoT_C: ratio of adjective POS count to coordinating conjunction count

    - to_AvTag_C: total number of adverb POS tags
    - as_AvTag_C: average number of adverb POS tags per sentence
    - at_AvTag_C: average number of adverb POS tags per token
    - ra_AvAjT_C: ratio of adverb POS count to adjective POS count
    - ra_AvNoT_C: ratio of adverb POS count to noun POS count
    - ra_AvVeT_C: ratio of adverb POS count to verb POS count
    - ra_AvSuT_C: ratio of adverb POS count to subordinating conjunction count
    - ra_AvCoT_C: ratio of adverb POS count to coordinating conjunction count

    - to_SuTag_C: total number of subordinating conjunction POS tags
    - as_SuTag_C: average number of subordinating conjunction POS tags per sentence
    - at_SuTag_C: average number of subordinating conjunction POS tags per token
    - ra_SuAjT_C: ratio of subordinating conjunction POS count to adjective POS count
    - ra_SuNoT_C: ratio of subordinating conjunction POS count to noun POS count
    - ra_SuVeT_C: ratio of subordinating conjunction POS count to verb POS count
    - ra_SuAvT_C: ratio of subordinating conjunction POS count to adverb POS count
    - ra_SuCoT_C: ratio of subordinating conjunction POS count to coordinating conjunction count

    - to_CoTag_C: total number of coordinating conjunction POS tags
    - as_CoTag_C: average number of coordinating conjunction POS tags per sentence
    - at_CoTag_C: average number of coordinating conjunction POS tags per token
    - ra_CoAjT_C: ratio of coordinating conjunction POS count to adjective POS count
    - ra_CoNoT_C: ratio of coordinating conjunction POS count to noun POS count
    - ra_CoVeT_C: ratio of coordinating conjunction POS count to verb POS count
    - ra_CoAvT_C: ratio of coordinating conjunction POS count to adverb POS count
    - ra_CoSuT_C: ratio of coordinating conjunction POS count to subordinating conjunction count

    - to_ContW_C: total number of content words
    - as_ContW_C: average number of content words per sentence
    - at_ContW_C: average number of content words per token
    - to_FuncW_C: total number of function words
    - as_FuncW_C: average number of function words per sentence
    - at_FuncW_C: average number of function words per token
    - ra_CoFuW_C: ratio of content words to function words
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
    - SimpNoV_S: unique nouns/total nouns (Noun Variation-1)
    - SquaNoV_S: (unique nouns**2)/total nouns (Squared Noun Variation-1)
    - CorrNoV_S: unique nouns/sqrt(2*total nouns) (Corrected Noun Variation-1)

    - SimpVeV_S: unique verbs/total verbs (Verb Variation-1)
    - SquaVeV_S: (unique verbs**2)/total verbs (Squared Verb Variation-1)
    - CorrVeV_S: unique verbs/sqrt(2*total verbs) (Corrected Verb Variation-1)

    - SimpAjV_S: unique adjectives/total adjectives (Adjective Variation-1)
    - SquaAjV_S: (unique adjectives**2)/total adjectives (Squared Adjective Variation-1)
    - CorrAjV_S: unique adjectives/sqrt(2*total adjectives) (Corrected Adjective Variation-1)

    - SimpAvV_S: unique adverbs/total adverbs (Adverb Variation-1)
    - SquaAvV_S: (unique adverbs**2)/total adverbs (Squared Adverb Variation-1)
    - CorrAvV_S: unique adverbs/sqrt(2*total adverbs) (Corrected Adverb Variation-1)
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
    - as_AACoL_C: average =AoA of lemmas, Cortese and Khanna norm per sentence
    - at_AACoL_C: average =AoA of lemmas, Cortese and Khanna norm per token
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
    def WoLF_(self):
        result = LxSem_WoLF.retrieve(self.token_list, self.n_token, self.n_sent, dir_path)
        result = nan_check(result)
        return result



    """
    Shallow Features -> 5

    output (type -> dictionary): 
    - as_Token_C: average number of tokens per sentence
    - as_Sylla_C: average number of syllables per sentence
    - at_Sylla_C: average number of syllables per token
    - as_Chara_C: average number of characters per sentence
    - at_Chara_C: average number of characters per token
    """
    def ShaF_(self):
        result = ShaTr_ShaF.retrieve(self.origin_doc, self.token_list, self.n_token, self.n_sent)
        result = nan_check(result)
        return result


    
    """
    Traditional Formulas Features -> 8

    output (type -> dictionary): 
    - FleschR_S: Flesch Reading Ease
    - SmogInd_S: Smog Index
    - ColeLia_S: Coleman Liau Readability Score
    - DaleCha_S: Dale Chall Readability Score
    - Gunning_S: Gunning Fog
    - AutoRea_S: Automated Readability Index
    - FleschG_S: Flesch Kincaid Grade
    - LinseaW_S: Linsear Write
    """
    def TraF_(self):
        result = ShaTr_TraF.retrieve(self.origin_doc)
        result = nan_check(result)
        return result
    


def nan_check(result):
    for key in result:
        if math.isnan(float(result[key])):
            result[key] = 0
    return result