import pyodbc
import csv

# Paramètres de CONNEXION A LA BD
host = "DESKTOP-B8MDB56\SIBYLLESQL"
db = "ATTENTATS_VF"
user = ""
pwd = ""
       
conn = pyodbc.connect("DRIVER={SQL Server}; SERVER="+host+";DATABASE="+db+";UID="+user+";PWD="+pwd)
cursor = conn.cursor()

# INSERTION ARTICLES
# ouverture du fichier
f = open('C:/Users/Sibylle/Documents/M1_SID/Semestre2/tdb/BDONNEES/donnees_article.csv', 'r')
file_article = csv.reader(f, delimiter=';', quotechar='"')
# appel à la procédure INSERTION_ARTICLE créée dans la BD
for article in file_article:
    cursor.execute("exec dbo.INSERTION_ARTICLE @pid_article_a = " + article[0] +
                   ", @pname_np = " + article[1] + ", @pdate_pub = " +
                   article[2])
    cursor.commit()
# fermer le fichier
f.close()

# INSERTION MOTS
# ouverture du fichier 1
f = open('C:/Users/Sibylle/Documents/M1_SID/Semestre2/tdb/BDONNEES/donnees_mots1.csv', 'r')
file_words = csv.reader(f, delimiter=';', quotechar='"')
# appel à la procédure INSERTION_WORD créée dans la BD
for word in file_words:
    cursor.execute("exec dbo.INSERTION_WORD @pid_word_w = " + word[0] +
                   ", @pword = " + word[1] + ", @plemma = " +
                   word[2] + ", @ppos_tag = " + word[3] + ", @position = " +
                   word[4] + ", @pid_article_w = " + word[5])
    cursor.commit()
# fermer le fichier
f.close()

# # ouverture du fichier 2
f = open('C:/Users/Sibylle/Documents/M1_SID/Semestre2/tdb/BDONNEES/donnees_mots2.csv', 'r')
file_words = csv.reader(f, delimiter=';', quotechar='"')
# appel à la procédure INSERTION_WORD créée dans la BD
for word in file_words:
    cursor.execute("exec dbo.INSERTION_WORD @pid_word_w = " + word[0] +
                   ", @pword = " + word[1] + ", @plemma = " +
                   word[2] + ", @ppos_tag = " + word[3] + ", @position = " +
                   word[4] + ", @pid_article_w = " + word[5])
    cursor.commit()
# fermer le fichier
f.close()

# ouverture du fichier 3
f = open('C:/Users/Sibylle/Documents/M1_SID/Semestre2/tdb/BDONNEES/donnees_mots3.csv', 'r')
file_words = csv.reader(f, delimiter=';', quotechar='"')
# appel à la procédure INSERTION_WORD créée dans la BD
for word in file_words:
    cursor.execute("exec dbo.INSERTION_WORD @pid_word_w = " + word[0] +
                   ", @pword = " + word[1] + ", @plemma = " +
                   word[2] + ", @ppos_tag = " + word[3] + ", @position = " +
                   word[4] + ", @pid_article_w = " + word[5])
    cursor.commit()
# fermer le fichier
f.close()

# INSERTION LOCALISATION
# ouverture du fichier
f = open('C:/Users/Sibylle/Documents/M1_SID/Semestre2/tdb/BDONNEES/donnees_localisation.csv', 'r')
file_loc = csv.reader(f, delimiter=';', quotechar='"')
# appel à la procédure INSERTION_LOCALISATION créée dans la BD
for loc in file_loc:
    cursor.execute("exec dbo.INSERTION_LOCALISATION @pid_localisation_l = " + loc[0] +
                   ", @pcountry = " + loc[1] + ", @pcity = " +
                   loc[2] + ", @pid_article_l = " + loc[3])
    cursor.commit()
# fermer le fichier
f.close()

# DECONNEXION DE LA BD
conn.close()
 
 






