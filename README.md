# LingFeat - Comprehensive Linguistic Features Extraction for Readability Assessment
## Overview

LingFeat is a Python research package for dealing with various handcrafted linguistic features (currently supports 218 linguistic features).

Most of these features are inspired from readability assessment (RA) research, a branch of NLP.

## Installation

1) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install LingFeat. (not supported now)
```bash
pip install foobar
```

2) Install from the repo.
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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)