# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 10:30:57 2020

@author: nelso
getsentences takes a filename and churns out a list of sentences.
"""

import spacy
import re
import os
import pandas as pd
from tqdm import tqdm

import en_core_web_sm
nlp = en_core_web_sm.load()

from spacy.lang.en.stop_words import STOP_WORDS

def getsentences(myfile):

    with open(myfile, 'r') as f:
        mytext = f.readlines()
    
    mysentences = []
    for line in mytext:
        doc = nlp(line)
        sentences = [sent.string.strip() for sent in doc.sents]
        mysentences.extend(sentences)
    
    return(mysentences)

# #testing the function
# filename = 'files/Western Union Co_20170502-Text.txt'
# tokenized_sentences = getsentences(filename)