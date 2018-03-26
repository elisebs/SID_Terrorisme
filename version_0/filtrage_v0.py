import pickle
nlp = spacy.load('fr')
from tqdm import tqdm
import csv


 path_target = '/Users/Elise/SID_Terrorisme/path_target'

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
