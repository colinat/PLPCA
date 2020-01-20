# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 20:06:23 2019

@author: Lalkrishna Adawani
"""

import requests, pandas as pd, numpy as np, json, os, matplotlib.pyplot as plt, webbrowser, csv, time 
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup

os.getcwd()
#os.chdir('/Users/jacobimmanuel/Downloads')
#os.chdir('C:/Users/Lalkrishna Adawani/Downloads/Compressed')
os.chdir('C:/Users/MJ/Downloads/steam_reviews-master/data/')

OpenOff = open('Sid_Meiers_Civilization_5.jsonlines')

Off = OpenOff.readlines()
type(Off[0])

List = []
for i in range(len(Off)):
    d = json.loads(Off[i])
    List.append(d)
    
type(List[0])

Off1 = json_normalize(List)

Off1.to_csv('Sid_Meiers_Civilization_5.csv')
