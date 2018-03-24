""
author:Raphael
""

 
#Installation des packages et chargement des librairies
install.packages("rgdal")
install.packages("plotrix")
install.packages("classInt")
install.packages("cartography")

library(rgdal)
library(plotrix)
library(classInt)
library(cartography)




# Lecture des fichiers shapefiles
pays   <- readOGR(dsn="C:/Users/cmisid/Documents/TableauDeBord/graphique/maps/cultural",layer="ne_110m_admin_0_countries")
grille <- readOGR(dsn="C:/Users/cmisid/Documents/TableauDeBord/graphique/maps/physical",layer="ne_110m_graticules_10")
boite  <- readOGR(dsn="C:/Users/cmisid/Documents/TableauDeBord/graphique/maps/physical",layer="ne_110m_wgs84_bounding_box")

# Projection en Winkel Tripel
pays   <- spTransform(pays,CRS("+proj=wintri"))
boite  <- spTransform(boite,  CRS("+proj=wintri"))
grille <- spTransform(grille, CRS("+proj=wintri"))

# Tracé du planisphère
pdf('C:/Users/cmisid/Documents/TableauDeBord/graphique/monde.pdf',width=10,height=6) # Exportation en PDF
par(mar=c(0,0,0,0)) # Marges nulles

plot(boite, col="white",    border="grey90",lwd=1)
plot(pays,  col="#E6E6E6",  border="#AAAAAA",lwd=1, add=TRUE)
plot(grille,col="#CCCCCC33",lwd=1, add=TRUE)
dev.off() # Enregistrement du fichier


# vecteur de taux d'attaque terroriste par pays
vec=c(0.022, 0.000, NA,    0.000, NA,    NA,    NA, NA,    0.025, 0.003, 0.000, 0.001, NA,    NA,    0.001, 0.002, 0.002, 0.000, 0.001, NA,    NA,      
      NA,    NA,    NA,    NA,    0.000, 0.000, 0.009, 0.018, 0.000, NA,    0.000, NA,    0.001, 0.000, 0.002, NA,    0.001, NA,    NA,    NA,    0.054,
      0.002, 0.003, 0.002, 0.001, 0.000, 0.002, NA,    0.031, 0.000, NA,    0.002, NA,    NA,    0.099, 0.004, 0.057, NA,    0.000, NA,    NA,    NA,
      NA,    0.002, 0.000, NA,    0.001, 0.000, 0.000, 0.001, 0.001, 0.003, 0.003, 0.003, 0.019, 0.061, 0.000, 0.007, NA,    0.001, 0.004, 0.003, 0.001,
      0.004, 0.001, 0.000, NA,    NA,    NA,    0.000, 0.010, 0.000, 0.015, NA,    NA,    NA,    NA,    NA,    NA,    NA,    0.000, 0.004, NA,    0.010,
      NA,    NA,    0.000, NA,    0.001, 0.000, 0.002, NA,    NA,    0.001, 0.002, NA,    NA,    0.000, NA,    0.001, 0.004, 0.023, 0.002, 0.000, NA,
      NA,    0.005, NA,    NA,    0.005, 0.000, NA,    NA,    0.001, 0.038, 0.001, NA,    0.004, 0.002, NA,    0.001, NA,    NA,    NA,    NA,    0.005,
      0.003, 0.000, NA,    0.002, 0.005, 0.000, 0.000, 0.001, NA,    NA,    NA,    NA,    NA,    0.001, NA,    0.044, NA,    NA,    NA,    0.009, 0.001,
      0.001, NA,    0.001, 0.003, 0.000, 0.006, 0.000, NA,    NA)




path = "C:/Users/cmisid/Documents/TableauDeBord/graphique/hdi.csv"
idh = read.csv(path) #données dans la quelle on va inclure le vecteur vec
pays <- merge(pays, idh, by.x="ISO_A3", by.y="Abbreviation")
pays$idh <- 1000*vec

# Génération de l'échelle de couleurs et affectation
col <- findColours(classIntervals(pays$idh, 100, style="pretty"),
                   smoothColors("#663b54",98,"#9b0711"))

# Affectation d'un gris clair pour les données manquantes
col[is.na(pays$idh)] <- "#DDDDDD"

# Génération de la légende
leg <- findColours(classIntervals(round(pays$idh,3), 7, style="pretty"),
                   smoothColors("#663b54",5,"#9b0711"),
                   under="moins de %", over="plus de %", between="-", cutlabels=FALSE)

# Tracé
cairo_pdf('CARTE.pdf',width=10,height=6)
par(mar=c(0,0,0,0),family="Myriad Pro",ps=8)

plot(boite, col="white", border="grey90",lwd=1)
plot(pays,  col=col, border=col,lwd=.8, add=TRUE)
plot(grille,col="#00000009",lwd=1, add=TRUE)

legend(-15000000,-3000000,fill=attr(leg, "palette"),
       legend=gsub("\\.", ",", names(attr(leg,"table"))),
       title = "TERRORISME&ATTENTAT/SID2018")
dev.off()













