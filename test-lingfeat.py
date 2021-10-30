from lingfeat import extractor

text = "TAEAN, South Chungcheong Province -- Just before sunup, Lee Young-ho, a seasoned fisherman with over 30 years of experience, silently waits for boats carrying blue crabs as the season for the seafood reaches its height. Soon afterward, small and big boats sail into Sinjin Port in Taean County, South Chungcheong Province, the second-largest source of blue crab after Incheon, accounting for 29 percent of total production of the country. A crane lifts 28 boxes filled with blue crabs weighing 40 kilograms each from the boat, worth about 10 million won ($8,500). “It has been a productive fall season for crabbing here. The water temperature is a very important factor affecting crab production. They hate cold water,” Lee said. The temperature of the sea off Taean appeared to have stayed at the level where crabs become active. If the sea temperature suddenly drops, crabs go into their winter dormancy mode, burrowing into the mud and sleeping through the cold months. "

LingFeat = extractor.pass_text(text)

LingFeat.preprocess()

WoKF = LingFeat.WoKF_() # Wikipedia Knowledge Features
WBKF = LingFeat.WBKF_() # WeeBit Corpus Knowledge Features
OSKF = LingFeat.OSKF_() # OneStopEng Corpus Knowledge Features

# Discourse (Disco) Features
EnDF = LingFeat.EnDF_() # Entity Density Features
EnGF = LingFeat.EnGF_() # Entity Grid Features

# Syntactic (Synta) Features
PhrF = LingFeat.PhrF_() # Noun/Verb/Adj/Adv/... Phrasal Features
TrSF = LingFeat.TrSF_() # (Parse) Tree Structural Features
POSF = LingFeat.POSF_() # Noun/Verb/Adj/Adv/... Part-of-Speech Features

# Lexico Semantic (LxSem) Features
TTRF = LingFeat.TTRF_() # Type Token Ratio Features
VarF = LingFeat.VarF_() # Noun/Verb/Adj/Adv Variation Features 
PsyF = LingFeat.PsyF_() # Psycholinguistic Difficulty of Words (AoA Kuperman)
WoLF = LingFeat.WorF_() # Word Familiarity from Frequency Count (SubtlexUS)

# Shallow Traditional (ShTra) Features
ShaF = LingFeat.ShaF_() # Shallow Features (e.g. avg number of tokens)
TraF = LingFeat.TraF_() # Traditional Formulas 

print(WoKF)
print(WBKF)
print(OSKF)

print(EnDF)
print(EnGF)

print(PhrF)
print(TrSF)
print(POSF)

print(TTRF)
print(VarF)
print(PsyF)
print(WoLF)

print(ShaF)
print(TraF)