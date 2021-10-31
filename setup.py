"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: setup.py
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -
"""

from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'lingfeat',

  #required for multi-level directory packages
  packages=find_packages(),

  version = '1.0.0-beta.19',
  license='cc-by-sa-4.0',
  description = 'Comprehensive Linguistic Features Extraction for Readability Assessment', 
  author = 'Bruce W. Lee',        
  author_email = 'phys.w.s.lee@gmail.com', 
  url = 'https://github.com/brucewlee',
  keywords = ['NLP', 'LINGUISTIC FEATURE', 'READABILITY'], 
  install_requires=[            # I get to this in a second
          'spacy >= 3.0.0',
          'supar',
          'gensim',
          'pandas',
          'python-Levenshtein'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  include_package_data=True,
)