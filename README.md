[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]
# LingFeat - Comprehensive Linguistic Features Extraction for Readability Assessment
## Overview

LingFeat is a Python research package for dealing with various handcrafted linguistic features. 

LingFeat currently supports 218 linguistic features, divided into five linguistic branches:
1. Advanced Semantic
2. Discourse
3. Syntactic
4. Lexico Semantic
5. Shallow Traditional

Most of these features are inspired from readability assessment (RA) research, a branch of NLP.

## Installation

Option 1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install LingFeat. (not supported now)
```bash
pip install lingfeat
```

Option 2. Install from the repo.
```bash
git clone https://github.com/brucewlee/lingfeat.git
```
   
## Usage

```python
# import
from lingfeat import extractor

# pass in text (string)
LingFeat = extractor.start(text)

# preprocess
LingFeat.preprocess()

# extract features - each method returns a dictionary of corresponding features
WoKF = LingFeat.WoKF_()
WBKF = LingFeat.WBKF_()
OSKF = LingFeat.OSKF_()
EnDF = LingFeat.EnDF_()
EnGF = LingFeat.EnGF_()
PhrF = LingFeat.PhrF_()
TrSF = LingFeat.TrSF_()
POSF = LingFeat.POSF_()
TTRF = LingFeat.TTRF_()
VarF = LingFeat.VarF_()
PsyF = LingFeat.PsyF_() 
WoLF = LingFeat.WoLF_()
ShaF = LingFeat.ShaF_()
TraF = LingFeat.TraF_()
```

## Available Features, Code, Definition
| Index | Linguistic Branch   | Subgroup Code | Subgroup Definition                  | Feature Code | Feature Definition                                                             |
|-------|---------------------|---------------|--------------------------------------|--------------|--------------------------------------------------------------------------------|
| 1     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WRich05_S    | Semantic Richness, 50 topics extracted from Wikipedia                          |
| 2     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WClar05_S    | Semantic Clarity, 50 topics extracted from Wikipedia                           |
| 3     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WNois05_S    | Semantic Noise, 50 topics extracted from Wikipedia                             |
| 4     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WTopc05_S    | Number of topics, 50 topics extracted from Wikipedia                           |
| 5     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WRich10_S    | Semantic Richness, 100 topics extracted from Wikipedia                         |
| 6     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WClar10_S    | Semantic Clarity, 100 topics extracted from Wikipedia                          |
| 7     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WNois10_S    | Semantic Noise, 100 topics extracted from Wikipedia                            |
| 8     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WTopc10_S    | Number of topics, 100 topics extracted from Wikipedia                          |
| 9     | Advanced Semantics  | WoKF_         | World Knowledge Features             | WRich15_S    | Semantic Richness, 150 topics extracted from Wikipedia                         |
| 10    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WClar15_S    | Semantic Clarity, 150 topics extracted from Wikipedia                          |
| 11    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WNois15_S    | Semantic Noise, 150 topics extracted from Wikipedia                            |
| 12    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WTopc15_S    | Number of topics, 150 topics extracted from Wikipedia                          |
| 13    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WRich20_S    | Semantic Richness, 200 topics extracted from Wikipedia                         |
| 14    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WClar20_S    | Semantic Clarity, 200 topics extracted from Wikipedia                          |
| 15    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WNois20_S    | Semantic Noise, 200 topics extracted from Wikipedia                            |
| 16    | Advanced Semantics  | WoKF_         | World Knowledge Features             | WTopc20_S    | Number of topics, 200 topics extracted from Wikipedia                          |
| 17    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BRich05_S    | Semantic Richness from 50 topics extracted from WeeBit Corpus                  |
| 18    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BClar05_S    | Semantic Clarity, 50 topics extracted from WeeBit Corpus                       |
| 19    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BNois05_S    | Semantic Noise, 50 topics extracted from WeeBit Corpus                         |
| 20    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BTopc05_S    | Number of topics, 50 topics extracted from WeeBit Corpus                       |
| 21    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BRich10_S    | Semantic Richness from 100 topics extracted from WeeBit Corpus                 |
| 22    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BClar10_S    | Semantic Clarity, 100 topics extracted from WeeBit Corpus                      |
| 23    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BNois10_S    | Semantic Noise, 100 topics extracted from WeeBit Corpus                        |
| 24    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BTopc10_S    | Number of topics, 100 topics extracted from WeeBit Corpus                      |
| 25    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BRich15_S    | Semantic Richness from 150 topics extracted from WeeBit Corpus                 |
| 26    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BClar15_S    | Semantic Clarity, 150 topics extracted from WeeBit Corpus                      |
| 27    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BNois15_S    | Semantic Noise, 150 topics extracted from WeeBit Corpus                        |
| 28    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BTopc15_S    | Number of topics, 150 topics extracted from WeeBit Corpus                      |
| 29    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BRich20_S    | Semantic Richness from 200 topics extracted from WeeBit Corpus                 |
| 30    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BClar20_S    | Semantic Clarity, 200 topics extracted from WeeBit Corpus                      |
| 31    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BNois20_S    | Semantic Noise, 200 topics extracted from WeeBit Corpus                        |
| 32    | Advanced Semantics  | WBKF_         | WeeBit Corpus Knowledge Features     | BTopc20_S    | Number of topics, 200 topics extracted from WeeBit Corpus                      |
| 33    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ORich05_S    | Semantic Richness from 50 topics extracted from OneStopEng Corpus              |
| 34    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OClar05_S    | Semantic Clarity, 50 topics extracted from OneStopEng Corpus                   |
| 35    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ONois05_S    | Semantic Noise, 50 topics extracted from OneStopEng Corpus                     |
| 36    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OTopc05_S    | Number of topics, 50 topics extracted from OneStopEng Corpus                   |
| 37    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ORich10_S    | Semantic Richness from 100 topics extracted from OneStopEng Corpus             |
| 38    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OClar10_S    | Semantic Clarity, 100 topics extracted from OneStopEng Corpus                  |
| 39    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ONois10_S    | Semantic Noise, 100 topics extracted from OneStopEng Corpus                    |
| 40    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OTopc10_S    | Number of topics, 100 topics extracted from OneStopEng Corpus                  |
| 41    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ORich15_S    | Semantic Richness from 150 topics extracted from OneStopEng Corpus             |
| 42    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OClar15_S    | Semantic Clarity, 150 topics extracted from OneStopEng Corpus                  |
| 43    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ONois15_S    | Semantic Noise, 150 topics extracted from OneStopEng Corpus                    |
| 44    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OTopc15_S    | Number of topics, 150 topics extracted from OneStopEng Corpus                  |
| 45    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ORich20_S    | Semantic Richness from 200 topics extracted from OneStopEng Corpus             |
| 46    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OClar20_S    | Semantic Clarity, 200 topics extracted from OneStopEng Corpus                  |
| 47    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | ONois20_S    | Semantic Noise, 200 topics extracted from OneStopEng Corpus                    |
| 48    | Advanced Semantics  | OSKF_         | OneStopEng Corpus Knowledge Features | OTopc20_S    | Number of topics, 200 topics extracted from OneStopEng Corpus                  |
| 49    | Discourse           | EnDF_         | Entity Density Features              | to_EntiM_C   | total number of Entities Mentions counts                                       |
| 50    | Discourse           | EnDF_         | Entity Density Features              | as_EntiM_C   | average number of Entities Mentions counts per sentence                        |
| 51    | Discourse           | EnDF_         | Entity Density Features              | at_EntiM_C   | average number of Entities Mentions counts per token (word)                    |
| 52    | Discourse           | EnDF_         | Entity Density Features              | to_UEnti_C   | total number of unique Entities                                                |
| 53    | Discourse           | EnDF_         | Entity Density Features              | as_UEnti_C   | average number of unique Entities per sentence                                 |
| 54    | Discourse           | EnDF_         | Entity Density Features              | at_UEnti_C   | average number of unique Entities per token (word)                             |
| 55    | Discourse           | EnGF_         | Entity Grid Features                 | ra_SSToT_C   | ratio of ss transitions to total                                               |
| 56    | Discourse           | EnGF_         | Entity Grid Features                 | ra_SOToT_C   | ratio of so transitions to total                                               |
| 57    | Discourse           | EnGF_         | Entity Grid Features                 | ra_SXToT_C   | ratio of sx transitions to total                                               |
| 58    | Discourse           | EnGF_         | Entity Grid Features                 | ra_SNToT_C   | ratio of sn transitions to total                                               |
| 59    | Discourse           | EnGF_         | Entity Grid Features                 | ra_OSToT_C   | ratio of os transitions to total                                               |
| 60    | Discourse           | EnGF_         | Entity Grid Features                 | ra_OOToT_C   | ratio of oo transitions to total                                               |
| 61    | Discourse           | EnGF_         | Entity Grid Features                 | ra_OXToT_C   | ratio of ox transitions to total                                               |
| 62    | Discourse           | EnGF_         | Entity Grid Features                 | ra_ONToT_C   | ratio of on transitions to total                                               |
| 63    | Discourse           | EnGF_         | Entity Grid Features                 | ra_XSToT_C   | ratio of xs transitions to total                                               |
| 64    | Discourse           | EnGF_         | Entity Grid Features                 | ra_XOToT_C   | ratio of xo transitions to total                                               |
| 65    | Discourse           | EnGF_         | Entity Grid Features                 | ra_XXToT_C   | ratio of xx transitions to total                                               |
| 66    | Discourse           | EnGF_         | Entity Grid Features                 | ra_XNToT_C   | ratio of xn transitions to total                                               |
| 67    | Discourse           | EnGF_         | Entity Grid Features                 | ra_NSToT_C   | ratio of ns transitions to total                                               |
| 68    | Discourse           | EnGF_         | Entity Grid Features                 | ra_NOToT_C   | ratio of no transitions to total                                               |
| 69    | Discourse           | EnGF_         | Entity Grid Features                 | ra_NXToT_C   | ratio of nx transitions to total                                               |
| 70    | Discourse           | EnGF_         | Entity Grid Features                 | ra_NNToT_C   | ratio of nn transitions to total                                               |
| 71    | Discourse           | EnGF_         | Entity Grid Features                 | LoCohPA_S    | Local Coherence for PA score                                                   |
| 72    | Discourse           | EnGF_         | Entity Grid Features                 | LoCohPW_S    | Local Coherence for PW score                                                   |
| 73    | Discourse           | EnGF_         | Entity Grid Features                 | LoCohPU_S    | Local Coherence for PU score                                                   |
| 74    | Discourse           | EnGF_         | Entity Grid Features                 | LoCoDPA_S    | Local Coherence distance for PA score                                          |
| 75    | Discourse           | EnGF_         | Entity Grid Features                 | LoCoDPW_S    | Local Coherence distance for PW score                                          |
| 76    | Discourse           | EnGF_         | Entity Grid Features                 | LoCoDPU_S    | Local Coherence distance for PU score                                          |
| 77    | Syntactic           | PhrF_         | Phrasal Features                     | to_NoPhr_C   | total count of Noun phrases                                                    |
| 78    | Syntactic           | PhrF_         | Phrasal Features                     | as_NoPhr_C   | average count of Noun phrases per sentence                                     |
| 79    | Syntactic           | PhrF_         | Phrasal Features                     | at_NoPhr_C   | average count of Noun phrases per token                                        |
| 80    | Syntactic           | PhrF_         | Phrasal Features                     | ra_NoVeP_C   | ratio of Noun phrases count to Verb phrases count                              |
| 81    | Syntactic           | PhrF_         | Phrasal Features                     | ra_NoSuP_C   | ratio of Noun phrases count to Subordinate Clauses count                       |
| 82    | Syntactic           | PhrF_         | Phrasal Features                     | ra_NoPrP_C   | ratio of Noun phrases count to Prep phrases count                              |
| 83    | Syntactic           | PhrF_         | Phrasal Features                     | ra_NoAjP_C   | ratio of Noun phrases count to Adj phrases count                               |
| 84    | Syntactic           | PhrF_         | Phrasal Features                     | ra_NoAvP_C   | ratio of Noun phrases count to Adv phrases count                               |
| 85    | Syntactic           | PhrF_         | Phrasal Features                     | to_VePhr_C   | total count of Verb phrases                                                    |
| 86    | Syntactic           | PhrF_         | Phrasal Features                     | as_VePhr_C   | average count of Verb phrases per sentence                                     |
| 87    | Syntactic           | PhrF_         | Phrasal Features                     | at_VePhr_C   | average count of Verb phrases per token                                        |
| 88    | Syntactic           | PhrF_         | Phrasal Features                     | ra_VeNoP_C   | ratio of Verb phrases count to Noun phrases count                              |
| 89    | Syntactic           | PhrF_         | Phrasal Features                     | ra_VeSuP_C   | ratio of Verb phrases count to Subordinate Clauses count                       |
| 90    | Syntactic           | PhrF_         | Phrasal Features                     | ra_VePrP_C   | ratio of Verb phrases count to Prep phrases count                              |
| 91    | Syntactic           | PhrF_         | Phrasal Features                     | ra_VeAjP_C   | ratio of Verb phrases count to Adj phrases count                               |
| 92    | Syntactic           | PhrF_         | Phrasal Features                     | ra_VeAvP_C   | ratio of Verb phrases count to Adv phrases count                               |
| 93    | Syntactic           | PhrF_         | Phrasal Features                     | to_SuPhr_C   | total count of Subordinate Clauses                                             |
| 94    | Syntactic           | PhrF_         | Phrasal Features                     | as_SuPhr_C   | average count of Subordinate Clauses per sentence                              |
| 95    | Syntactic           | PhrF_         | Phrasal Features                     | at_SuPhr_C   | average count of Subordinate Clauses per token                                 |
| 96    | Syntactic           | PhrF_         | Phrasal Features                     | ra_SuNoP_C   | ratio of Subordinate Clauses count to Noun phrases count                       |
| 97    | Syntactic           | PhrF_         | Phrasal Features                     | ra_SuVeP_C   | ratio of Subordinate Clauses count to Verb phrases count                       |
| 98    | Syntactic           | PhrF_         | Phrasal Features                     | ra_SuPrP_C   | ratio of Subordinate Clauses count to Prep phrases count                       |
| 99    | Syntactic           | PhrF_         | Phrasal Features                     | ra_SuAjP_C   | ratio of Subordinate Clauses count to Adj phrases count                        |
| 100   | Syntactic           | PhrF_         | Phrasal Features                     | ra_SuAvP_C   | ratio of Subordinate Clauses count to Adv phrases count                        |
| 101   | Syntactic           | PhrF_         | Phrasal Features                     | to_PrPhr_C   | total count of prepositional phrases                                           |
| 102   | Syntactic           | PhrF_         | Phrasal Features                     | as_PrPhr_C   | average count of prepositional phrases per sentence                            |
| 103   | Syntactic           | PhrF_         | Phrasal Features                     | at_PrPhr_C   | average count of prepositional phrases per token                               |
| 104   | Syntactic           | PhrF_         | Phrasal Features                     | ra_PrNoP_C   | ratio of Prep phrases count to Noun phrases count                              |
| 105   | Syntactic           | PhrF_         | Phrasal Features                     | ra_PrVeP_C   | ratio of Prep phrases count to Verb phrases count                              |
| 106   | Syntactic           | PhrF_         | Phrasal Features                     | ra_PrSuP_C   | ratio of Prep phrases count to Subordinate Clauses count                       |
| 107   | Syntactic           | PhrF_         | Phrasal Features                     | ra_PrAjP_C   | ratio of Prep phrases count to Adj phrases count                               |
| 108   | Syntactic           | PhrF_         | Phrasal Features                     | ra_PrAvP_C   | ratio of Prep phrases count to Adv phrases count                               |
| 109   | Syntactic           | PhrF_         | Phrasal Features                     | to_AjPhr_C   | total count of Adjective phrases                                               |
| 110   | Syntactic           | PhrF_         | Phrasal Features                     | as_AjPhr_C   | average count of Adjective phrases per sentence                                |
| 111   | Syntactic           | PhrF_         | Phrasal Features                     | at_AjPhr_C   | average count of Adjective phrases per token                                   |
| 112   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AjNoP_C   | ratio of Adj phrases count to Noun phrases count                               |
| 113   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AjVeP_C   | ratio of Adj phrases count to Verb phrases count                               |
| 114   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AjSuP_C   | ratio of Adj phrases count to Subordinate Clauses count                        |
| 115   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AjPrP_C   | ratio of Adj phrases count to Prep phrases count                               |
| 116   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AjAvP_C   | ratio of Adj phrases count to Adv phrases count                                |
| 117   | Syntactic           | PhrF_         | Phrasal Features                     | to_AvPhr_C   | total count of Adverb phrases                                                  |
| 118   | Syntactic           | PhrF_         | Phrasal Features                     | as_AvPhr_C   | average count of Adverb phrases per sentence                                   |
| 119   | Syntactic           | PhrF_         | Phrasal Features                     | at_AvPhr_C   | average count of Adverb phrases per token                                      |
| 120   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AvNoP_C   | ratio of Adv phrases count to Noun phrases count                               |
| 121   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AvVeP_C   | ratio of Adv phrases count to Verb phrases count                               |
| 122   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AvSuP_C   | ratio of Adv phrases count to Subordinate Clauses count                        |
| 123   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AvPrP_C   | ratio of Adv phrases count to Prep phrases count                               |
| 124   | Syntactic           | PhrF_         | Phrasal Features                     | ra_AvAjP_C   | ratio of Adv phrases count to Adj phrases count                                |
| 125   | Syntactic           | TrSF_         | Tree Structure Features              | to_TreeH_C   | total Tree height of all sentences                                             |
| 126   | Syntactic           | TrSF_         | Tree Structure Features              | as_TreeH_C   | average Tree height per sentence                                               |
| 127   | Syntactic           | TrSF_         | Tree Structure Features              | at_TreeH_C   | average Tree height per token (word)                                           |
| 128   | Syntactic           | TrSF_         | Tree Structure Features              | to_FTree_C   | total length of flattened Trees                                                |
| 129   | Syntactic           | TrSF_         | Tree Structure Features              | as_FTree_C   | average length of flattened Trees per sentence                                 |
| 130   | Syntactic           | TrSF_         | Tree Structure Features              | at_FTree_C   | average length of flattened Trees per token (word)                             |
| 131   | Syntactic           | POSF_         | Part-of-Speech Features              | to_NoTag_C   | total count of Noun POS tags                                                   |
| 132   | Syntactic           | POSF_         | Part-of-Speech Features              | as_NoTag_C   | average count of Noun POS tags per sentence                                    |
| 133   | Syntactic           | POSF_         | Part-of-Speech Features              | at_NoTag_C   | average count of Noun POS tags per token                                       |
| 134   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_NoAjT_C   | ratio of Noun POS count to Adjective POS count                                 |
| 135   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_NoVeT_C   | ratio of Noun POS count to Verb POS count                                      |
| 136   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_NoAvT_C   | ratio of Noun POS count to Adverb POS count                                    |
| 137   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_NoSuT_C   | ratio of Noun POS count to Subordinating Conjunction count                     |
| 138   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_NoCoT_C   | ratio of Noun POS count to Coordinating Conjunction count                      |
| 139   | Syntactic           | POSF_         | Part-of-Speech Features              | to_VeTag_C   | total count of Verb POS tags                                                   |
| 140   | Syntactic           | POSF_         | Part-of-Speech Features              | as_VeTag_C   | average count of Verb POS tags per sentence                                    |
| 141   | Syntactic           | POSF_         | Part-of-Speech Features              | at_VeTag_C   | average count of Verb POS tags per token                                       |
| 142   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_VeAjT_C   | ratio of Verb POS count to Adjective POS count                                 |
| 143   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_VeNoT_C   | ratio of Verb POS count to Noun POS count                                      |
| 144   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_VeAvT_C   | ratio of Verb POS count to Adverb POS count                                    |
| 145   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_VeSuT_C   | ratio of Verb POS count to Subordinating Conjunction count                     |
| 146   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_VeCoT_C   | ratio of Verb POS count to Coordinating Conjunction count                      |
| 147   | Syntactic           | POSF_         | Part-of-Speech Features              | to_AjTag_C   | total count of Adjective POS tags                                              |
| 148   | Syntactic           | POSF_         | Part-of-Speech Features              | as_AjTag_C   | average count of Adjective POS tags per sentence                               |
| 149   | Syntactic           | POSF_         | Part-of-Speech Features              | at_AjTag_C   | average count of Adjective POS tags per token                                  |
| 150   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AjNoT_C   | ratio of Adjective POS count to Noun POS count                                 |
| 151   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AjVeT_C   | ratio of Adjective POS count to Verb POS count                                 |
| 152   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AjAvT_C   | ratio of Adjective POS count to Adverb POS count                               |
| 153   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AjSuT_C   | ratio of Adjective POS count to Subordinating Conjunction count                |
| 154   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AjCoT_C   | ratio of Adjective POS count to Coordinating Conjunction count                 |
| 155   | Syntactic           | POSF_         | Part-of-Speech Features              | to_AvTag_C   | total count of Adverb POS tags                                                 |
| 156   | Syntactic           | POSF_         | Part-of-Speech Features              | as_AvTag_C   | average count of Adverb POS tags per sentence                                  |
| 157   | Syntactic           | POSF_         | Part-of-Speech Features              | at_AvTag_C   | average count of Adverb POS tags per token                                     |
| 158   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AvAjT_C   | ratio of Adverb POS count to Adjective POS count                               |
| 159   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AvNoT_C   | ratio of Adverb POS count to Noun POS count                                    |
| 160   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AvVeT_C   | ratio of Adverb POS count to Verb POS count                                    |
| 161   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AvSuT_C   | ratio of Adverb POS count to Subordinating Conjunction count                   |
| 162   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_AvCoT_C   | ratio of Adverb POS count to Coordinating Conjunction count                    |
| 163   | Syntactic           | POSF_         | Part-of-Speech Features              | to_SuTag_C   | total count of Subordinating Conjunction POS tags                              |
| 164   | Syntactic           | POSF_         | Part-of-Speech Features              | as_SuTag_C   | average count of Subordinating Conjunction POS tags per sentence               |
| 165   | Syntactic           | POSF_         | Part-of-Speech Features              | at_SuTag_C   | average count of Subordinating Conjunction POS tags per token                  |
| 166   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_SuAjT_C   | ratio of Subordinating Conjunction POS count to Adjective POS count            |
| 167   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_SuNoT_C   | ratio of Subordinating Conjunction POS count to Noun POS count                 |
| 168   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_SuVeT_C   | ratio of Subordinating Conjunction POS count to Verb POS count                 |
| 169   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_SuAvT_C   | ratio of Subordinating Conjunction POS count to Adverb POS count               |
| 170   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_SuCoT_C   | ratio of Subordinating Conjunction POS count to Coordinating Conjunction count |
| 171   | Syntactic           | POSF_         | Part-of-Speech Features              | to_CoTag_C   | total count of Coordinating Conjunction POS tags                               |
| 172   | Syntactic           | POSF_         | Part-of-Speech Features              | as_CoTag_C   | average count of Coordinating Conjunction POS tags per sentence                |
| 173   | Syntactic           | POSF_         | Part-of-Speech Features              | at_CoTag_C   | average count of Coordinating Conjunction POS tags per token                   |
| 174   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_CoAjT_C   | ratio of Coordinating Conjunction POS count to Adjective POS count             |
| 175   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_CoNoT_C   | ratio of Coordinating Conjunction POS count to Noun POS count                  |
| 176   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_CoVeT_C   | ratio of Coordinating Conjunction POS count to Verb POS count                  |
| 177   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_CoAvT_C   | ratio of Coordinating Conjunction POS count to Adverb POS count                |
| 178   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_CoSuT_C   | ratio of Coordinating Conjunction POS count to Subordinating Conjunction count |
| 179   | Syntactic           | POSF_         | Part-of-Speech Features              | to_ContW_C   | total count of Content words                                                   |
| 180   | Syntactic           | POSF_         | Part-of-Speech Features              | as_ContW_C   | average count of Content words per sentence                                    |
| 181   | Syntactic           | POSF_         | Part-of-Speech Features              | at_ContW_C   | average count of Content words per token                                       |
| 182   | Syntactic           | POSF_         | Part-of-Speech Features              | to_FuncW_C   | total count of Function words                                                  |
| 183   | Syntactic           | POSF_         | Part-of-Speech Features              | as_FuncW_C   | average count of Function words per sentence                                   |
| 184   | Syntactic           | POSF_         | Part-of-Speech Features              | at_FuncW_C   | average count of Function words per token                                      |
| 185   | Syntactic           | POSF_         | Part-of-Speech Features              | ra_CoFuW_C   | ratio of Content words to Function words                                       |
| 186   | Lexico-Semantic     | TTRF_         | Type Token Ratio Features            | SimpTTR_S    | unique tokens/total tokens (TTR)                                               |
| 187   | Lexico-Semantic     | TTRF_         | Type Token Ratio Features            | CorrTTR_S    | unique tokens/sqrt(2*total tokens) (Corrected TTR)                             |
| 188   | Lexico-Semantic     | TTRF_         | Type Token Ratio Features            | BiLoTTR_S    | log(unique tokens)/log(total tokens) (Bi-Logarithmic TTR)                      |
| 189   | Lexico-Semantic     | TTRF_         | Type Token Ratio Features            | UberTTR_S    | (log(unique tokens))^2/log(total tokens/unique tokens) (Uber Index)            |
| 190   | Lexico-Semantic     | TTRF_         | Type Token Ratio Features            | MTLDTTR_S    | Measure of Textual Lexical Diversity (default TTR = 0.72)                      |
| 191   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SimpNoV_S    | unique Nouns/total Nouns (Noun Variation-1)                                    |
| 192   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SquaNoV_S    | (unique Nouns**2)/total Nouns (Squared Noun Variation-1)                       |
| 193   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | CorrNoV_S    | unique Nouns/sqrt(2*total Nouns) (Corrected Noun Variation-1)                  |
| 194   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SimpVeV_S    | unique Verbs/total Verbs (Verb Variation-1)                                    |
| 195   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SquaVeV_S    | (unique Verbs**2)/total Verbs (Squared Verb Variation-1)                       |
| 196   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | CorrVeV_S    | unique Verbs/sqrt(2*total Verbs) (Corrected Verb Variation-1)                  |
| 197   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SimpAjV_S    | unique Adjectives/total Adjectives (Adjective Variation-1)                     |
| 198   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SquaAjV_S    | (unique Adjectives**2)/total Adjectives (Squared Adjective Variation-1)        |
| 199   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | CorrAjV_S    | unique Adjectives/sqrt(2*total Adjectives) (Corrected Adjective Variation-1)   |
| 200   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SimpAvV_S    | unique Adverbs/total Adverbs (AdVerb Variation-1)                              |
| 201   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | SquaAvV_S    | (unique Adverbs**2)/total Adverbs (Squared AdVerb Variation-1)                 |
| 202   | Lexico-Semantic     | VarF_         | Variation Ratio Features             | CorrAvV_S    | unique Adverbs/sqrt(2*total Adverbs) (Corrected AdVerb Variation-1)            |
| 203   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | to_AAKuW_C   | total AoA (Age of Acquisition) of words                                        |
| 204   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | as_AAKuW_C   | average AoA of words per sentence                                              |
| 205   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | at_AAKuW_C   | average AoA of words per token                                                 |
| 206   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | to_AAKuL_C   | total lemmas AoA of lemmas                                                     |
| 207   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | as_AAKuL_C   | average lemmas AoA of lemmas per sentence                                      |
| 208   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | at_AAKuL_C   | average lemmas AoA of lemmas per token                                         |
| 209   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | to_AABiL_C   | total lemmas AoA of lemmas, Bird norm                                          |
| 210   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | as_AABiL_C   | average lemmas AoA of lemmas, Bird norm per sentence                           |
| 211   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | at_AABiL_C   | average lemmas AoA of lemmas, Bird norm per token                              |
| 212   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | to_AABrL_C   | total lemmas AoA of lemmas, Bristol norm                                       |
| 213   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | as_AABrL_C   | average lemmas AoA of lemmas, Bristol norm per sentence                        |
| 214   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | at_AABrL_C   | average lemmas AoA of lemmas, Bristol norm per token                           |
| 215   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | to_AACoL_C   | total AoA of lemmas, Cortese and Khanna norm                                   |
| 216   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | as_AACoL_C   | average AoA of lemmas, Cortese and Khanna norm per sentence                    |
| 217   | Lexico-Semantic     | PsyF_         | Psycholinguistic Features            | at_AACoL_C   | average AoA of lemmas, Cortese and Khanna norm per token                       |
| 218   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbFrQ_C   | total SubtlexUS FREQcount value                                                |
| 219   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbFrQ_C   | average SubtlexUS FREQcount value per sentenc                                  |
| 220   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbFrQ_C   | average SubtlexUS FREQcount value per token                                    |
| 221   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbCDC_C   | total SubtlexUS CDcount value                                                  |
| 222   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbCDC_C   | average SubtlexUS CDcount value per sentence                                   |
| 223   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbCDC_C   | average SubtlexUS CDcount value per token                                      |
| 224   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbFrL_C   | total SubtlexUS FREQlow value                                                  |
| 225   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbFrL_C   | average SubtlexUS FREQlow value per sentence                                   |
| 226   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbFrL_C   | average SubtlexUS FREQlow value per token                                      |
| 227   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbCDL_C   | total SubtlexUS CDlow value                                                    |
| 228   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbCDL_C   | average SubtlexUS CDlow value per sentence                                     |
| 229   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbCDL_C   | average SubtlexUS CDlow value per token                                        |
| 230   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbSBW_C   | total SubtlexUS SUBTLWF value                                                  |
| 231   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbSBW_C   | average SubtlexUS SUBTLWF value per sentence                                   |
| 232   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbSBW_C   | average SubtlexUS SUBTLWF value per token                                      |
| 233   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbL1W_C   | total SubtlexUS Lg10WF value                                                   |
| 234   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbL1W_C   | average SubtlexUS Lg10WF value per sentence                                    |
| 235   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbL1W_C   | average SubtlexUS Lg10WF value per token                                       |
| 236   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbSBC_C   | total SubtlexUS SUBTLCD value                                                  |
| 237   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbSBC_C   | average SubtlexUS SUBTLCD value per sentence                                   |
| 238   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbSBC_C   | average SubtlexUS SUBTLCD value per token                                      |
| 239   | Lexico-Semantic     | WorF_         | Word Frequency Features              | to_SbL1C_C   | total SubtlexUS Lg10CD value                                                   |
| 240   | Lexico-Semantic     | WorF_         | Word Frequency Features              | as_SbL1C_C   | average SubtlexUS Lg10CD value per sentence                                    |
| 241   | Lexico-Semantic     | WorF_         | Word Frequency Features              | at_SbL1C_C   | average SubtlexUS Lg10CD value per token                                       |
| 242   | Shallow Traditional | ShaF_         | Shallow Features                     | to_Token_C   | total count of tokens x total count of sentence                                |
| 243   | Shallow Traditional | ShaF_         | Shallow Features                     | as_Token_C   | average count of tokens per sentence                                           |
| 244   | Shallow Traditional | ShaF_         | Shallow Features                     | as_Sylla_C   | average count of syllables per sentence                                        |
| 245   | Shallow Traditional | ShaF_         | Shallow Features                     | at_Sylla_C   | average count of syllables per token                                           |
| 246   | Shallow Traditional | ShaF_         | Shallow Features                     | as_Chara_C   | average count of characters per sentence                                       |
| 247   | Shallow Traditional | ShaF_         | Shallow Features                     | at_Chara_C   | average count of characters per token                                          |
| 248   | Shallow Traditional | TraF_         | Traditional Formulas Features        | FleschR_S    | Flesch Reading Ease                                                            |
| 249   | Shallow Traditional | TraF_         | Traditional Formulas Features        | SmogInd_S    | Smog Index                                                                     |
| 250   | Shallow Traditional | TraF_         | Traditional Formulas Features        | ColeLia_S    | Coleman Liau Readability Score                                                 |
| 251   | Shallow Traditional | TraF_         | Traditional Formulas Features        | DaleCha_S    | Dale Chall Readability Score                                                   |
| 252   | Shallow Traditional | TraF_         | Traditional Formulas Features        | Gunning_S    | Gunning Fog                                                                    |
| 253   | Shallow Traditional | TraF_         | Traditional Formulas Features        | AutoRea_S    | Automated Readability Index                                                    |
| 254   | Shallow Traditional | TraF_         | Traditional Formulas Features        | FleschG_S    | Flesch Kincaid Grade                                                           |
| 255   | Shallow Traditional | TraF_         | Traditional Formulas Features        | LinseaW_S    | Linsear Write                                                                  |


## License
We license LingFeat source code under [(Creative Commons Attribution Share Alike 4.0 license CC-BY-SA-4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

Under CC-BY-SA-4.0 license, you are allowed to distribute, modify, or privately use this repository.

But patent use, trademark use, and warranty use are not permitted. Work building on top of LingFeat must be released under the same license. In some case, a similar license may be used.

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg