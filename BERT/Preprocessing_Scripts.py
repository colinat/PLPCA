#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
from tqdm import tqdm
import spacy
import argparse


# In[10]:


import glob
import os

sector = ["Consumer_discretionaries", "Consumer_staples", "healthcare",
         "Industrials", "InfoTech"]

file = []

for sec in sector:
    item = glob.glob(os.path.join(os.getcwd(), sec, "*.txt"))
    file.append(item)


# In[11]:


file_list = [item for sublist in file for item in sublist]
print(len(file_list))


# In[18]:


print(file_list[0:2])


# In[7]:


get_ipython().system('python -m spacy download en_core_web_sm -q')


# In[8]:


nlp = spacy.load('en_core_web_sm')
nlp.add_pipe(nlp.create_pipe('sentencizer'))


# In[19]:


filename_list = []

for file_path in file_list:
    file_name = os.path.basename(file_path)
    file_name = os.path.splitext(file_name)[0]
    filename_list.append(file_name)
    
print(filename_list[0:3])


# In[20]:


scripts = []
for file_path in file_list:
    file_name = os.path.basename(file_path)
    file_name = os.path.splitext(file_name)[0]
    
    with open(file_path, 'r') as file:
        mydata = file.readlines()
        for lines in mydata:
            scripts.append(lines)

#Save the Combined Scripts to Disk
with open("scripts.txt", 'w') as output:
    for row in scripts:
        output.write(str(row) + '\n')


# In[21]:


scripts[0:3]


# In[22]:


# get sentence segemented review with #sentences > 2
def sentence_segment_filter_docs(doc_array):
    sentences = []

    for doc in nlp.pipe(doc_array, disable=['parser', 'tagger', 'ner'], batch_size=1000, n_threads=8):
        sentences.append([sent.text.strip() for sent in doc.sents])

    return sentences


# In[23]:


print(f'Found {len(scripts)} transcripts')
print(f'Tokenizing Transcripts...')

sentences = sentence_segment_filter_docs(scripts)
nr_sents = sum([len(s) for s in sentences])
print(f'Segmented {nr_sents} transcript sentences')


# In[24]:


# Save to file
fn_out = f'transcript_corpus.txt'


# In[25]:


with open(fn_out, "w") as f:
    for sents in tqdm(sentences):
        real_sents = []
        for s in sents:
            x = s.replace(' ', '').replace('\n', '')
            if x != '':
                real_sents.append(s.replace('\n', ''))
        # filter only paragraph more than or equal to 1 sentence        
        if len(real_sents) >= 1:
            str_to_write = "\n" + "\n".join(real_sents) + "\n"
            f.write(str_to_write)

print(f'Done writing to {fn_out}')

