# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:17:30 2020

@author: nelso
"""
import os
import json
import numpy as np
os.chdir(r"C:\Users\nelso\Documents\Data Science\Python Projects\bertsentiment")

##### LOADING CATEGORIES
# cat is a json file prepared when building the model.

with open('cat2.txt', 'r') as reader:
    myfile = reader.readlines()

categories = []
for item in myfile:
    categories.append(json.loads(item))

#### SETTING UP TORCH
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
n_gpu = torch.cuda.device_count()
# torch.cuda.get_device_name(0)

###### 
# LOADING THE MODEL
######

import torch.nn as nn
from transformers.modeling_bert import BertPreTrainedModel, BertModel
from torch.nn import CrossEntropyLoss
from torch.nn import BCEWithLogitsLoss

class BertForMultitask(BertPreTrainedModel):
    def __init__(self, config):
        super(BertForMultitask, self).__init__(config)
        self.bert = BertModel(config)
        # self.dropout = nn.Dropout(config.hidden_dropout_prob)
        
        self.classifier = nn.Linear(config.hidden_size, out_features=11)
        self.s_classifier = nn.Linear(config.hidden_size, out_features=3)
        self.e_classifier = nn.Linear(config.hidden_size, out_features=4)

        self.init_weights()

    def forward(self, input_ids=None, token_type_ids=None, attention_mask=None, 
                labels=None, s_labels=None, e_labels=None):
        _, pooled_output  = self.bert(input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask)
        # pooled_output = self.dropout(pooled_output)
        
        logits = self.classifier(pooled_output)
        s_logits = self.s_classifier(pooled_output)
        e_logits = self.e_classifier(pooled_output)
        
        outputs = logits, s_logits, e_logits

        return outputs
            
from transformers import BertTokenizer
from transformers import BertForSequenceClassification, AdamW, BertConfig

# Load a trained model and vocabulary that you have fine-tuned
output_dir = 'data/model_save_MultiClass/'

# Load a trained model and vocabulary that you have fine-tuned
model = BertForMultitask.from_pretrained(output_dir)
tokenizer = BertTokenizer.from_pretrained(output_dir)

print("Model at /{} loaded successfully.".format(output_dir))
# Copy the model to the GPU.
model.to(device)

import argparse
import collections
import logging
import re
import math

from torch.utils.data.distributed import DistributedSampler
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler

from transformers import BertModel

import spacy
import pandas as pd
from tqdm import tqdm
# In the original paper, the authors used a length of 512.
#MAX_LEN was decided when the model is trained.

##### PREPARING THE TEXT INTO ACCEPTABLE LINES
MAX_LEN = 512
seq_length = MAX_LEN # type=int

logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s', 
                    datefmt = '%m/%d/%Y %H:%M:%S',
                    level = logging.INFO)
logger = logging.getLogger(__name__)

class InputExample(object):

    def __init__(self, unique_id, text_a, text_b):
        self.unique_id = unique_id
        self.text_a = text_a
        self.text_b = text_b
        #self.labels = labels

def processText(line, unique_id = 0):
    line = line.strip()
    text_a = None
    text_b = None
    m = re.match(r"^(.*) \|\|\| (.*)$", line)
    if m is None:
      text_a = re.sub(r"(\|\|\|)$", "", line)
    else:
      text_a = m.group(1)
      text_b = m.group(2)

    return(InputExample(unique_id=unique_id, text_a=text_a, text_b=text_b))

# The maximum total input sequence length after WordPiece tokenization. 
# Sequences longer than this will be truncated, and sequences shorter than this will be padded.

def _truncate_seq_pair(tokens_a, tokens_b, max_length):
    """Truncates a sequence pair in place to the maximum length."""

    # This is a simple heuristic which will always truncate the longer sequence
    # one token at a time. This makes more sense than truncating an equal percent
    # of tokens from each, since if one sequence is very short then each token
    # that's truncated likely contains more information than a longer sequence.
    while True:
        total_length = len(tokens_a) + len(tokens_b)
        if total_length <= max_length:
            break
        if len(tokens_a) > len(tokens_b):
            tokens_a.pop()
        else:
            tokens_b.pop()

class InputFeatures(object):
    """A single set of features of data."""

    def __init__(self, unique_id, tokens, input_ids, input_mask, input_type_ids):
        self.unique_id = unique_id
        #self.labels = labels
        self.tokens = tokens
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.input_type_ids = input_type_ids

def process_into_features(a_line, echo=True):
    tokens_a = tokenizer.tokenize(a_line.text_a)

    tokens_b = None
    if a_line.text_b:
        tokens_b = tokenizer.tokenize(a_line.text_b)

    if tokens_b:
        # Modifies `tokens_a` and `tokens_b` in place so that the total
        # length is less than the specified length.
        # Account for [CLS], [SEP], [SEP] with "- 3"
        _truncate_seq_pair(tokens_a, tokens_b, seq_length - 3)
    else:
        # Account for [CLS] and [SEP] with "- 2"
        if len(tokens_a) > seq_length - 2:
            tokens_a = tokens_a[0:(seq_length - 2)]

    tokens = []
    input_type_ids = []
    tokens.append("[CLS]")
    input_type_ids.append(0)
    for token in tokens_a:
        tokens.append(token)
        input_type_ids.append(0)
    tokens.append("[SEP]")
    input_type_ids.append(0)

    if tokens_b:
        for token in tokens_b:
            tokens.append(token)
            input_type_ids.append(1)
        tokens.append("[SEP]")
        input_type_ids.append(1)

    input_ids = tokenizer.convert_tokens_to_ids(tokens)

    # The mask has 1 for real tokens and 0 for padding tokens. Only real
    # tokens are attended to.
    input_mask = [1] * len(input_ids)

    # Zero-pad up to the sequence length.
    while len(input_ids) < seq_length:
        input_ids.append(0)
        input_mask.append(0)
        input_type_ids.append(0)

    assert len(input_ids) == seq_length
    assert len(input_mask) == seq_length
    assert len(input_type_ids) == seq_length

    if echo == True:
        logger.info("******")
        logger.info("unique_id: %s" % (a_line.unique_id))
        #logger.info("labels: %s" % (a_line.labels))
        logger.info("tokens: %s" % " ".join([str(x) for x in tokens]))
        logger.info("input_ids: %s" % " ".join([str(x) for x in input_ids]))
        logger.info("input_mask: %s" % " ".join([str(x) for x in input_mask]))
        logger.info(
            "input_type_ids: %s" % " ".join([str(x) for x in input_type_ids]))
  
    return(InputFeatures(
                unique_id=a_line.unique_id,
                
                tokens=tokens,
                input_ids=input_ids,
                input_mask=input_mask,
                input_type_ids=input_type_ids))

# Processing a single InputExample object into an InputFeatures object.
# p_mytext = "Let us test if this tokenizer works. Sentence embeddings.\
# I will also include a proper noun: Boeing Airlines,\
# and a garbage word: llakskokao."

# text_a = processText(p_mytext)
# tokenized_line = process_into_features(text_a)

# print(' ')
# print('Max sentence length: ' + str(MAX_LEN))
    
########
# This section for predicting a single line.
########

def predict_one_line(tokenized_line):
    batch_size = 32
    local_rank = -1 

    prediction_input_ids = torch.tensor([tokenized_line.input_ids], dtype=torch.long) # Token ids for every sentences in individual list
    prediction_input_ids_index = torch.arange(prediction_input_ids.size(0), dtype=torch.long) # Index for each sentences in one list

    prediction_input_mask = torch.tensor([tokenized_line.input_mask], dtype=torch.long)
    # Telling the model not to compute or store gradients, saving memory and 
    # speeding up prediction
    with torch.no_grad():
        # Forward pass, calculate logit predictions
        logits, s_logits, e_logits = model(prediction_input_ids, token_type_ids=None, 
                                     attention_mask=prediction_input_mask)

        y_prob = logits.softmax(dim = -1) # normalizes values along axis 1
        s_y_prob = s_logits.softmax(dim = -1)
        e_y_prob = e_logits.softmax(dim = -1)

    # Move logits to CPU
    y_prob = y_prob.detach().cpu().numpy()
    s_y_prob = s_y_prob.detach().cpu().numpy()
    e_y_prob = e_y_prob.detach().cpu().numpy()
    return(y_prob, s_y_prob, e_y_prob)

# p_mytext = "thanks for attending our call."

# text_a = processText(p_mytext)
# tokenized_line = process_into_features(text_a)
# aspect, sentiment, emotion = predict_one_line(tokenized_line)

# print('Testing the predictions to confirm if everything is loaded fine.')
# print('######')
# print(p_mytext)

# print('######')
# print(aspect, categories[0])
# print(sentiment, categories[1])
# print(emotion, categories[2])

########
# This section for predicting multiple lines.
########

def predict_multiple_lines(text_list):
    batch_size = 8
    local_rank = -1 
    
    features = []
    for line in text_list:
        line = processText(line)
        features.append(process_into_features(line))

    prediction_input_ids = torch.tensor([f.input_ids for f in features], dtype=torch.long) # Token ids for every sentences in individual list
    prediction_input_ids_index = torch.arange(prediction_input_ids.size(0), dtype=torch.long) # Index for each sentences in one list

    prediction_input_mask = torch.tensor([f.input_mask for f in features], dtype=torch.long)
    prediction_data = TensorDataset(prediction_input_ids, prediction_input_mask, prediction_input_ids_index)

    # Create the DataLoader for our testing set.
    if local_rank == -1:
        prediction_sampler = SequentialSampler(prediction_data)
    else:
        prediction_sampler = DistributedSampler(prediction_data)
    prediction_dataloader = DataLoader(prediction_data, sampler=prediction_sampler, batch_size=batch_size)
    
    combined_aspect = []
    combined_sentiment = []
    combined_emotion = []
    
    print("Lines to process: {}".format(len(text_list)))
    print("Total Batches: {}".format(len(prediction_dataloader)))
          
    for batch in prediction_dataloader:
        # Add batch to GPU
        batch = tuple(t.to(device) for t in batch)

        # Unpack the inputs from our dataloader
        b_input_ids, b_input_mask, b_input_ids_index = batch

        # Telling the model not to compute or store gradients, saving memory and 
        # speeding up prediction
        with torch.no_grad():
            # Forward pass, calculate logit predictions
            logits, s_logits, e_logits = model(b_input_ids, token_type_ids=None, 
                                         attention_mask=b_input_mask)

            y_prob = logits.softmax(dim = -1) # normalizes values along axis 1
            s_y_prob = s_logits.softmax(dim = -1)
            e_y_prob = e_logits.softmax(dim = -1)

            # Move logits to CPU
            combined_aspect.append(y_prob.detach().cpu().numpy())
            combined_sentiment.append(s_y_prob.detach().cpu().numpy())
            combined_emotion.append(e_y_prob.detach().cpu().numpy())
        
        print('Batch done!')
    
    combined_aspect = np.concatenate(combined_aspect, axis=0)
    combined_sentiment = np.concatenate(combined_sentiment, axis=0)
    combined_emotion = np.concatenate(combined_emotion, axis=0)
    return(combined_aspect, combined_sentiment, combined_emotion)

# line_list = ['Hello, my name is nelson.','This is a statement about organic expansion.','This is a statement about risks of the business.']

# aspect, sentiment, emotion = predict_multiple_lines(line_list)

# print('Testing the predictions to confirm if everything is loaded fine.')
# print('######')
# print(line_list)

# print('######')
# print(aspect, categories[0])
# print(sentiment, categories[1])
# print(emotion, categories[2])

########

########
# Processing txt files.
########

from spacy_processing import getsentences
# filenames = os.listdir("files/")
# print(filenames)

####### 
# Following function takes in a filename and outputs a processed csv.
def getcsv(file, filename = "output.csv"):
    mytranscript = getsentences(file)
    aspect, sentiment, emotion = predict_multiple_lines(mytranscript)
    
    mydata = np.concatenate((aspect, sentiment, emotion), axis = 1)
    colnames = []
    for item in categories:
        colnames.extend(item.values())
    
    mydf = pd.DataFrame(mydata, columns= colnames)
    mydf.insert(loc = 0, column = 'Sentence', value = mytranscript)
    
    mydf.to_csv(filename, encoding='utf-8')


# mynplist = []
# for line in range(50):
#     print(line)
    
#     p_mytext = mytranscript[line]
#     text_a = processText(p_mytext)
#     tokenized_line = process_into_features(text_a)
#     aspect, sentiment, emotion = predict_one_line(tokenized_line)
    
#     mydata = np.concatenate((aspect, sentiment, emotion), axis = 1)
    
#     mynplist.append(mydata)  
# while True:
#     p_mytext = input("Type 1 to test the model, 2 to process a file. If you want to exit, type 'Exit': ")
    
#     if p_mytext == 'Exit':
#         exit()
#     elif p_mytext == '1':
#         mytext = input("Enter a Sentence: ")
#         text_a = processText(mytext)
#         tokenized_line = process_into_features(text_a)
#         logits = predict_one_line(tokenized_line)
        
#         print('######')
#         print(mytext)
        
#         print('######')
#         print(aspect, categories[0])
#         print(sentiment, categories[1])
#         print(emotion, categories[2])
        
#     elif p_mytext == '2':
#         myfile = input("Enter the file name to process: ")
#         getcsv(myfile)
        
#         print("file can be found at output.csv")
        
#     else:
#         print("Unrecognied Selection.")
#         print(" ")
#         next
    

