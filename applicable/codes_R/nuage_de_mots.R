# Installer
install.packages("tm")  # pour le text mining
install.packages("SnowballC") # pour le text stemming
install.packages("wordcloud") # générateur de word-cloud 
install.packages("RCurl") 
install.packages("RColorBrewer") # Palettes de couleurs
# Charger
library("tm")
library("SnowballC")
library("wordcloud")
library("RColorBrewer")

# On récupére les 50 mots les plus fréquents dans la base de données pour
# effectuer un nuage de mots et voir les mots les plus fréquents.

filePath = read.csv2("/Users/Elise/Documents/Travail/M1_SID/SID_Terrorisme/TOP50_mots.csv", header = FALSE, sep=";")

wordcloud(words = filePath$V1, freq = filePath$V2, min.freq = 1,
          max.words=500, random.order=FALSE, rot.per=0.40, 
          colors=brewer.pal(10,"Reds"))

# Ici, on a récupéré plus de mots afin de mettre un nuage de mots sur la
# page de couverture.

filePath2 = read.csv2("/Users/Elise/Documents/Travail/M1_SID/SID_Terrorisme/Elise_mots.csv", header = FALSE, sep=";")

wordcloud(words = filePath2$V1, freq = filePath2$V2, min.freq = 1,
          max.words=80, random.order=FALSE, rot.per=0.40, 
          colors=brewer.pal(8, "Set2"))
