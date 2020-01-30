# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:32:33 2020

@author: MJ
"""

import pandas as pd
import os

directory = os.fsencode('A:/TRANSCRIPT/')

TranscriptName = []
TranscriptContent = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"): 
        myfile = os.path.join('A:/TRANSCRIPT/', filename)
        print(filename)
        filenameToString = ''.join([str(elem) for elem in filename])
        with open(myfile, 'r', encoding="utf8") as file:
            mydata = file.readlines()
            mydataToString = ' '.join([str(elem) for elem in mydata])

        TranscriptName.append(filenameToString)
        TranscriptContent.append(mydataToString)
    else:
        continue

mydf = pd.DataFrame({"Transcript_Name": TranscriptName,
                             "Transcript_Content": TranscriptContent}) 
mydf.to_csv(''.join(['A:/TRANSCRIPT/Transcript-consolidate.csv']))

print
print("Transcript_Name = ",mydf.Transcript_Name[0])
print("Transcript_Content = ",mydf.Transcript_Content[0])
print("Shape = ", mydf.shape)
print("Transcript_Name = ",mydf.Transcript_Name[574])
print("Transcript_Content = ",mydf.Transcript_Content[574])
