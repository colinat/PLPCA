# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:55:39 2020

@author: MJ
"""

import pandas as pd
import os
os.chdir(r"A:/GIT Repository/PLPCA")

sectors = [
      'Consumer_discretionaries'
     ,'Consumer_staples'
     ,'healthcare'
     ,'Industrials'
     ,'InfoTech'
           ]

for sector in sectors:
    
    directory = os.fsencode('datasets/transcripts/By Sector/' + sector)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".txt"): 
            myfile = os.path.join(directory, file)
            with open(myfile, 'r', encoding="utf8") as file:
                mydata = file.readlines()
            sentences = []
            for line in mydata:
                #print(line)
                sentences.append(str(line).strip())
            
            mysentences = pd.DataFrame({'Sentences': sentences})
            #print(mysentences.head())
    
            mysentences.to_csv(''.join(['Flask/File_To_Upload/', sector, '/', filename[:-4],'.csv']), index = None, header=False)
        else:
            continue