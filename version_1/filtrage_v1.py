import re
import json
import spacy
from spacy.lemmatizer import Lemmatizer
import pickle
nlp = spacy.load('fr')
from tqdm import tqdm


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


def analys_token(article, text_token, entity_, is_title=False):
              post_w : info_token minus the stopwords
              info_without : processed title without stopwords
    info_token = {}
    i = 1
    list_word = []
     for token in text_token:
        if token.text in stop_words:
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
                    " ").split()).issubset(str([x['title'] for x in article]).upper(
                            ).split(" ")))
        }
        i = 1

    info_without = [token for token in info_token.values() if str(
        token["pos_tag"]) != "STOPWORD" and token["word"] != '.']


    return info_without
        if token.text not in stop_words and token.text != '.':
            list_word.append(token.lemma_)

    return list_word
