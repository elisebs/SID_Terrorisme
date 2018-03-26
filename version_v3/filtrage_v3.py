# -*- coding: utf-8 -*-
"""
Nettoyage des données
"""

import re
import json
import spacy
import pickle
nlp = spacy.load('fr')
import csv
import os

# Ici, on charge une liste de stopwords :
stop_words = pickle.load(open('/Users/sofian/Documents/Projet_att/stopwords.p', 'rb'))

# chemin où les articles filtrés seront mis
path_target = '/Users/sofian/Documents/Projet_att/path_target/'


def clean_symbols(text):

    '''
        La fonction clean_symbols permet de nettoyer l'article c'est-a-dire
        d'enlever toute la ponctuation, les accents, de remplacer les
        apostrophes par des blancsou bien supprimer des symboles.
    '''

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


def tokeniz(text):
    '''
        La fonction tokenize va permettre d'obtenir chaque mot separer.
    '''
    doc = nlp(text)
    return doc


# Entites nommes
def handing_entity(tokenize_text):
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


def analys_token(article, text_token, entity_,newspapers,identi_article,date_p):
    """
        Résumé :
            cette fonction permet de créer un dictionnaire regroupant l'id de
            l'article, le nom du journal, le mot, le mot lemmatise, le pos_tag
            du mot, sa position et sa date de publication.
        En entrée :
            - l'article
            - text_token : liste de mot tokenise
            - entity : liste de entités nommées
        En sortie :
            cette fonction renvoie les informations décrites dans le résumé.
    """

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
            "position": i,
            "date_publication": date_p
        }
        i += 1

    # info_without prend les infos du info_token en retirant
    # les stop_words et les ponctuations
    info_without = [token for token in info_token.values() if str(
        token["pos_tag"]) != "STOPWORD" and token["word"] != '.'
        and str(token["pos_tag"]) != "PUNCT"]

    return info_without


def tag_text(article, k):
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
    id_article = k
    date_publication = [x['date_publi'] for x in article]
    # remove punctuation
    clean_text = clean_symbols(str(text))
    # list of entity and list of entity here " " are replace by "_"
    entity, entity_ = handing_entity(tokeniz(clean_text))
    for keys in entity.keys():
        clean_text = clean_text.replace(keys, keys.replace(" ", "_"))
    tokens = tokeniz(clean_text)

    # idemn le journal etait en list, mis en str
    journal = "".join(journal)

    return analys_token(article, tokens, entity_, journal,
                        id_article, date_publication)


path_target_lmnde = "/Users/sofian/Documents/Projet_att/article_total"

list_file = os.listdir(path_target_lmnde)
# del list_file[0] # supprime le '.DS_Store'

# Creation d'une liste pour permettre d'executer les fonctions
data_post_content = []

# Creation d'un csv dans lequel nous mettons les articles filtres
c = csv.writer(open(path_target + "article_filtered.csv", "w"))

'''
    Nous parcourons chaque article pour pouvoir les nettoyer. Ensuite, les
    articles sont inséré dans le csv pour pouvoir par la suite les inserer dans
    la base de donnees.
'''

i = 0
j = 0
for file in list_file:
    i = i+1
    j = j+1
    f = open(path_target_lmnde + '/' + list_file[1], 'rb')
    articles = [json.loads(s.decode('utf-8')) for s in f.readlines()]
    data_post_content.append(tag_text(articles, i))
    if j == 50:
            j = 0
            print(i)

data_final = []
# pour mettre en list de dictonnaire au lieu de list de list
for sublist in data_post_content:
    for item in sublist:
        data_final.append(item)

c.writerow(data_final)
