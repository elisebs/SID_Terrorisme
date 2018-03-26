import pickle
 nlp = spacy.load('fr')
 from tqdm import tqdm
+import csv
+

 path_target = '/Users/Elise/SID_Terrorisme/path_target'

@@ -398,7 +400,7 @@ def analys_token(article, text_token, entity_, is_title=False):
     info_token = {}
     i = 1
     for token in text_token:
-        if str(token.text) in stop_words:
+        if token.text in stop_words:
             tag = "STOPWORD"
         else:
             tag = token.pos_
@@ -416,22 +418,13 @@ def analys_token(article, text_token, entity_, is_title=False):
                     " ").split()).issubset(str([x['title'] for x in article]).upper(
                             ).split(" ")))
         }
-        i += 1
+        i += 1

     info_without = [token for token in info_token.values() if str(
         token["pos_tag"]) != "STOPWORD" and token["word"] != '.']

-    if not is_title:
-        post_w = {"article": {"date_publication": [x['date_publi'] for x in article],
-                              "name_newspaper": [x['newspaper'] for x in article],
-                              "surname_author": [x['author'] for x in article]
-                              }, "position_word": info_without}
-        #info_token["words"] = [tkn.text for tkn in text_token]
-        info_token["words"] = [tkn.text for tkn in text_token if tkn.tag != "STOPWORD"]
-        info_token["list_lemma"] = [tkn.lemma_ for tkn in text_token]
-        return post_w, info_token
-    else:
-        return info_without
+
+    return info_without


 def tag_text(article, is_title=False):
@@ -466,5 +459,9 @@ def tag_text(article, is_title=False):

     return analys_token(article, tokens, entity_, is_title=is_title)

+data_post_content = []
+data_post_content.append(tag_text(docs, is_title=False))

-data_post_content, filtered = tag_text(docs, is_title=False)
+w = csv.writer(open("test.csv", "w"))
+w.writerow(["lemma","pos_tag", "position", "title", "type_entiy", "word"])
+w.writerows(data_post_content)
