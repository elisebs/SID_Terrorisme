# Ecriture des procedures dans un fichier texte 
from datetime import date
import csv

path = "C:/Users/Sibylle/Documents/M1_SID/Semestre2/tdb/BDONNEES/"

# TABLE ARTICLE
# Cette boucle permet de recuperer toutes les informations necessaires pour remplir la table ARTICLE
# On recupere donc ici : l'id_article, le nom du journal et la date de publication
file = open(path + "donnees_article.csv", "w")
writer = csv.writer(file, delimiter=";", quotechar='"', lineterminator='\n')
for i in range(len(real_data_final)):
    id_article = real_data_final[i].get('id_art')
    if id_article != real_data_final[i-1].get('id_art'):
        name_np = real_data_final[i].get('newspaper')
        date_trait1 = (real_data_final[i].get('date_publication'))[0]
        # traitements differents car plusieurs dates etaient sous la forme liste de liste de string
        # alors que d'autres etaient sous la forme liste de string
        if type(date_trait1) == list :
            date_string = date_trait1[0]
        else :    
            date_string = date_trait1
        index = str(date_string).find('/')
        # traitements differents car certaines dates etaient sous la forme annee-mois-date
        # et d'autres sous la forme jour/mois/annee
        if index == -1:
            year_i, month_i, day_i = map(int, date_string.split("-"))
            #date_pub = date(year, day, month)
        else:
            day_i, month_i, year_i = map(int, date_string.split("/"))
            #date_pub = date(year, day, month)
        day=str(day_i)
        if (len(day)==1):
            day="0"+day
        month=str(month_i)
        if (len(month)==1):
            month="0"+month
        year=str(year_i)
        writer.writerow((id_article,
                         "'" + name_np + "'", 
                         "'" + year + "-" + day + "-" + month + "'"))
file.close()

# TABLE WORD
# Cette boucle permet d'encoder de maniere uniforme les differentes variables
for i in range(len(real_data_final)): 
    diction = real_data_final[i]
    for key in diction.keys():
                diction[key] = str(diction[key]).encode('ascii', 'ignore')

# Cette boucle permet de recuperer les differentes informations necessaires pour remplir la table WORD
# On recupere donc ici : l'id mot (auto_increment), le mot, la lemmatisation, le pos-tagging et l'id article 
# on créait 3 fichiers csv différents pour contourner le problème de mémoire d'un csv
file1 = open(path + "donnees_mots1.csv", "w")
writer_1 = csv.writer(file1, delimiter=";", quotechar='"', lineterminator='\n')

file2 = open(path + "donnees_mots2.csv", "w")
writer_2 = csv.writer(file2, delimiter=";", quotechar='"', lineterminator='\n')

file3 = open(path + "donnees_mots3.csv", "w")
writer_3 = csv.writer(file3, delimiter=";", quotechar='"', lineterminator='\n')

for i in range(len(real_data_final)):
    id_word=i+1
    word = (real_data_final[i].get('word')).decode()
    # on enlève toutes les lignes contenant un caractère spécial
    if word.find("\'") == -1 :
        if word.find('\\') == -1 :
            lemma = (real_data_final[i].get('lemma')).decode()
            if lemma.find("\'") == -1 :
                if lemma.find('/') == -1 :
                    if lemma.find('\\') == -1 :
                        if lemma.find('\"') == -1 :
                            if lemma.find('=') == -1 :
                                if lemma.find('*') == -1 : 
                                    if lemma.find('+') == -1 :
                                        if lemma.find ('-') == -1 :
                                            if lemma.find ('[') == -1 :
                                                if lemma.find(']') == -1 :
                                                    # ici on ne garde que les mots avec une lemmatisation < 15 caracteres et les mots > 1 caractère
                                                    # pour eviter de se retrouver avec des mots avec des caracteres speciaux a qui on a attribue une mauvaise lemmatisation
                                                    if (len(lemma)<15 or len(lemma)>1): 
                                                        pos_tag = (real_data_final[i].get('pos_tag')).decode()
                                                        position = (real_data_final[i].get('position')).decode()
                                                        id_article = (real_data_final[i].get('id_art')).decode()
                                                        if i <=1000000 :
                                                            writer_1.writerow((id_word, 
                                                                               "'" + word + "'", 
                                                                               "'" + lemma + "'", 
                                                                               "'" + pos_tag + "'", 
                                                                               position, 
                                                                               id_article))
                                                        elif i >1000000 and i<=2000000 :
                                                            writer_2.writerow((id_word, 
                                                                               "'" + word + "'", 
                                                                               "'" + lemma + "'", 
                                                                               "'" + pos_tag + "'", 
                                                                               position, 
                                                                               id_article))
                                                        else : 
                                                            writer_3.writerow((id_word, 
                                                                               "'" + word + "'", 
                                                                               "'" + lemma + "'", 
                                                                               "'" + pos_tag + "'", 
                                                                               position, 
                                                                               id_article))
file1.close()
file2.close()
file3.close()

# TABLE LOCALISATION
# TXT
# Cette boucle permet de recuperer les differentes informations necessaires pour remplir la table LOCALISATION
# On recupere donc ici : l'id localisation (auto_increment), le pays, la ville et l'id article 
file = open(path + "donnees_localisation.csv", "w")
writer = csv.writer(file, delimiter=";", quotechar='"', lineterminator='\n')
for i in range(len(localisation)):
    id_localisation=i+1
    country_=localisation[i].get('pays')
    country=country_.replace("\'", "_")
    city=localisation[i].get('ville')
    if city != 'internet' :
        if city == 'europe' :
            country = 'europe'
        id_article=localisation[i].get('id_art')
        writer.writerow((id_localisation, 
                         "'"  + country + "'", 
                         "'" + city + "'", 
                         id_article))
file.close()

test=str('coucou je m"appelle \ sibylle ')
liste=['\\', '\"', 'cou']
test.find(liste)

import numpy as np
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0]
