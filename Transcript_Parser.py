# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:21:18 2020

@author: nelso
"""
import spacy
nlp = spacy.load("en_core_web_sm")

import pandas as pd
import os

directory = os.fsencode('datasets/transcripts/By Sector/healthcare/')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): 
        myfile = os.path.join('datasets/transcripts/By Sector/healthcare/', filename)
        with open(myfile, 'r') as file:
            mydata = file.readlines()
        
        sentences = []
        mywords = []
        lemmas = []
        mytags = []
        myshape = []
        
        for lines in mydata:
            doc = nlp(lines)
            for sent in doc.sents:
                sentences.append(sent.string.strip())
#            mytokens = [token.text for token in doc]
#            print(mytokens)
            for token in doc:
#            print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#            token.shape_, token.is_alpha, token.is_stop)
                mywords.append(token.text)
                lemmas.append(token.lemma_)
                mytags.append(token.tag_)
                myshape.append(token.shape_)
        
        mydf = pd.DataFrame({'Word': mywords,
                             'Lemma': lemmas,
                             'POSTag': mytags,
                             'Shape': myshape})
        mysentences = pd.DataFrame({'Sentences': sentences})

        mydf.to_csv(''.join(['datasets/transcripts/By Sector/healthcare/',filename[:-4],'.csv']))
        mysentences.to_csv(''.join(['datasets/transcripts/By Sector/healthcare/',filename[:-4],'-sentences.csv']))
    else:
        continue