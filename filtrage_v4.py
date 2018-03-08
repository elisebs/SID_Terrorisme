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
import os

stop_words = pickle.load(open('/Users/sofian/Documents/Projet_att/stopwords.p', 'rb'))

# Enlever les articles où il y a marqué en direct
#articles = [json.loads(s.decode('utf-8')) for s in f.readlines()]

# chemin où les dossiers filtrés seront mis
path_target = '/Users/sofian/Documents/Projet_att/path_target/'



# cleanText

'''
La fonction cleanTokens permet de nettoyer l'article c'est-a-dire d'enlever
toute la ponctuation
'''


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


def analys_token(article, text_token, entity_,newspapers,identi_article):
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
    # ici en sortie on aura un dico avec le mot, sa lemmatisation, le pos_tag,
    #la position et si c'est un truc VRAI/FAUX
    
    info_token = {}
    i = 1
    for token in text_token:
        if token.text in stop_words:
            tag = "STOPWORD"
        else:
            tag = token.pos_

        info_token[i] = {
            "id_art": identi_article,
            "newspaper": newspapers,
            "word": token.text,
            "lemma": token.lemma_,
            "pos_tag": tag,
            #"type_entity": entity_[str(token)]
            #if str(token) in entity_.keys()
           # else "",
            "position": i
            #"title": (
            #    set(str(token.text).upper().replace("_",
            #        " ").split()).issubset(str([x['title'] for x in article]).upper(
            #                ).split(" ")))
        }
        i += 1 
    
    #info_without prend les infos du info_token en retirant les stop_words et les ponctuations
    info_without = [token for token in info_token.values() if str(
        token["pos_tag"]) != "STOPWORD" and token["word"] != '.' and str(token["pos_tag"]) != "PUNCT"]
    
    
    #ICI, je prend juste la lemma pour obtenir une liste de mot. (correspond à la table WORD)
    #sans id, car je crois que c'est en auto_increment
    #ici on récupére juste la lemma sans les stopwords
    #list_word = []
    #for token in text_token:
    #    if token.text not in stop_words and token.text != '.':
    #        list_word.append(token.lemma_)
       
    return info_without


def tag_text(article):
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
    text = [x['content'] for x in article]
    journal = [x['newspaper'] for x in article]
    id_article = [x['id_art'] for x in article]
    # remove punctuation
    clean_text = clean_symbols(str(text))
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = handing_entity(tokeniz(clean_text))
    for keys in entity.keys():
        clean_text = clean_text.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(clean_text)

    id_article = "".join(id_article) # car l'id etait en list, je l'ai mis en str
    journal = "".join(journal) # idemn avec journal
    
    return analys_token(article, tokens, entity_,journal,id_article)


#Le problème ici, c'est que file devrait prendre tous les articles de list_file
#sauf qu'on reste toujours sur le meme article... Pourtant que je fais print la boucle
#fonctionne.
#Ensuite, si tu veux faire une sortie par table comme on avait discuté, il faudra
#gérer ce que l'on souhaite dans la fonction analys_token : pour l'instant on
#à la sortie qui correspond à la table WORD c'est-à-dire une liste de mot pour chaque
#article du journal le monde.
    
path_target_lmnde="/Users/sofian/Documents/Projet_att/article_total"

list_file = os.listdir(path_target_lmnde)
#del list_file[0] # supprime le '.DS_Store'

data_post_content = []
c = csv.writer(open(path_target + "article_filtered.csv", "w"))

i=0
j=0
for file in list_file :
    i=i+1
    j=j+1
    f = open(path_target_lmnde+ '/' + file,'rb')
    articles = [json.loads(s.decode('utf-8')) for s in f.readlines()]
    data_post_content.append(tag_text(articles))
    if j == 50:
            j=0
            print(i)

data_final=[] 
for sublist in data_post_content: ## pour mettre en list de dictonnaire au lieu de list de list
    for item in sublist:
        data_final.append(item)
  
c.writerow(data_final)
    