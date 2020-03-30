# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:17:30 2020

@author: nelso
"""
import os
import numpy as np
#os.chdir(r"C:\Users\nelso\Documents\Data Science\Python Projects\bertsentiment")

##### LOADING CATEGORIES
# cat is a json file prepared when building the model.
# preparing categories
categories = {'Aspect' : ["sales","earnings","op_costs","products_services","organic_expansion","acquisitions","competition","op_risks","debt","not_applicable","NIL","Aspect"],
              'Sentiment' : ["Negative","Neutral","Positive","Sentiment"],
              'Emotion' : ["Confident","Dodgy","NIL","Uncertain","Emotion"]}

#### SETTING UP TORCH
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
n_gpu = torch.cuda.device_count()
# torch.cuda.get_device_name(0)

###### 
# LOADING THE MODEL
######

from transformers import BertTokenizer
from transformers import BertForSequenceClassification, AdamW, BertConfig
ROOT_PATH = os.path.dirname(os.path.abspath('__file__'))
modelLocation = ROOT_PATH.replace('Flask', 'data')
print('modelLocation - ', modelLocation)
    
def modelloader(my_model = 'Aspect'):

    if my_model == 'Aspect':
        output_dir = modelLocation + '/a_model_save/'
        num_labels = 11
    elif my_model == 'Sentiment':
        output_dir = modelLocation + '/s_model_save/'
        num_labels = 3
    elif my_model == 'Emotion':
        output_dir = modelLocation + '/e_model_save/'
        num_labels = 4
    else:
        print('Word unrecognized. Defaulting to Emotion.')
        output_dir = modelLocation + '/e_model_save/'
        num_labels = 4
    
    print('output_dir - ', output_dir)
    model = BertForSequenceClassification.from_pretrained(output_dir, num_labels = num_labels)
    print('####')
    print("Model at /{} loaded successfully.".format(output_dir))
    
    return(model)

tokenizer = BertTokenizer.from_pretrained(modelLocation + '/a_model_save/')
##########
import argparse
import logging
import re

from torch.utils.data.distributed import DistributedSampler
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler

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

def process_into_features(a_line, echo=False):
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

def predict_one_line(a_line, classifier = None):
    
    if classifier == None:
        print("Select a model: Aspect, Sentiment, Emotion")
        return(None)
    
    # Load and copy the model to the GPU.
    model= modelloader(classifier)
    model.to(device)
    
    a_line = processText(a_line)
    tokenized_line = process_into_features(a_line)

    prediction_input_ids = torch.tensor([tokenized_line.input_ids], dtype=torch.long) # Token ids for every sentences in individual list
    prediction_input_mask = torch.tensor([tokenized_line.input_mask], dtype=torch.long)
    # Telling the model not to compute or store gradients, saving memory and 
    # speeding up prediction
    with torch.no_grad():
        # Forward pass, calculate logit predictions
        logits = model(prediction_input_ids, token_type_ids=None, 
                       attention_mask=prediction_input_mask)

        y_prob = logits[0].softmax(dim = -1) # normalizes values along axis 1

    # Move logits to CPU
    y_prob = y_prob.detach().cpu().numpy().tolist()
    classes = categories[classifier]
    
    y_prob[0].append(classes[y_prob[0].index(max(y_prob[0]))])
    del(model)
    return(y_prob[0])

# p_mytext = "thanks for attending our call."

# predictions = predict_one_line(p_mytext, classifier = 'Sentiment')

# print('Testing the predictions to confirm if everything is loaded fine.')
# print('######')
# print(p_mytext)

# print('######')
# print(predictions, categories[1])

########
# This section for predicting multiple lines.
########

def predict_multiple_lines(text_list, classifier = None):
    
    if classifier == None:
        print("Select a model: Aspect, Sentiment, Emotion")
        return(None)
    
    # Load and copy the model to the GPU.
    model = modelloader(classifier)
    model.to(device)
    
    batch_size = 8
    
    features = []
    for line in text_list:
        line = processText(line)
        features.append(process_into_features(line))

    prediction_input_ids = torch.tensor([f.input_ids for f in features], dtype=torch.long) # Token ids for every sentences in individual list
    prediction_input_ids_index = torch.arange(prediction_input_ids.size(0), dtype=torch.long) # Index for each sentences in one list

    prediction_input_mask = torch.tensor([f.input_mask for f in features], dtype=torch.long)
    prediction_data = TensorDataset(prediction_input_ids, prediction_input_mask, prediction_input_ids_index)

    # Create the DataLoader for our testing set.

    prediction_sampler = SequentialSampler(prediction_data)
    prediction_dataloader = DataLoader(prediction_data, sampler=prediction_sampler, batch_size=batch_size)
    
    predictions = []
    
    print("Lines to process: {}".format(len(text_list)))
    print("Total Batches: {}".format(len(prediction_dataloader)))
    print("Predicting {}".format(classifier))
    classes = categories[classifier]
          
    for batch in prediction_dataloader:
        # Add batch to GPU
        batch = tuple(t.to(device) for t in batch)

        # Unpack the inputs from our dataloader
        b_input_ids, b_input_mask, b_input_ids_index = batch

        # Telling the model not to compute or store gradients, saving memory and 
        # speeding up prediction
        with torch.no_grad():
            # Forward pass, calculate logit predictions
            logits = model(b_input_ids, token_type_ids=None, 
                                         attention_mask=b_input_mask)

            y_prob = logits[0].softmax(dim = -1) # normalizes values along axis 1

            # Move logits to CPU
            
            y_prob = y_prob.detach().cpu().numpy().tolist()
            for ind in range(len(y_prob)):
                y_prob[ind].append(classes[y_prob[ind].index(max(y_prob[ind]))])
            
            predictions.extend(y_prob)
        
        print('Batch done!')
    
    predictions = pd.DataFrame(predictions, columns = classes)
    del(model)
    
    return(predictions)

# line_list = ['Hello, my name is nelson.','This is a statement about organic expansion.','This is a statement about risks of the business.',\
#              'Hello, my name is nelson.','This is a statement about organic expansion.','This is a statement about risks of the business.',\
#              'Hello, my name is nelson.','This is a statement about organic expansion.','This is a statement about risks of the business.',\
#              'Hello, my name is nelson.','This is a statement about organic expansion.','This is a statement about risks of the business.']

# lines = pd.DataFrame(line_list, columns = ['Sentence'])
# predictions = predict_multiple_lines(line_list, classifier = 'Aspect')
# predictions2 = predict_multiple_lines(line_list, classifier = 'Sentiment')
# predictions3 = predict_multiple_lines(line_list, classifier = 'Emotion')

# mydata = pd.concat([lines.reset_index(drop=True), predictions.reset_index(drop=True), predictions2.reset_index(drop=True), predictions3], axis=1)

# print('Testing the predictions to confirm if everything is loaded fine.')
# print('######')
# print(line_list)

# print('######')
# print(mydata)

########

########
# Processing txt files.
########

from spacy_processing import getsentences
# filenames = os.listdir("files/")
# print(filenames)

####### 
# Following function takes in a filename and outputs a processed csv.
def getcsv(file):
    fileLocation = ROOT_PATH.replace('Flask', 'data/')
    filename = fileLocation + "output.csv"
    mytranscript = getsentences(file)
    
    lines = pd.DataFrame(mytranscript, columns = ['Sentence'])
    aspect= predict_multiple_lines(mytranscript, classifier = 'Aspect')
    sentiment= predict_multiple_lines(mytranscript, classifier = 'Sentiment')
    emotion= predict_multiple_lines(mytranscript, classifier = 'Emotion')
    
    mydata = pd.concat([lines.reset_index(drop=True), aspect.reset_index(drop=True), sentiment.reset_index(drop=True), emotion], axis=1)
    
    mydata.to_csv(filename, encoding='utf-8')


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
    

