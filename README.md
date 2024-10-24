# Dummy Project

## Overview
*The Dummy project analyzes a full article stored in corpus.txt and counts the frequency of a specified word or phrase (token).*
## File structure 
* dummy/
│
├── __init__.py
├── counter.py
└── prompt.py
corpus.txt *


## File Descriptions
* dummy/__init__.py: Marks the directory as a Python package (can be empty).
* dummy/counter.py: count_word(text, word): Counts occurrences of word in text.
* read_corpus(): Reads and returns the content of corpus.txt.dummy/prompt.py:
* report_count(token): Reports how many times token appears in the article.
* corpus.txt: Contains the full text of the article to be analyzed. 

## Usage 
### Run the following code to analyze a specific token:
from importlib import reload
import dummy.prompt

reload(dummy.prompt)
from dummy.prompt import report_count

## Specify the token you want to count
token = "Newgate"
print(report_count(token))
