library(cartography)

# Import de données dans la session
data("nuts2006")

# Affichage de couches d'habillage
plot(nuts0.spdf, border = NA, col = NA, bg = "#A6CAE0")
plot(world.spdf, col = "#E3DEBF", border = NA, add = TRUE)
plot(nuts0.spdf, col = "#D1914D", border = "grey80", 
     add = TRUE)


# ajout attentat dans la liste
nuts0.df$attentat=c(166,0,83,928,60,24,2853,151,15,1615,95,17745,0,24,43,135,18,0,0,23,0,
                    11,0,58,0,54,240,237,62,155,5,90,2296,3003)

# Cartographie des attentats des pays en cercles
# proportionnels
propSymbolsLayer(spdf = nuts0.spdf, df = nuts0.df, 
                 var = "attentat", symbols = "circle", col = "#920000", 
                 legend.pos = "topright", legend.title.txt = "Nombre d'occurences \n des pays européens ", 
                 legend.style = "c")

# Ajout des titres, légende, sources, etc.
layoutLayer(title = "Attentats en Europe", 
            author = "", sources="" ,
            scale = NULL)