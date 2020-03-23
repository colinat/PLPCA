#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:22:59 2020

@author: mj
"""

def plotBarChart(cwd, sentiment, sentiment_score, ylabel, aspect, title = "'s Aspect Analysis"):
    import matplotlib.pyplot as plt
    import numpy as np
    xpos = np.arange(len(sentiment))
    plt.xticks(xpos,sentiment)
    plt.ylabel(ylabel)
    plt.title(aspect + title)
    plt.bar(xpos, sentiment_score)
    #plt.legend()
    savePlot(cwd, plt, aspect)
    
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
def plotPieChart(cwd, emotional_sentiment_score, emotional_sentiment, aspect, title = "'s Emotional Sentiment Analysis"):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.pie(emotional_sentiment_score,labels=emotional_sentiment, radius=1.5, autopct='%1.1f%%', shadow=True, explode=[0.1,0,0.2], startangle=180)
    ax.axis("equal")
    ax.set_title(aspect + title)
    savePlot(cwd, plt, aspect + "_E")
    
def savePlot(cwd, plt, aspect):
    plt.savefig(cwd+"/static/images/" + aspect + "S.png", bbox_inches='tight', pad_inches=0.1, transprarent=True)

def plotAllAspects(cwd):
    print("inside plotAllAspects ...")
    import pandas as pd
    test = pd.read_csv("".join(cwd+"/test.csv"))

    emotional_sentiment = ['Confident', 'UnCertain', 'Doggy']
    aspect = list(["Sales", "Op_costs", "Products_services"])
    sentiment = ['Positive', 'Negative', 'Neutral']
    for i in range(len(aspect)):
        print(aspect[i])
        test_sales = test[test[aspect[i]] == 1]
        sentiment_score = [sum(test_sales.Positive), sum(test_sales.Negative), sum(test_sales.Neutral)]
        print(sentiment_score)
        plotBarChart(cwd, sentiment, sentiment_score, "No. of Sentences", aspect[i])
    
    for i in range(len(aspect)):
        print(aspect[i])
        test_sales = test[test[aspect[i]] == 1]
        emotional_sentiment_score = [sum(test_sales.Confident), sum(test_sales.UnCertain), sum(test_sales.Doggy)]
        print(emotional_sentiment_score)
        plotPieChart(cwd, emotional_sentiment_score, emotional_sentiment, aspect[i])
        
    return True
        
if __name__ == "__main__":
    import os
    cwd = os.getcwd()
    plotAllAspects(cwd)
    