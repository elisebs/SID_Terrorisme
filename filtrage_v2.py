 import re
 import json
 import spacy
+from spacy.lemmatizer import Lemmatizer
 import pickle
 nlp = spacy.load('fr')
 from tqdm import tqdm
@@ -68,6 +69,14 @@ def clean_symbols(text):
     art = art.replace(')', '')
     art = art.replace('<', '')
     art = art.replace('>', '')
+
+    # Replace accent
+    art = art.replace('é', 'e')
+    art = art.replace('è', 'e')
+    art = art.replace('à', 'a')
+    art = art.replace('ç', 'c')
+    art = art.replace('œ', 'oe')
+

     # Replace apostrophes by blanks
     art = re.sub(r'’', ' ', art)
@@ -397,34 +406,12 @@ def analys_token(article, text_token, entity_, is_title=False):
             - post_w : info_token minus the stopwords
             - info_without : processed title without stopwords
     """
-    info_token = {}
-    i = 1
+    list_word = []
     for token in text_token:
-        if token.text in stop_words:
-            tag = "STOPWORD"
-        else:
-            tag = token.pos_
-
-        info_token[i] = {
-            "word": token.text,
-            "lemma": token.lemma_,
-            "pos_tag": tag,
-            "type_entity": entity_[str(token)]
-            if str(token) in entity_.keys()
-            else "",
-            "position": i,
-            "title": (
-                set(str(token.text).upper().replace("_",
-                    " ").split()).issubset(str([x['title'] for x in article]).upper(
-                            ).split(" ")))
-        }
-        i += 1
-
-    info_without = [token for token in info_token.values() if str(
-        token["pos_tag"]) != "STOPWORD" and token["word"] != '.']
-
-
-    return info_without
+        if token.text not in stop_words and token.text != '.':
+            list_word.append(token.lemma_)
+
+    return list_word


 def tag_text(article, is_title=False):
@@ -462,6 +449,9 @@ def tag_text(article, is_title=False):
 data_post_content = []
 data_post_content.append(tag_text(docs, is_title=False))

-w = csv.writer(open("test.csv", "w"))
-w.writerow(["lemma","pos_tag", "position", "title", "type_entiy", "word"])
-w.writerows(data_post_content)
+c = csv.writer(open("test.csv", "w"))
+c.writerows(data_post_content)
+
+#w = csv.writer(open("test.csv", "w"))
+#w.writerow(["lemma","pos_tag", "position", "title", "type_entiy", "word"])
+#w.writerows(data_post_content)
