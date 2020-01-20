# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 09:12:07 2020

@author: nelso
"""

import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("This is a text")
# Token texts
print([token.text for token in doc])

from spacy import displacy
doc = nlp(u'Rats are various medium-sized, long-tailed rodents.')

#Jupyter notebook works with render, Spyder = serve on localhost:5000
#displacy.render(doc, style='dep',jupyter=True)

#open localhost:5000
displacy.serve(doc, style="dep")
#displacy.serve(nlp("Larry Page founded Google"), style="ent")

#displacy.serve(doc, style="dep")

#doc = nlp("Larry Page founded Google")
#displacy.serve(doc, style="ent")

import pandas as pd

mydata = pd.read_csv("datasets/womens_clothing.csv", nrows=20)
sampletext = mydata['Review Text'][2]

nlp.add_pipe(nlp.create_pipe('sentencizer'))
doc = nlp(sampletext)
sentences = [sent.string.strip() for sent in doc.sents]

mytokens = [token.text for token in doc]
