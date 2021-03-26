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
pip install foobar
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

# extract features
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

## License
We license LingFeat source code under [(Creative Commons Attribution Share Alike 4.0 license CC-BY-SA-4.0)](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

Under CC-BY-SA-4.0 license, you are allowed to commercially use, distribute, modify, or privately use this repository.

But patent use, trademark use, and warranty use are not permitted. Work building on top of LingFeat must be released under the same license. In some case, a similar license may be used.