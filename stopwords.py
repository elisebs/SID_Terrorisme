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
from tqdm import tqdm
nltk.download('stopwords')


def tokeniz(article):
    nlp = spacy.load('fr')
    doc = nlp(article)
    return doc


list_stopwords = []


def get_stopwords():
    # list of spacy stopwords
    # list_stopwords = []
    for find_stopwords in b:
        if find_stopwords.is_stop:
            list_stopwords.extend([find_stopwords])
    for i in range(len(list_stopwords)):
        list_stopwords[i] = str(list_stopwords[i])
    list_stopwords_other = []
    #for i in stop_words:
        #list_stopwords_other.append(i)
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

list_stop_words = ['are', 'also', 'a', 'ai', 'aie', 'aient', 'aies', 'ailleurs', 'ainsi',
                   'ait', 'alors', 'après', 'as', 'assez', 'au', "ajourd'hui", 'aucun',
                   'aucune', 'aura', 'aurai', 'auraient', 'aurais', 'aurait',
                   'auras', 'aurez', 'auriez', 'aurions', 'aurons', 'auront',
                   'aussi', 'autre', 'autres', 'aux', 'avaient', 'avais',
                   'avait', 'avant', 'avec', 'avez', 'aviez', 'avions',
                   'avoir', 'avons', 'ayant', 'ayante', 'ayantes', 'ayants',
                   'ayez', 'ayons', 'beaucoup', 'bien', 'c', 'ce', 'ceci',
                   'cela', 'celle', 'celui', 'certain', 'certaines', 'ces', 'cet'
                   'cette', 'ceux', 'comme', 'comment', 'contre', 'd', 'dans',
                   'de', 'debout', 'depuis', 'dernier', 'derrière', 'des',
                   'dessous', 'devant', 'différent', 'different', 'différente',
                   'différentes', 'différents', 'dire', 'dit', 'doit', 'donc',
                   'dont', 'du', 'dès', 'désormais', 'else', 'effet', 'elle', 'elles',
                   'en', 'encore', 'entre', 'environ', 'es', 'est', 'et', 'eu',
                   'eue', 'eues', 'eurent', 'eus', 'eusse', 'eussent',
                   'eusses', 'eussiez', 'eussions', 'eut', 'eux', 'exactement',
                   'eûmes', 'eût', 'eûtes', 'fais', 'fait', 'font', 'furent',
                   'fus', 'fusse', 'fussent', 'fusses', 'fussiez', 'fussions',
                   'fut', 'fûmes', 'fût', 'fûtes', 'gens', 'ha', 'il', 'ils',
                   'importe', 'j', 'je', 'juste', 'jour', 'l', 'la', 'le', 'lequel',
                   'les', 'leur', 'leurs', 'lors', 'lui', 'là', 'm', 'ma',
                   'mais', 'malgré', 'me', 'mes', 'moi', 'moins', 'mon',
                   'même', 'mêmes', 'n', 'ne', 'ni', 'nombreuses', 'nombreux',
                   'non', 'nos', 'notamment', 'notre', 'nous', 'nouveau', 'on',
                   'ont', 'ou', 'où', 'par', 'parce', 'parfois', 'parler',
                   'pas', 'pendant', 'pense', 'permet', 'peu', 'peut',
                   'peuvent', 'plein', 'plus', 'plusieurs', 'plutôt',
                   'possible', 'pour', 'pourquoi', 'pourrait', 'près', 'puis',
                   'qu', 'quand', 'que', 'quel', 'quelle', 'quelque',
                   'quelques', 'qui', 'quoi', 'rare', 'rares', 'rien', 's',
                   'sa', 'screen', 'sait', 'sans', 'se', 'selon', 'semble', 'semblent',
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
                   'etait', 'etant','etante', 'etantes', 'etants', 'etiez', 'etions', 'ete',
                   'etee', 'etees', 'etes', 'etes', 'etre', 'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f',
          'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n', 'a', 'afin', 'ai', 'aie', 'aient', 'aies', 'ailleurs', 'ainsi',
       'ait', 'alors', 'apres', 'as', 'attendu', 'au', 'aucune',
       "aujourd'hui", 'aupres', 'aura', 'aurai', 'auraient', 'aurais',
       'aurait', 'auras', 'aurez', 'auriez', 'aurions', 'aurons',
       'auront', 'aussi', 'autre', 'autrement', 'autres', 'aux',
       'avaient', 'avais', 'avait', 'avant', 'avec', 'avez', 'aviez',
       'avions', 'avoir', 'avons', 'ayant', 'ayante', 'ayantes', 'ayants',
       'ayez', 'ayons', 'bas', 'bat', 'beaucoup', 'bien', 'c', 'ce',
       'ceci', 'cela', 'celle', 'celle-ci', 'celles', 'celui-ci',
       'cependant', 'certain', 'certaine', 'certaines', 'certains', 'ces',
       'cet', 'cette', 'ceux', 'chacun', 'chacune', 'chaque', 'cher',
       'chez', 'cinq', 'combien', 'comme', 'compris', 'concernant',
       'contre', 'd', 'dans', 'de', 'deja', 'depuis', 'dernier',
       'derniere', 'derriere', 'des', 'desormais', 'deux', 'devant',
       'dire', 'dit', 'doit', 'doivent', 'donc', 'dont', 'douze', 'du',
       'duquel', 'effet', 'egalement', 'elle', 'elles', 'en', 'encore',
       'entre', 'envers', 'es', 'est', 'et', 'etaient', 'etait', 'etant',
       'etre', 'eu', 'eue', 'eues', 'eurent', 'eus', 'eusse', 'eussent',
       'eusses', 'eussiez', 'eussions', 'eut', 'eux', 'eûmes', 'eût',
       'eûtes', 'faisaient', 'faisant', 'fait', 'font', 'furent', 'fus',
       'fusse', 'fussent', 'fusses', 'fussiez', 'fussions', 'fut',
       'fûmes', 'fût', 'fûtes', 'gens', 'hui', 'huit', 'il', 'ils', 'j',
       'je', 'juste', 'l', 'la', 'laquelle', 'le', 'lequel', 'les',
       'lesquels', 'leur', 'leurs', 'longtemps', 'lors', 'lorsque', 'lui',
       'm', 'ma', 'maintenant', 'mais', 'malgre', 'me', 'meme', 'memes',
       'mes', 'moi', 'moins', 'mon', 'multiples', 'même', 'n', 'ne',
       'neanmoins', 'neuf', 'nombreuses', 'non', 'nos', 'notamment',
       'notre', 'nous', 'nouveau', 'on', 'ont', 'onze', 'ou', 'outre',
       'par', 'parfois', 'parler', 'parmi', 'particulier', 'pas',
       'pendant', 'pense', 'personne', 'peu', 'peut', 'peuvent', 'peux',
       'pire', 'plein', 'plus', 'plusieurs', 'pour', 'pourrait',
       'pouvait', 'precisement', 'premier', 'pres', 'proche', 'pu',
       'puis', 'qu', 'quatre', 'que', 'quel', 'quelle', 'quelque',
       'quelques', 'qui', 'quinze', 'quoi', 'remarquable', 'rend',
       'rendre', 'reste', 'restent', 'retour', 'rien', 's', 'sa', 'sans',
       'sauf', 'se', 'sein', 'seize', 'selon', 'semble', 'semblent',
       'sept', 'sera', 'serai', 'seraient', 'serais', 'serait', 'seras',
       'serez', 'seriez', 'serions', 'serons', 'seront', 'ses', 'seul',
       'seule', 'seulement', 'si', 'six', 'soient', 'sois', 'soit',
       'sommes', 'son', 'sont', 'sous', 'souvent', 'soyez', 'soyons',
       'suis', 'sur', 'surtout', 't', 'ta', 'te', 'telle', 'telles',
       'tenir', 'tes', 'toi', 'ton', 'toujours', 'tous', 'tout', 'toute',
       'toutes', 'tres', 'trois', 'tu', 'un', 'une', 'unique', 'va',
       'vers', 'via', 'vingt', 'voici', 'vont', 'vos', 'votre', 'vous',
       'vu', 'y', 'à', 'étaient', 'étais', 'était', 'étant', 'étante',
       'étantes', 'étants', 'étiez', 'étions', 'été', 'étée', 'étées',
       'étés', 'êtes', 'tbody', 'left', 'var', 'jusqu',  'softConnector', 'Aujourd_hui',
       'aujourd_hui', 'priori', 'width:1', 'br9h', 'nen', 'sac', 'tot', 'ok', 'del',
       'the', 'beau','go', 'colors:', 'table.display', 'a', 'abord', 'absolument', 'afin', 'ai', 'ailleurs', 'ainsi',
       'ait', 'allaient', 'allons', 'alors', 'anterieures', 'apres',
       'après', 'as', 'assez', 'attendu', 'au', 'aucun', 'aucune',
       "aujourd'hui", 'aupres', 'auquel', 'aura', 'auraient', 'aurait',
       'auront', 'aussi', 'autre', 'autrement', 'autres', 'autrui', 'aux',
       'auxquelles', 'auxquels', 'avaient', 'avais', 'avait', 'avant',
       'avec', 'avoir', 'avons', 'ayant', 'bas', 'basee', 'bat', 'beau',
       'beaucoup', 'bien', 'boum', 'car', 'ce', 'ceci', 'cela', 'celle',
       'celle-ci', 'celles', 'celles-ci', 'celui', 'celui-ci', 'cent',
       'cependant', 'certain', 'certaine', 'certaines', 'certains',
       'certes', 'ces', 'cet', 'cette', 'ceux', 'ceux-ci', 'chacun',
       'chacune', 'chaque', 'cher', 'chers', 'chez', 'chère', 'ci',
       'cinq', 'cinquantaine', 'cinquante', 'cinquantième', 'cinquième',
       'combien', 'comme', 'comment', 'comparable', 'comparables',
       'compris', 'concernant', 'contre', 'dans', 'de', 'debout',
       'dehors', 'deja', 'delà', 'depuis', 'dernier', 'derniere',
       'derriere', 'derrière', 'des', 'desormais', 'desquelles',
       'desquels', 'dessous', 'dessus', 'deux', 'deuxième', 'devant',
       'devra', 'different', 'differentes', 'differents', 'différent',
       'différente', 'différentes', 'différents', 'dire', 'directe',
       'directement', 'dit', 'dite', 'dits', 'divers', 'diverses', 'dix',
       'dix-huit', 'dix-neuf', 'dix-sept', 'doit', 'doivent', 'donc',
       'dont', 'douze', 'du', 'duquel', 'durant', 'dès', 'désormais',
       'effet', 'egalement', 'elle', 'elle-même', 'elles', 'elles-mêmes',
       'en', 'encore', 'enfin', 'entre', 'envers', 'environ', 'es', 'est',
       'et', 'etaient', 'etais', 'etait', 'etant', 'etc', 'etre', 'eu',
       'eux', 'exactement', 'excepté', 'exterieur', 'fais', 'faisaient',
       'faisant', 'fait', 'façon', 'feront', 'font', 'gens', 'ha', 'hein',
       'hi', 'hop', 'hormis', 'hors', 'hue', 'hui', 'huit', 'huitième',
       'hélas', 'i', 'il', 'ils', 'importe', 'je', 'jusque', 'juste',
       'la', 'laisser', 'laquelle', 'las', 'le', 'lequel', 'les',
       'lesquelles', 'lesquels', 'leur', 'leurs', 'longtemps', 'lors',
       'lorsque', 'lui', 'lui-même', 'là', 'ma', 'maintenant', 'mais',
       'malgre', 'malgré', 'maximale', 'me', 'meme', 'memes', 'merci',
       'mes', 'mien', 'mienne', 'miennes', 'mille', 'mince', 'moi',
       'moi-même', 'moindres', 'moins', 'mon', 'multiple', 'multiples',
       'même', 'mêmes', 'na', 'naturel', 'naturelle', 'naturelles', 'ne',
       'neanmoins', 'necessaire', 'necessairement', 'neuf', 'ni',
       'nombreuses', 'nombreux', 'non', 'nos', 'notamment', 'notre',
       'nous', 'nouveau', 'nul', 'néanmoins', 'nôtre', 'o', 'on', 'ont',
       'onze', 'ou', 'outre', 'ouvert', 'ouverte', 'ouverts', 'où', 'pan',
       'par', 'parce', 'parfois', 'parle', 'parlent', 'parler', 'parmi',
       'partant', 'particulier', 'particulière', 'particulièrement',
       'pas', 'passé', 'pendant', 'pense', 'permet', 'personne', 'peu',
       'peut', 'peuvent', 'peux', 'pire', 'plein', 'plus', 'plusieurs',
       'plutôt', 'possible', 'possibles', 'pour', 'pourquoi', 'pourrais',
       'pourrait', 'pouvait', 'prealable', 'precisement', 'premier',
       'première', 'pres', 'probable', 'probante', 'proche', 'près', 'pu',
       'puis', 'puisque', 'pur', 'pure', 'qu', 'quand', 'quant',
       'quarante', 'quatorze', 'quatre', 'quatrième', 'que', 'quel',
       'quelconque', 'quelle', 'quelles', "quelqu'un", 'quelque',
       'quelques', 'quels', 'qui', 'quiconque', 'quinze', 'quoi', 'rare',
       'rarement', 'rares', 'relative', 'relativement', 'remarquable',
       'rend', 'rendre', 'restant', 'reste', 'restent', 'retour', 'rien',
       'sa', 'sait', 'sans', 'sauf', 'se', 'sein', 'seize', 'selon',
       'semblable', 'semblaient', 'semble', 'semblent', 'sent', 'sept',
       'septième', 'sera', 'seraient', 'serait', 'seront', 'ses', 'seul',
       'seule', 'seulement', 'si', 'sien', 'sienne', 'siennes', 'siens',
       'sinon', 'six', 'sixième', 'soi', 'soi-même', 'soit', 'soixante',
       'son', 'sont', 'sous', 'souvent', 'specifiques', 'strictement',
       'suffisant', 'suffit', 'suis', 'suit', 'suivant', 'suivante',
       'suivantes', 'suivants', 'suivre', 'sur', 'surtout', 'ta', 'tant',
       'tardive', 'te', 'tel', 'telle', 'tellement', 'telles', 'tels',
       'tenant', 'tend', 'tenir', 'tente', 'tes', 'tienne', 'tiens',
       'toi', 'ton', 'touchant', 'toujours', 'tous', 'tout', 'toute',
       'toutefois', 'toutes', 'treize', 'trente', 'tres', 'trois',
       'troisième', 'trop', 'très', 'tu', 'un', 'une', 'unes', 'unique',
       'uns', 'va', 'vais', 'vas', 'vers', 'via', 'vif', 'vifs', 'vingt',
       'vive', 'vives', 'voici', 'voilà', 'vont', 'vos', 'votre', 'vous',
       'vu', 'à', 'ça', 'ès', 'étaient', 'étais', 'était', 'étant', 'été',
       'être']

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