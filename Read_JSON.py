# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:20:46 2020

@author: nelso
"""
import pandas as pd

#N = 1 #read first 50 lines to sandbox
#with open('datasets/mini-normal1.json', encoding = "utf8") as json_file:
#    head = [next(json_file) for x in range(N)]

post_files = ['datasets/mafiadata/mini-normal1.json']
slot_files = ['datasets/mafiadata/mini-normal-slots.json']

posts = pd.concat(pd.read_json(fn, orient='records') for fn in post_files)
slots = pd.concat(pd.read_json(fn, orient='records') for fn in slot_files)

game_id = 71796 #Pick a game_id to sandbox
posts_1game = posts.loc[posts['game_id'] == game_id]
slots_1game = slots.loc[slots['game_id'] == game_id]

# for game 71796, Transcend was a goon.
# Lets read his comments.

lies = posts_1game.loc[posts_1game['author'] == 'Transcend']
lies2 = posts_1game.loc[posts_1game['author'] == 'Mulch']

truths = posts_1game.loc[posts_1game['author'] == 'Ryker']
truths2 = posts_1game.loc[posts_1game['author'] == 'FrozenFlame']
truths3 = posts_1game.loc[posts_1game['author'] == 'Zulfy']
