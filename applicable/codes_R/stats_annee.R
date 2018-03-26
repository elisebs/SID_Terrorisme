# setwd("/Users/sofian/Documents/GitHub/Groupe4_Robot")
setwd("/Users/sofian/Documents/Projet_att")

data=read.csv2("nouv_journaux_annee.csv",sep=";",header=FALSE)
tab <- subset(data, data$V1 != 2018)
plot(tab$V1,tab$V2,main="Evolution du nombre d'articles sur les attentats au cours du temps",type = "l",xlab="Année",ylab="Nombre d'articles",xlim=c(1992,2017))
axis(side=1, at=c(1992, 2017))

data_mois=read.csv2("sof_jouranux_mois.csv",header=FALSE)
hist(data_mois$V1,main="Diagramme en barres des mois de publication des articles", xlab="Mois",ylab="Nombre d'article", col="red",xlim=c(0,12))
