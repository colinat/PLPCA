# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:20:46 2020

@author: nelso
"""
import pandas as pd

#N = 1 #read first 50 lines to sandbox
#with open('datasets/mini-normal1.json', encoding = "utf8") as json_file:
#    head = [next(json_file) for x in range(N)]

df = pd.read_csv("datasets/steamreview.csv", nrows=100000, header = None)
df.columns = ["Game Id", "Review", "Sentiment", "Useful"]

df.to_csv('steam_small.csv')
