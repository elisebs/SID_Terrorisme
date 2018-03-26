#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:29:50 2018

@author: Elise
"""
import spacy
import json
import numpy as np
import nltk
import os
import pickle
from nltk.corpus import stopwords
nltk.download('stopwords')


def tokeniz(article):
    nlp = spacy.load('fr')
    doc = nlp(article)
    return doc


list_stopwords = []


def get_stopwords():

    for find_stopwords in b:
        if find_stopwords.is_stop:
            list_stopwords.extend([find_stopwords])
    for i in range(len(list_stopwords)):
        list_stopwords[i] = str(list_stopwords[i])
    list_stopwords_other = []

    for i in range(len(list_stopwords_other)):
        if list_stopwords_other[i] not in list_stopwords:
            np.unique(list_stopwords.append(list_stopwords_other[i]))
    return list_stopwords


path = '/Users/Elise/Documents/Travail/M1_SID/SID_Terrorisme/test/'
for i in os.listdir(path):
    if i != '.DS_Store':
        json_data = open(path + str(i))
        data = json.load(json_data)
        json_data.close()
        art = data['content']
        b = tokeniz(art)
        stop_words = get_stopwords()
        stop_words = np.unique(stop_words)


articles = {}
art = data['content']

stop_words_bis = stopwords.words('french')
stop_words_bis = np.unique(stop_words_bis)

list_stop_words = np.append(stop_words_bis, stop_words)
list_stop_words = np.unique(list_stop_words)


stop_words = get_stopwords()


lettre = ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f',
          'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n']

for i in lettre:
    list_stop_words.append(i)

list_stop_words = np.unique(list_stop_words)

list_stop_words = ['are', 'also', 'a', 'ai', 'aie', 'aient', 'aies',
                   'ailleurs', 'ainsi', 'ait', 'alors', 'après', 'as', 'assez',
                   'au', "ajourd'hui", 'aucun', 'aucune', 'aura', 'aurai',
                   'auraient', 'aurais', 'aurait', 'auras', 'aurez', 'auriez',
                   'aurions', 'aurons', 'auront', 'aussi', 'autre', 'autres',
                   'aux', 'avaient', 'avais', 'avait', 'avant', 'avec',
                   'avez', 'aviez', 'avions', 'avoir', 'avons', 'ayant',
                   'ayante', 'ayantes', 'ayants', 'ayez', 'ayons', 'beaucoup',
                   'bien', 'c', 'ce', 'ceci', 'cela', 'celle', 'celui',
                   'certain', 'certaines', 'ces', 'cet', 'cette', 'ceux',
                   'comme', 'comment', 'contre', 'd', 'dans', 'eu',
                   'de', 'debout', 'depuis', 'dernier', 'derrière', 'des',
                   'dessous', 'devant', 'différent', 'different', 'différente',
                   'différentes', 'différents', 'dire', 'dit', 'doit', 'donc',
                   'dont', 'du', 'dès', 'désormais', 'else', 'effet', 'elle',
                   'elles', 'en', 'encore', 'entre', 'environ', 'es', 'est',
                   'eue', 'eues', 'eurent', 'eus', 'eusse', 'eussent', 'et',
                   'eusses', 'eussiez', 'eussions', 'eut', 'eux', 'exactement',
                   'eûmes', 'eût', 'eûtes', 'fais', 'fait', 'font', 'furent',
                   'fus', 'fusse', 'fussent', 'fusses', 'fussiez', 'fussions',
                   'fut', 'fûmes', 'fût', 'fûtes', 'gens', 'ha', 'il', 'ils',
                   'importe', 'j', 'je', 'juste', 'jour', 'l', 'la', 'le',
                   'les', 'leur', 'leurs', 'lors', 'lui', 'là', 'm', 'ma',
                   'mais', 'malgré', 'me', 'mes', 'moi', 'moins', 'mon',
                   'même', 'mêmes', 'n', 'ne', 'ni', 'nombreuses', 'nombreux',
                   'non', 'nos', 'notamment', 'notre', 'nous', 'nouveau', 'on',
                   'ont', 'ou', 'où', 'par', 'parce', 'parfois', 'parler',
                   'pas', 'pendant', 'pense', 'permet', 'peu', 'peut',
                   'peuvent', 'plein', 'plus', 'plusieurs', 'plutôt', 'lequel',
                   'possible', 'pour', 'pourquoi', 'pourrait', 'près', 'puis',
                   'qu', 'quand', 'que', 'quel', 'quelle', 'quelque',
                   'quelques', 'qui', 'quoi', 'rare', 'rares', 'rien', 's',
                   'sa', 'screen', 'sait', 'sans', 'se', 'selon', 'semble',
                   'sera', 'serai', 'seraient', 'serais', 'serait', 'seras',
                   'serez', 'seriez', 'serions', 'serons', 'seront', 'ses',
                   'seul', 'seulement', 'si', 'soient', 'sois', 'soit',
                   'sommes', 'son', 'sont', 'soyez', 'soyons', 'strictement',
                   'suis', 'suit', 'suivre', 'sur', 'surtout', 't', 'ta', 'te',
                   'telles', 'tes', 'toi', 'ton', 'toujours', 'tous', 'tout',
                   'toute', 'toutefois', 'toutes', 'trop', 'très', 'tu', 'té',
                   'un', 'une', 'unique', 'vers', 'vos', 'votre', 'vous', 'vu',
                   'y', 'à', 'ça', 'étaient', 'étais', 'était', 'étant',
                   'étante', 'étantes', 'étants', 'étiez', 'étions', 'été',
                   'étée', 'étées', 'étés', 'êtes', 'être', 'etaient', 'etais',
                   'etait', 'etant', 'etante', 'etantes', 'etants', 'etiez',
                   'etions', 'ete', 'semblent', 'r', 't', 'y', 'u', 'i', 'o',
                   'p', 'q', 's', 'd', 'f', 'ces', 'cher', 'du', 'encore',
                   'etee', 'etees', 'etes', 'etes', 'etre', 'a', 'z', 'e',
                   'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b',
                   'n']

with open('stopwords.p', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(list_stop_words)

with open('stop_words.p', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    test = mon_depickler.load()


stop_words = pickle.load(open('/Users/Elise/Documents/Travail/M1_SID/SID_Terrorisme/test/stopwords.p', 'rb'))
np.unique(stop_words)


def tf(articles):
    a = []
    for i in range(len(articles)):
        a.append(str(articles[i]))
    unique, counts = np.unique(a, return_counts=True)
    dict_words = {}
    for uk, ct in zip(unique, counts):
        sum_words = np.sum(counts)
        dict_words[uk] = ct/sum_words
        continue
    return dict_words


stopwords = list(set(stop_words + list(list_stop_words)))
