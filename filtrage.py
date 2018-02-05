#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:11:43 2018

@author: Elise Benois & Sibylle de Gerin-Ricard
"""

import json
import spacy
import pickle
nlp = spacy.load('fr')
#stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/' + 'functions/stopwords.p', 'rb'))
stop_words = pickle.load(open('/Users/Elise/SID_Terrorisme/stopwords.p', 'rb'))

# Enlever les articles où il y a marqué en direct
f = open("/Users/Elise/SID_Terrorisme/article_nouvelobs_v0/art_noob_1_2018-02-01_robot.json",'rb')
docs = [json.loads(s.decode('utf-8')) for s in f.readlines()]
titres = [x['title'] for x in docs]
content = [x['content'] for x in docs]

# cleanText

'''
La fonction cleanTokens permet de nettoyer l'article c'est-a-dire d'enlever
toute la ponctuation
'''


def cleanText(sent):
    sent = sent.lower()
    sent = "".join([x if x.isalpha() else " " for x in sent])
    sent = " ".join(sent.split())
    return sent


clean2Text = [cleanText(x) for x in content]


# tokenize

'''
La fonction tokenize va permettre d'obtenir chaque mot separer.
'''


def tokeniz(text):  # Tokenize a text with library Spacy
    doc = nlp(text)
    return doc


b = tokeniz(clean2Text[0]) 

# b[8] renvoie le 8e mot


# stop_words

'''
On veut retirer les stopwords de a liste de mots
'''

for i in b:
    if i in stop_words:
        tag = "STOPWORD"
        continue
