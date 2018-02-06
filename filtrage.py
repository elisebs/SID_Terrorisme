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

# Entites nommes


def handing_entity(tokenize_text):  # Unique named entity version
    """
        Summary:
            we go through a tokenize text (result of the function "tokenize"),
            to find named entity in the text.
        In:
            - tokenize text, result of function "tokeniz()"
        Out:
            - list of named entity, and the same list, but whitespaces
            are replace by _, in order to recognize one entity, as one token in
            the lemmatisation
    """
    ent = {}
    ent_und = {}
    for entity in tokenize_text.ents:
        ent[entity.text] = [entity.start_char, entity.end_char, entity.label_]
        ent_und[entity.text.replace(" ", "_")] = entity.label_
    return ent, ent_und


entity = handing_entity

# stop_words

'''
On veut retirer les stopwords de a liste de mots
'''

'''
for i in b:
    if i in stop_words:
        tag = "STOPWORD"
        continue
'''


def analys_token(article, text_token, entity_, is_title=False):
    """
        Summary:
            This function creates the dictionnary.
            Requires global variable "stop_words"
        In:
            - text_token: list of tokenized word
            - entity_: list of named entities, whitespaces are underscores
            - is_title: boolean:
                    * 'True' if text_token contains the title,
                    * 'False' if it's the actual article content.
        Out:
            - info_token : a dictionnary:
                each compartiment is a dictionnary which contains informations
                for each words
            - post_w : info_token minus the stopwords
            - info_without : processed title without stopwords
    """
    info_token = {}
    i = 1
    for token in text_token:
        if str(token.text) in stop_words:
            tag = "STOPWORD"
        else:
            tag = token.pos_

        info_token[i] = {
            "word": token.text,
            "lemma": token.lemma_,
            "pos_tag": tag,
            "type_entity": entity_[str(token)]
            if str(token) in entity_.keys()
            else "",
            "position": i,
            "title": (
                set(str(token.text).upper().replace("_",
                    " ").split()).issubset(article["title"].upper(
                            ).split(" ")))
        }
        i += 1

    info_without = [token for token in info_token.values() if str(
        token["pos_tag"]) != "STOPWORD" and token["word"] != '.']

    if not is_title:
        post_w = {"article": {"date_publication": article["date_publi"],
                              "name_newspaper": article["newspaper"],
                              "surname_author": article["author"]
                              }, "position_word": info_without}
        info_token["words"] = [tkn.text for tkn in text_token]
        info_token["list_lemma"] = [tkn.lemma_ for tkn in text_token]
        return post_w, info_token
    else:
        return info_without


test = analys_token(docs, b, entity, False) # Voir le .keys()


def tag_text(article, is_title=False):
    """
        Summary:
        In:
            - article: content of the article
            - f_stopwords: boolean used with parameter "with_stopwords"
            from analys_token
        Out:
            2 results (see analys_tokens)
            if is_title = True:
                - a dict with a list of all the words in the title processed
                and without stopwords
           if is_title = False:
               - a list of all the words striped of stopwords
               - a list of all the words
               both with stems and pos-tags and a flag if the word is
               named entity
    """
    if is_title:
        text = article["title"]
    else:
        text = article["content"]
    # remove punctuation
    clean_text = clean2Text(text)
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = handing_entity(tokeniz(clean_text))
    for keys in entity.keys():
        clean_text = clean_text.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(clean_text)

    return analys_token(article, tokens, entity_, is_title=is_title)
