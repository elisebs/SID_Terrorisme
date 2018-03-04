#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:11:43 2018

@author: Elise Benois & Sibylle de Gerin-Ricard
"""

import re
import json
import spacy
from spacy.lemmatizer import Lemmatizer
import pickle
nlp = spacy.load('fr')
from tqdm import tqdm
import csv


path_target = '/Users/Elise/SID_Terrorisme/path_target'

#stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/' + 'functions/stopwords.p', 'rb'))
stop_words = pickle.load(open('/Users/Elise/SID_Terrorisme/stopwords.p', 'rb'))

# Enlever les articles où il y a marqué en direct
f = open("/Users/Elise/SID_Terrorisme/article_nouvelobs_v0/art_noob_1_2018-02-01_robot.json",'rb')
docs = [json.loads(s.decode('utf-8')) for s in f.readlines()]

# titres = [x['title'] for x in docs]
# content = [x['content'] for x in docs]

# cleanText

'''
La fonction cleanTokens permet de nettoyer l'article c'est-a-dire d'enlever
toute la ponctuation
'''


#def cleanText(sent):
#    sent = "".join([x if x.isalpha() else " " for x in sent])
#    sent = " ".join(sent.split())
#    return sent


#clean2Text = [cleanText(x) for x in content]

def clean_symbols(text):
    """
        Summary:
            This functions clean the function in order to make a tokenization
            without punctuation.
            Only the sentence-ending punctuations is kept as a point.
        In:
            - text: actual content of the article
        Out:
            - art: cleaned text.
    """

    art = text_modif(text)
    # Replace sentence ending punctuation by full-stop
    art = art.replace('?', '.')
    art = art.replace('!', '.')
    art = art.replace('...', '.')
    art = art.replace('\n', '')
    art = art.replace('\r', '')
    art = art.replace("\\\"", "")
    art = art.replace('\r', '')
    art = art.replace('(', '')
    art = art.replace(')', '')
    art = art.replace('<', '')
    art = art.replace('>', '')
    
    # Replace accent
    art = art.replace('é', 'e')
    art = art.replace('è', 'e')
    art = art.replace('à', 'a')
    art = art.replace('ç', 'c')
    art = art.replace('œ', 'oe')


    # Replace apostrophes by blanks
    art = re.sub(r'’', ' ', art)
    art = art.replace('\n', '')
    art = art.replace('\r', '')
    # Get previous letter
    prev_apostrophe = re.findall('([A-Za-z])\'', art)
    for letter in prev_apostrophe:
        art = re.sub(letter + '\'', letter + ' ', art)
        continue
    # Remove symbols and characters other than letters and digits(accents stay)
    # noinspection Annotator
    art = re.sub(r'[^\w\s\._]', '', art, re.UNICODE)
    # Remove blanks at the beginning or the end.
    art = re.sub('^ +', '', art)
    art = re.sub(' +$', '', art)
    # Replace several consecutive blanks by just one blank.
    art = re.sub(' +', ' ', art)
    # Out: text content without unnecessary characters
    return art


def text_modif(content):
    import re

    # use regular expression to transform few ' in _
    regex = re.compile(r"(?=(.))(?:[Aa]ujourd['’]hui)", flags=re.IGNORECASE)
    content = regex.sub(r"\1ujourd_hui", content)

    regex = re.compile(r"(?=(.))(?:[Pp]rud'homme)", flags=re.IGNORECASE)
    content = regex.sub(r"\1rud_homme", content)

    regex = re.compile(r"(?=(.))(?:[Pp]resqu'[iî]le)", flags=re.IGNORECASE)
    content = regex.sub(r"\1resqu_île", content)

    regex = re.compile(r"(?=(.))(?:[Dd]'abord)", flags=re.IGNORECASE)
    content = regex.sub(r"\1_abord", content)

    regex = re.compile(r"(?=(.))(?:[Gg]rand'm[eè]re)", flags=re.IGNORECASE)
    content = regex.sub(r"\1rand_mère", content)

    regex = re.compile(r"(?=(.))(?:[Gg]rand'p[eè]re)", flags=re.IGNORECASE)
    content = regex.sub(r"\1rand_père", content)

    regex = re.compile(r"(?=(.))(?:[Qq]uelqu'un)", flags=re.IGNORECASE)
    content = regex.sub(r"\1uelqu_un", content)

    regex = re.compile(r"(?=(.))(?:[Cc]hef-d'oeuvre)", flags=re.IGNORECASE)
    content = regex.sub(r"\1hef-d_oeuvre", content)

    regex = re.compile(r"(?=(.))(?:[Hh]ors-d'oeuvre)", flags=re.IGNORECASE)
    content = regex.sub(r"\1ors-d_oeuvre", content)

    regex = re.compile(r"(?=(.))(?:[Ee]ntr'ouvert)", flags=re.IGNORECASE)
    content = regex.sub(r"\1ntre_ouvert", content)

    regex = re.compile(r"(?=(.))(?:[Mm]ain-d'oeuvre)", flags=re.IGNORECASE)
    content = regex.sub(r"\1ain-d_oeuvre", content)

    # use regular expression to transform date with .-/ in date with _
    reg_exp_one = re.compile(r'\d{4}[-/.]\d{2}[-/.]\d{2}')
    matches_list = reg_exp_one.findall(content)
    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '/',
                '_').replace(
                '-',
                '_').replace(
                '.',
                '_'),
            content)

    reg_exp_two = re.compile(r'\d{2}[-/.]\d{2}[-/.]\d{4}')
    matches_list = reg_exp_two.findall(content)
    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '/',
                '_').replace(
                '-',
                '_').replace(
                '.',
                '_'),
            content)

    reg_exp_three = re.compile(r'\d{2}[-/.]\d{2}[-/.]\d{2}')
    matches_list = reg_exp_three.findall(content)
    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '/',
                '_').replace(
                '-',
                '_').replace(
                '.',
                '_'),
            content)

    # use regular expression to transform fraction with / in fraction with _
    reg_exp_four = re.compile(r'[0-9]+[/][0-9]+')
    matches_list = reg_exp_four.findall(content)
    for matche in matches_list:
        content = re.sub(matche, matche.replace('/', '_'), content)

    # use regular expression to transform date with space in date with _
    # list days and months
    days = ['[Ll]undi', '[mM]ardi', '[mM]ercredi', '[Jj]eudi', '[Vv]endredi',
            '[Ss]amedi', '[Dd]imanche']
    months = ['[Jj]anvier', '[Ff][eé]vrier', '[mM]ars', '[Aa]vril', '[mM]ai',
              '[Jj]uin', '[Jj]uillet', '[Aa]o[uû]t', '[Ss]eptembre',
              '[Oo]ctobre', '[Nn]ovembre', '[Dd][eé]cembre',
              '[Jj]an', '[Ff][eé]v', '[mM]ar', '[Aa]vr', '[mM]ai',
              '[Jj]un', '[Jj]ul', '[Aa]o[uû]', '[Ss]ep',
              '[Oo]ct', '[Nn]ov', '[Dd][eé]c']

    format_days = r'(' + '|'.join(days) + r')? ?'
    format_months = r'(' + '|'.join(months) + r')[^A-Za-z,\.]?'
    pattern_three = re.compile(format_days +
                               r'(\d\d?)? ?' +
                               format_months +
                               r'(\d\d\d?\d?)?')

    reg_exp_five = re.compile(pattern_three)
    matches_list = reg_exp_five.findall(content)

    list_without_month = []
    for matche in matches_list:
        if matche[0] or matche[1] or matche[3]:
            list_without_month.append(matche)

    list_without_month.sort(reverse=True)
    for matche in list_without_month:
        if matche[0] and matche[1] and matche[2] and matche[3]:
            content = re.sub(
                matche[0] +
                ' ' +
                matche[1] +
                ' ' +
                matche[2] +
                ' ' +
                matche[3],
                ''.join(matche),
                content)
        elif not matche[0] and not matche[1]:
            content = re.sub(
                matche[2] +
                ' ' +
                matche[3],
                ''.join(matche),
                content)
        elif not matche[0] and not matche[3]:
            content = re.sub(
                matche[1] +
                ' ' +
                matche[2],
                ''.join(matche),
                content)
        else:
            content = re.sub(
                matche[1] +
                ' ' +
                matche[2] +
                ' ' +
                matche[3],
                ''.join(matche),
                content)

    # use regular expression to transform number with space/. in number with _
    reg_exp_six = re.compile(
            r'[0-9]+[., ][0-9]{3}[., ][0-9]{3}[., ][0-9]{3}[., ][0-9]{3}[., ][0-9]{1,3}')
    matches_list = reg_exp_six.findall(content)

    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '.',
                '_').replace(
                ',',
                '_').replace(
                ' ',
                '_'),
            content)

    reg_exp_seven = re.compile(
        r'[0-9]+[., ][0-9]{3}[., ][0-9]{3}[., ][0-9]{3}[., ][0-9]{1,3}')
    matches_list = reg_exp_seven.findall(content)

    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '.',
                '_').replace(
                ',',
                '_').replace(
                ' ',
                '_'),
            content)

    reg_exp_eight = re.compile(
        r'[0-9]+[., ][0-9]{3}[., ][0-9]{3}[., ][0-9]{1,3}')
    matches_list = reg_exp_eight.findall(content)

    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '.',
                '_').replace(
                ',',
                '_').replace(
                ' ',
                '_'),
            content)

    reg_exp_nine = re.compile(r'[0-9]+[., ][0-9]{3}[., ][0-9]{3}')
    matches_list = reg_exp_nine.findall(content)

    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '.',
                '_').replace(
                ',',
                '_').replace(
                ' ',
                '_'),
            content)

    reg_exp_ten = re.compile(r'[0-9]+[., ][0-9]')
    matches_list = reg_exp_ten.findall(content)

    for matche in matches_list:
        content = re.sub(
            matche,
            matche.replace(
                '.',
                '_').replace(
                ',',
                '_').replace(
                ' ',
                '_'),
            content)
    try:
        # use regular expression to transform deg in space
        reg_exp_eleven = re.compile(r'[a-zA-ÿ]+[deg][0-9]')
        matches_list = reg_exp_eleven.findall(content)

        for matche in matches_list:
            content = re.sub(matche, matche.replace('deg', ' '), content)

        reg_exp_twelve = re.compile(r'[0-9][deg][a-zA-ÿ]+')
        matches_list = reg_exp_twelve.findall(content)
        for matche in matches_list:
            content = re.sub(matche, matche.replace('deg', ' '), content)

        reg_ex_thirteen = re.compile(r'[0-9][deg]')
        matches_list = reg_ex_thirteen.findall(content)
        for matche in matches_list:
            content = re.sub(matche, matche.replace('deg', ' '), content)
    except BaseException:
        print("Deg stuff didn't work this time...")

    return content


# tokenize

'''
La fonction tokenize va permettre d'obtenir chaque mot separer.
'''


def tokeniz(text):  # Tokenize a text with library Spacy
    doc = nlp(text)
    return doc


# b = tokeniz(clean_symbols[0])

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
    list_word = []
    for token in text_token:
        if token.text not in stop_words and token.text != '.':
            list_word.append(token.lemma_)
        
    return list_word


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
        text = [x['title'] for x in article]
    else:
        text = [x['content'] for x in article]
    # remove punctuation
    clean_text = clean_symbols(str(text))
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = handing_entity(tokeniz(clean_text))
    for keys in entity.keys():
        clean_text = clean_text.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(clean_text)

    return analys_token(article, tokens, entity_, is_title=is_title)

data_post_content = []
data_post_content.append(tag_text(docs, is_title=False))

c = csv.writer(open("test.csv", "w"))
c.writerows(data_post_content)

#w = csv.writer(open("test.csv", "w"))
#w.writerow(["lemma","pos_tag", "position", "title", "type_entiy", "word"])
#w.writerows(data_post_content)