#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:22:59 2020

@author: mj
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def plotBarChart(cwd, sentiment, sentiment_score, ylabel, aspect, title = "'s Aspect Analysis"):
    xpos = np.arange(len(sentiment))
    plt.xticks(xpos,sentiment)
    plt.ylabel(ylabel)
    plt.title(aspect + title)
    plt.bar(xpos, sentiment_score)
    #plt.legend()
    savePlot(cwd, plt, aspect)
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
def plotPieChart(cwd, emotional_sentiment_score, emotional_sentiment, aspect, title = "'s Emotional Sentiment Analysis"):
    fig, ax = plt.subplots()
    ax.pie(emotional_sentiment_score,labels=emotional_sentiment, radius=1.5, autopct='%1.1f%%', shadow=True, explode=[0.1,0,0.2,0.1], startangle=180)
    ax.axis("equal")
    ax.set_title(aspect + title)
    savePlot(cwd, plt, aspect + "_E")
    
def savePlot(cwd, plt, aspect):
    plt.savefig(cwd+"/static/images/" + aspect + "S.png", bbox_inches='tight', pad_inches=0.1, transprarent=True)
    
def convertZeroAndOneDF(df):
    return df.eq(df.where(df != 0).max(1), axis=0).astype(int)

def concatDataFrame(df1, df2):
    return pd.concat([df1, df2], axis=1, join='inner')

def plotAllAspects(cwd):
    print("inside plotAllAspects ...")
    
    #test = pd.read_csv("".join(cwd+"/predicted_Altria Group Inc_20171026-Text.csv"))
    test = pd.read_csv("".join(cwd+"/output.csv"))
    
    df = test.drop(columns = [test.columns[0], test.columns[2], test.columns[3]])
    print(df.columns)
    length = len(df.columns)
    
    sentence = df.columns[0:1]
    emotional_sentiment = df.columns[length-4:]
    aspect = df.columns[1:length-8]
    sentiment = df.columns[length-8:length-4]
    
    dft = df.loc[:, sentence]
    dfa = df.loc[:, aspect]
    dfs = df.loc[:, sentiment]
    dfes = df.loc[:, emotional_sentiment]
    
    dfa = convertZeroAndOneDF(dfa)
    dfs = convertZeroAndOneDF(dfs)
    dfes = convertZeroAndOneDF(dfes)
    
    result = concatDataFrame(concatDataFrame(concatDataFrame(dft, dfa), dfs), dfes)
    
    cwd = os.getcwd()
    print("cwd from os - ", cwd)
    
    for i in range(len(aspect)):
        print(aspect[i])
        test = result[result[aspect[i]] == 1]
        sentiment_score = [sum(test.NIL), sum(test.Negative), sum(test.Neutral), sum(test.Positive)]
        print(sentiment_score)
        plotBarChart(cwd, sentiment, sentiment_score, "No. of Sentences", aspect[i])
    
    for i in range(len(aspect)):
        print(aspect[i])
        test = result[result[aspect[i]] == 1]
        emotional_sentiment_score = [sum(test.Confident), sum(test.Dodgy), sum(test['NIL.1']), sum(test.Uncertain)]
        print(emotional_sentiment_score)
        plotPieChart(cwd, emotional_sentiment_score, emotional_sentiment, aspect[i])
        
    return True
        
if __name__ == "__main__":
    cwd = os.getcwd()
    print("cwd - ", cwd)
    folderLocation = cwd.replace('Flask', 'data')
    print("folderLocation - ", folderLocation)
    plotAllAspects(folderLocation)
    