import spacy
 import pickle
 nlp = spacy.load('fr')
+from tqdm import tqdm
+
 #stop_words = pickle.load(open('/var/www/html/projet2018/code/filtering/' + 'functions/stopwords.p', 'rb'))
 stop_words = pickle.load(open('/Users/Elise/SID_Terrorisme/stopwords.p', 'rb'))

@@ -464,3 +466,38 @@ def tag_text(article, is_title=False):

 test = tag_text(docs, is_title=False)
 print(test)
+
+with tqdm(desc='JSONing', total=len(docs)) as pbar:
+    tableau_vide = []
+    for item in docs:
+        art = docs[item]
+        data_post_content, filtered = tag_text(art, isTitle=False)
+
+        data_post_title = tag_text(art, isTitle=True)
+        data_post_title = list(data_post_title)
+        for dic in range(len(data_post_title)):
+            data_post_content["position_word"].append(data_post_title[dic])
+        data_post_content["id_art"] = art["id_art"]
+        data_post = []
+        data_post.append(data_post_content)
+#        data_post = json.dumps(data_post, ensure_ascii='False')
+#        print('POST filtering en cours ...')
+#        log_post_filt = post_filtering(data_post)
+#        id_article = log_post_filt.json()[0][0]["message"]["id_article"]
+        ifile = path_post_filt_target + '/' + item + '_post_filtered.json'
+        with open(ifile, 'w', encoding='utf-8') as outfile:
+            json.dump(data_post, outfile, ensure_ascii=False)
+
+        tfidf = get_tf_idf(filtered['list_lemma'], art["id_art"])
+#        tfidf = json.dumps(tfidf, ensure_ascii='False')
+#        print('POST TF en cours ...')
+#        log_post_tf = post_tfidf(tfidf)
+#        print('POST TF OK')
+#        print('log_post_tf = '+str(log_post_tf))
+        ifile = path_post_tf_target + '/' + item + '_post_tf.json'
+        with open(ifile, 'w', encoding='utf-8') as outfile:
+            json.dump(tfidf, outfile, ensure_ascii=False)
+        pbar.update()
+
+import spacy
+x=spacy.load('en')
